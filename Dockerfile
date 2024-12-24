FROM python:3.12-alpine
ENV ENV=PROD \
    PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
COPY /src requirements.txt ./
RUN uv pip install --no-cache --system -r requirements.txt \
    && rm -f requirements.txt
ENTRYPOINT ["python", "main.py"]
