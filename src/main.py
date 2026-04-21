import asyncio

from telegramify_markdown import telegramify
from telegramify_markdown.content import ContentType

from ai import translate
from config import bot
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
        results = await telegramify(translation, max_message_length=4090)
        for item in results:
            if item.content_type == ContentType.TEXT:
                await bot.send_message(
                    message.chat.id,
                    item.text,
                    entities=[e.to_dict() for e in item.entities],
                )
            elif item.content_type == ContentType.PHOTO:
                await bot.send_photo(
                    message.chat.id,
                    (item.file_name, item.file_data),
                    caption=item.caption_text or None,
                    caption_entities=[e.to_dict() for e in item.caption_entities]
                    or None,
                )
            elif item.content_type == ContentType.FILE:
                await bot.send_document(
                    message.chat.id,
                    (item.file_name, item.file_data),
                    caption=item.caption_text or None,
                    caption_entities=[e.to_dict() for e in item.caption_entities]
                    or None,
                )

    except Exception as e:
        await bot.reply_to(message, f"Unexpected: {e}")


if __name__ == "__main__":
    asyncio.run(bot.polling())
