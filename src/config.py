import os

from google import genai
from google.genai import types
from telebot.async_telebot import AsyncTeleBot

if os.getenv("ENV") != "PROD":
    from dotenv import load_dotenv

    load_dotenv()

TG_API_TOKEN = os.environ["TG_API_TOKEN"]
bot = AsyncTeleBot(token=TG_API_TOKEN, disable_web_page_preview=True)


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
gemini_client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_ID = "gemini-2.5-flash"  # gemini-2.0-flash
GEMINI_CONFIG = types.GenerateContentConfig(
    system_instruction="""
        You are a language model specializing in accurate, context-sensitive
        translations.
        Translate each text with precise meaning and maintain the original
        tone and style.
        Adapt idioms, cultural references, and metaphors for naturalness in the target
        language, while providing brief explanations directly in the text if necessary.
        Avoid literal translations unless they are essential.
        When terms have multiple meanings, use the context to select the best fit.
        Do not translate proper nouns or technical terms unless widely recognized
        equivalents exist.
        Ensure consistent terminology, especially for technical or specialized language.
        Use polite, respectful language, adjusting formality as appropriate for the text
        type (e.g., legal, business, casual).
        I want you to only reply the translation, do not write notes or explanations.
        """,
    safety_settings=[
        types.SafetySetting(
            category="HARM_CATEGORY_HARASSMENT",
            threshold="BLOCK_NONE",
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH",
            threshold="BLOCK_NONE",
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
            threshold="BLOCK_NONE",
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold="BLOCK_NONE",
        ),
    ],
    thinking_config=types.ThinkingConfig(thinking_budget=0),  # comment for 2.0-flash
    response_mime_type="text/plain",
    max_output_tokens=8192,
)


MAX_MESSAGE_LENGTH = 4096


TARGET_LANGUAGE = os.environ.get("TARGET_LANGUAGE", "English")


DB_URL = os.environ["DB_URL"]


SUPPORTED_LANGUAGES = [
    "Arabic",
    "Bengali",
    "Bulgarian",
    "Chinese",
    "Croatian",
    "Czech",
    "Danish",
    "Dutch",
    "English",
    "Estonian",
    "Finnish",
    "French",
    "German",
    "Greek",
    "Hebrew",
    "Hindi",
    "Hungarian",
    "Indonesian",
    "Italian",
    "Japanese",
    "Korean",
    "Latvian",
    "Lithuanian",
    "Norwegian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Serbian",
    "Slovak",
    "Slovenian",
    "Spanish",
    "Swahili",
    "Swedish",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Vietnamese",
]
