FROM python:3.12-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip wheel --wheel-dir /app/wheels -r requirements.txt

FROM python:3.12-slim
ENV ENV=PROD
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY . .
RUN pip install --no-cache-dir /wheels/*
ENTRYPOINT ["python", "bot.py"]
