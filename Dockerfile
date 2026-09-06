FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src ./src
COPY server_config ./server_config

RUN pip install --no-cache-dir .

EXPOSE 4000

CMD ["gunicorn", "axiom.app:axiom_app", "-c", "server_config/multiprocessing.py"]
