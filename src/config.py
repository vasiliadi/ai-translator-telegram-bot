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
MODEL_ID = "gemini-3-flash-preview"
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
            category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
    ],
    thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.HIGH),
    response_mime_type="text/plain",
)


TARGET_LANGUAGE = os.environ.get("TARGET_LANGUAGE", "English")


DB_URL = os.environ["DB_URL"]


SUPPORTED_LANGUAGES = [
    "Afrikaans",
    "Albanian",
    "Amharic",
    "Arabic",
    "Armenian",
    "Assamese",
    "Azerbaijani",
    "Basque",
    "Belarusian",
    "Bengali",
    "Bosnian",
    "Bulgarian",
    "Catalan",
    "Cebuano",
    "Corsican",
    "Croatian",
    "Czech",
    "Danish",
    "Dhivehi",
    "Dutch",
    "English",
    "Esperanto",
    "Estonian",
    "Finnish",
    "French",
    "Frisian",
    "Galician",
    "Georgian",
    "German",
    "Greek",
    "Gujarati",
    "Haitian Creole",
    "Hausa",
    "Hawaiian",
    "Hebrew",
    "Hindi",
    "Hmong",
    "Hungarian",
    "Icelandic",
    "Igbo",
    "Indonesian",
    "Irish",
    "Italian",
    "Japanese",
    "Javanese",
    "Kannada",
    "Kazakh",
    "Khmer",
    "Korean",
    "Krio",
    "Kurdish",
    "Kyrgyz",
    "Lao",
    "Latin",
    "Latvian",
    "Lithuanian",
    "Luxembourgish",
    "Macedonian",
    "Malagasy",
    "Malay",
    "Malayalam",
    "Maltese",
    "Maori",
    "Marathi",
    "Mongolian",
    "Nepali",
    "Norwegian",
    "Pashto",
    "Persian",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Romanian",
    "Russian",
    "Samoan",
    "Scots Gaelic",
    "Serbian",
    "Sesotho",
    "Shona",
    "Sindhi",
    "Slovak",
    "Slovenian",
    "Somali",
    "Spanish",
    "Sundanese",
    "Swahili",
    "Swedish",
    "Tajik",
    "Tamil",
    "Telugu",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Urdu",
    "Uyghur",
    "Uzbek",
    "Vietnamese",
    "Welsh",
    "Xhosa",
    "Yiddish",
    "Yoruba",
    "Zulu",
]
