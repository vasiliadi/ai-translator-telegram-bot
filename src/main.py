import asyncio

from telebot.util import smart_split
from telegramify_markdown import markdownify

from ai import translate
from config import MAX_MESSAGE_LENGTH, bot
from database import auth, register_user


@bot.message_handler(commands=["start"])
async def handle_start(message):
    if await register_user(
        message.from_user.id,
        message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.username,
    ):
        await bot.send_message(
            message.chat.id,
            "Hi there. I'm a private bot, if you know how to use me, go ahead.",
        )
    else:
        await bot.send_message(
            message.chat.id,
            "You are good to go!",
        )


@bot.message_handler(commands=["info"])
async def handle_info(message):
    await bot.send_message(message.chat.id, f"{message.from_user.id}")


@bot.message_handler(content_types=["text"])
async def handle_text(message):
    try:
        if not await auth(message.from_user.id):
            await bot.send_message(message.chat.id, "You are not approved.")
            return

        translation = await translate(message.text.strip())
        if len(translation) > MAX_MESSAGE_LENGTH:
            chunks = smart_split(translation, 4096)
            for text in chunks:
                await bot.reply_to(
                    message,
                    markdownify(text),
                    parse_mode="MarkdownV2",
                )
                await asyncio.sleep(1)
        else:
            await bot.reply_to(
                message,
                markdownify(translation),
                parse_mode="MarkdownV2",
            )
    except Exception as e:
        await bot.reply_to(message, f"Unexpected: {e}")


if __name__ == "__main__":
    asyncio.run(bot.polling())
