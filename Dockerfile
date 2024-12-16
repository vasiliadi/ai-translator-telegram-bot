FROM python:3.12-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir pip -U \
    && pip wheel --wheel-dir /app/wheels -r requirements.txt

FROM python:3.12-alpine
ENV ENV=PROD
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY /src .
RUN pip install --no-cache-dir pip -U \
    && pip install --no-cache-dir /wheels/*
ENTRYPOINT ["python", "bot.py"]
