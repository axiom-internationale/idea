FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src ./src
COPY server_config ./server_config

RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["gunicorn", "axiom.app:app", "-c", "server_config/multiprocessing.py"]
