FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend ./backend
COPY docker-entrypoint.sh .
ENV FLASK_APP=backend/__main__.py
CMD ["/app/docker-entrypoint.sh"]
