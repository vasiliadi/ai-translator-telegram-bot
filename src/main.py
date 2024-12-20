from telebot.util import smart_split
from telegramify_markdown import markdownify

from ai import translate
from config import MAX_MESSAGE_LENGTH, bot
from database import auth, register_user


@bot.message_handler(commands=["start"])
def handle_start(message):
    if register_user(
        message.from_user.id,
        message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.username,
    ):
        bot.send_message(
            message.chat.id,
            "Hi there. I'm a private bot, if you know how to use me, go ahead.",
        )
    else:
        bot.send_message(
            message.chat.id,
            "You are good to go!",
        )


@bot.message_handler(commands=["info"])
def handle_info(message):
    bot.send_message(message.chat.id, f"{message.from_user.id}")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if not auth(message.from_user.id):
        bot.send_message(message.chat.id, "You are not approved.")
        return

    try:
        translation = translate(message.text.strip())
        if len(translation) > MAX_MESSAGE_LENGTH:
            chunks = smart_split(translation, 4096)
            for text in chunks:
                bot.reply_to(
                    message,
                    markdownify(text),
                    parse_mode="MarkdownV2",
                )
        else:
            bot.reply_to(message, markdownify(translation), parse_mode="MarkdownV2")
    except Exception as e:
        bot.reply_to(message, f"Unexpected: {e}")


if __name__ == "__main__":
    bot.infinity_polling(timeout=20)
