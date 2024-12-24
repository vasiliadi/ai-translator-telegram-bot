# AI translator - telegram bot

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
[![CodeFactor](https://www.codefactor.io/repository/github/vasiliadi/ai-translator-telegram-bot/badge)](https://www.codefactor.io/repository/github/vasiliadi/ai-translator-telegram-bot)

## Usage

1. Get API keys: [@BotFather](https://t.me/BotFather) and [Gemini](https://ai.google.dev/)
2. Setup DB, for example [Supabase x Postgres](https://supabase.com/database)
3. Edit `.env`
4. Run `python main.py`

After `/start`, you need to set approved to `True` for wanted user IDs. Depending on your database, you can use [SQL Editor](https://supabase.com/docs/guides/database/overview) for [Supabase x Postgres](https://supabase.com/database) or any other SQL client for another database.

Example of `.env` file:

```text
ENV = "PROD"
TG_API_TOKEN="your_api_key"
GEMINI_API_KEY="your_api_key"
DB_URL="postgresql+psycopg://user:password@host:port/db"
TARGET_LANGUAGE="English"
```

After completing these steps, you are ready to send any text to the bot and receive translated text.

## SQL Clients

[pgAdmin](https://www.pgadmin.org/) \
[DbVisualizer](https://www.dbvis.com/) \
[Beekeeper Studio](https://www.beekeeperstudio.io/) \
[Navicat](https://www.navicat.com/en/)

## Docs

[SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) \
[pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/) \
[google-genai](https://googleapis.github.io/python-genai/) \
[telegramify-markdown](https://github.com/sudoskys/telegramify-markdown)

[Telegram Bot API](https://core.telegram.org/bots/api) \
[Gemini language support](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#languages-gemini) \
[Gemini v2](https://ai.google.dev/gemini-api/docs/models/gemini-v2)
