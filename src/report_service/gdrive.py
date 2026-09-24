"""
Google Drive upload helper for bulk report delivery.

Handles 100–1000+ files with parallel uploads, retry on transient
errors, and a progress manifest so failed runs can resume.

Setup (one-time):
  1. Go to https://console.cloud.google.com
  2. Create a project (or reuse one) → enable the Google Drive API
  3. Credentials → Create OAuth 2.0 Client ID → Desktop app
  4. Download the JSON and save it as:
       src/report_service/credentials.json
  5. pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
  6. First run opens a browser for consent; after that a token is cached.
"""

from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SERVICE_DIR = Path(__file__).resolve().parent
CREDENTIALS_PATH = SERVICE_DIR / "credentials.json"
TOKEN_PATH = SERVICE_DIR / "token.json"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

ANYONE_READER_PERMISSION = {"type": "anyone", "role": "reader"}

MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0
MAX_WORKERS = 10

MIME_MAP = {
    ".pdf": "application/pdf",
    ".json": "application/json",
    ".typ": "text/plain",
}


def authenticate() -> Credentials:
    """Return valid credentials, refreshing or prompting as needed."""
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_PATH.exists():
                raise FileNotFoundError(
                    f"Missing {CREDENTIALS_PATH}\n"
                    "Download OAuth credentials from Google Cloud Console "
                    "and save them there. See docstring for steps."
                )
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")

    return creds


def _build_service(creds: Credentials):
    return build("drive", "v3", credentials=creds)


def _retry(fn, *args, **kwargs):
    """Call fn with exponential backoff on transient Drive errors."""
    backoff = INITIAL_BACKOFF
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return fn(*args, **kwargs)
        except HttpError as e:
            code = e.resp.status
            if code in (429, 500, 502, 503) and attempt < MAX_RETRIES:
                time.sleep(backoff)
                backoff = min(backoff * 2, 30)
                continue
            raise
        except (ConnectionError, TimeoutError):
            if attempt < MAX_RETRIES:
                time.sleep(backoff)
                backoff = min(backoff * 2, 30)
                continue
            raise


def _get_or_create_folder(service, name: str, parent_id: str | None = None) -> str:
    """Find a folder by name under parent, or create it. Returns folder ID."""
    query = f"name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    if parent_id:
        query += f" and '{parent_id}' in parents"

    def _list():
        return service.files().list(q=query, spaces="drive", fields="files(id, name)", pageSize=1).execute()

    results = _retry(_list)
    files = results.get("files", [])
    if files:
        return files[0]["id"]

    metadata = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder",
    }
    if parent_id:
        metadata["parents"] = [parent_id]

    def _create():
        return service.files().create(body=metadata, fields="id").execute()

    folder = _retry(_create)
    return folder["id"]


def ensure_folder_path(service, path_parts: list[str]) -> str:
    """Create nested folder hierarchy. Returns the deepest folder ID."""
    parent_id = None
    for part in path_parts:
        parent_id = _get_or_create_folder(service, part, parent_id)
    return parent_id


def _make_public(service, file_id: str) -> None:
    """Grant 'anyone with the link' read access to a file."""

    def _do():
        service.permissions().create(
            fileId=file_id,
            body=ANYONE_READER_PERMISSION,
            fields="id",
        ).execute()

    _retry(_do)


def _upload_single(creds: Credentials, local_path: Path, folder_id: str) -> dict:
    """Upload one file, make it public, return metadata with shareable link."""
    service = _build_service(creds)
    mime = MIME_MAP.get(local_path.suffix, "application/octet-stream")
    metadata = {"name": local_path.name, "parents": [folder_id]}
    media = MediaFileUpload(str(local_path), mimetype=mime, resumable=True)

    def _do_upload():
        return service.files().create(body=metadata, media_body=media, fields="id, name, webViewLink").execute()

    info = _retry(_do_upload)
    _make_public(service, info["id"])
    return info


def _load_progress(progress_path: Path) -> set[str]:
    """Load set of already-uploaded filenames from a prior run."""
    if not progress_path.exists():
        return set()
    data = json.loads(progress_path.read_text(encoding="utf-8"))
    return {entry["name"] for entry in data}


def _save_progress(progress_path: Path, uploaded: list[dict]) -> None:
    progress_path.write_text(json.dumps(uploaded, ensure_ascii=False, indent=2), encoding="utf-8")


def upload_batch(
    file_paths: list[Path],
    folder_parts: list[str],
    max_workers: int = MAX_WORKERS,
) -> list[dict]:
    """
    Authenticate, create the folder hierarchy, and upload all files
    in parallel with retry and resume support.

    Args:
        file_paths:   list of local PDF/JSON paths to upload
        folder_parts: e.g. ["Axiom", "Law", "2026-09-21", "14"]
        max_workers:  concurrent upload threads (default 10)

    Returns:
        list of Drive file metadata dicts (id, name, webViewLink)
    """
    creds = authenticate()
    service = _build_service(creds)

    # Create folders upfront (sequential, only 3-4 API calls)
    folder_id = ensure_folder_path(service, folder_parts)

    # Resume: skip files already uploaded in a prior attempt
    progress_path = file_paths[0].parent / "_upload_progress.json"
    already_done = _load_progress(progress_path)
    remaining = [p for p in file_paths if p.name not in already_done]

    if already_done:
        print(f"  Resuming — {len(already_done)} already uploaded, {len(remaining)} remaining")

    uploaded: list[dict] = []
    if progress_path.exists():
        uploaded = json.loads(progress_path.read_text(encoding="utf-8"))

    errors: list[str] = []
    total = len(remaining)

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_upload_single, creds, path, folder_id): path for path in remaining}
        for done_count, future in enumerate(as_completed(futures), 1):
            path = futures[future]
            try:
                info = future.result()
                uploaded.append(info)
                _save_progress(progress_path, uploaded)
                print(f"  [{done_count}/{total}] {info['name']}")
            except Exception as exc:
                msg = f"  [{done_count}/{total}] FAIL {path.name}: {exc}"
                print(msg)
                errors.append(msg)

    # Clean up progress file on full success
    if not errors and progress_path.exists():
        progress_path.unlink()

    if errors:
        print(f"\n{len(errors)} upload failure(s) — re-run to resume.")

    return uploaded
