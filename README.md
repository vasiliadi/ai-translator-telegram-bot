# AI translator - telegram bot

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15_|_16-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage

1. Get API keys: [@BotFather](https://t.me/BotFather) and [Gemini](https://ai.google.dev/)
2. Setup DB, for example [Supabase x Postgres](https://supabase.com/database)
3. Edit `.env`
4. Run `python bot.py`

After `/start`, you need to set approved to `True` for wanted user IDs. Depending on your database, you can use [SQL Editor](https://supabase.com/docs/guides/database/overview) for [Supabase x Postgres](https://supabase.com/database) or any other SQL client for another database.

Example of `.env` file:

```text
ENV = "PROD"
TG_API_TOKEN = "your_api_key"
GEMINI_API_KEY = "your_api_key"
DB_PROVIDER = "postgres"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "your_host.supabase.com"
DB_PORT = "6543"
DB_NAME = "postgres"
TARGET_LANGUAGE = "English"
```

Currently [Pony](https://docs.ponyorm.org/api_reference.html#supported-databases) supports 5 database types: `sqlite`, `mysql`, `postgres`, `cockroach` and `oracle`.

After completing these steps, you are ready to send any text to the bot and receive translated text.

## Docs

[PonyORM](https://docs.ponyorm.org/) \
[pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/) \
[google-generativeai](https://ai.google.dev/gemini-api/docs/quickstart?lang=python)

[Telegram Bot API](https://core.telegram.org/bots/api) \
[Gemini language support](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#languages-gemini)
