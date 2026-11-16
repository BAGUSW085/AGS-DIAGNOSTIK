# Production Dockerfile — AGOS SMART DIAGNOSTIK by Agos Corporation
# Siap deploy 24/7 ke Railway, Render, Fly.io, atau Cloud Run
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app/backend

COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/backend/requirements.txt

COPY backend /app/backend

EXPOSE 8000

# Jika volume persisten /data dipasang (misal di Railway/Fly), salin DB awal bila belum ada
CMD ["sh", "-c", "if [ -d /data ] && [ -w /data ] && [ -z \"$DATABASE_URL\" ]; then if [ ! -f /data/bengkel_masa_depan.db ] && [ -f /app/backend/bengkel_masa_depan.db ]; then cp /app/backend/bengkel_masa_depan.db /data/bengkel_masa_depan.db; fi; export DATABASE_URL='sqlite+aiosqlite:////data/bengkel_masa_depan.db'; fi; exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
