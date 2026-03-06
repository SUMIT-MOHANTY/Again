FROM python:3.11-slim AS builder\nWORKDIR /app\nCOPY backend/requirements.txt /app/\nRUN pip install --upgrade pip && pip install -r requirements.txt\n\nFROM python:3.11-slim AS runtime\nWORKDIR /app\nCOPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages\nCOPY backend/ /app/\nCOPY .env.example /app/.env.example\n\n# Declare build‑time arguments matching .env.example\nARG POSTGRES_USER\nARG POSTGRES_PASSWORD\nARG POSTGRES_DB\nARG POSTGRES_HOST\nARG POSTGRES_PORT\nARG REDIS_HOST\nARG REDIS_PORT\nARG JWT_SECRET\nARG AZURE_OPENAI_ENDPOINT\nARG AZURE_OPENAI_KEY\n\n# Transfer ARG values to runtime ENV (fallback to .env.example)\nENV POSTGRES_USER=${POSTGRES_USER} \
    POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    POSTGRES_DB=${POSTGRES_DB} \
    POSTGRES_HOST=${POSTGRES_HOST} \
    POSTGRES_PORT=${POSTGRES_PORT} \
    REDIS_HOST=${REDIS_HOST} \
    REDIS_PORT=${REDIS_PORT} \
    JWT_SECRET=${JWT_SECRET} \
    AZURE_OPENAI_ENDPOINT=${AZURE_OPENAI_ENDPOINT} \
    AZURE_OPENAI_KEY=${AZURE_OPENAI_KEY}\n\nENV PYTHONUNBUFFERED=1\nCMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]\n