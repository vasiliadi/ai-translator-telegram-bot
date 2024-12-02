FROM python:3.12-alpine AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip wheel --wheel-dir /app/wheels -r requirements.txt

FROM python:3.12-alpine
ENV ENV=PROD
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY . .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir /wheels/*
ENTRYPOINT ["python", "bot.py"]
