import os

import google.generativeai as genai
from telebot import TeleBot

if os.getenv("ENV") != "PROD":
    from dotenv import load_dotenv

    load_dotenv()

TG_API_TOKEN = os.environ["TG_API_TOKEN"]
bot = TeleBot(token=TG_API_TOKEN, disable_web_page_preview=True)


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
gemini_flash_model = genai.GenerativeModel(
    "models/gemini-1.5-flash-latest",
    generation_config={"max_output_tokens": 8192},
    safety_settings=[
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ],
    system_instruction="""
    You are a language model specializing in accurate, context-sensitive translations.
    Translate each text with precise meaning and maintain the original tone and style.
    Adapt idioms, cultural references, and metaphors for naturalness in the target
    language, while providing brief explanations if necessary. Avoid literal
    translations unless they are essential.
    When terms have multiple meanings, use the context to select the best fit.
    Do not translate proper nouns or technical terms unless widely recognized
    equivalents exist.
    Ensure consistent terminology, especially for technical or specialized language.
    Use polite, respectful language, adjusting formality as appropriate for the text
    type (e.g., legal, business, casual).
    """,
)


MAX_MESSAGE_LENGTH = 4096


TARGET_LANGUAGE = os.environ.get("TARGET_LANGUAGE", "English")


DB_SETTINGS = {
    "provider": os.getenv("DB_PROVIDER"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}


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
    "Afrikaans",
    "Amharic",
    "Assamese",
    "Azerbaijani",
    "Belarusian",
    "Bosnian",
    "Catalan",
    "Cebuano",
    "Corsican",
    "Welsh",
    "Dhivehi",
    "Esperanto",
    "Basque",
    "Persian",
    "Filipino",
    "Frisian",
    "Irish",
    "Scots",
    "Galician",
    "Gujarati",
    "Hausa",
    "Hawaiian",
    "Hmong",
    "Haitian",
    "Armenian",
    "Igbo",
    "Icelandic",
    "Javanese",
    "Georgian",
    "Kazakh",
    "Khmer",
    "Kannada",
    "Krio",
    "Kurdish",
    "Kyrgyz",
    "Latin",
    "Luxembourgish",
    "Lao",
    "Malagasy",
    "Maori",
    "Macedonian",
    "Malayalam",
    "Mongolian",
    "Meiteilon",
    "Marathi",
    "Malay",
    "Maltese",
    "Myanmar",
    "Nepali",
    "Nyanja",
    "Odia",
    "Punjabi",
    "Pashto",
    "Sindhi",
    "Sinhala",
    "Samoan",
    "Shona",
    "Somali",
    "Albanian",
    "Sesotho",
    "Sundanese",
    "Tamil",
    "Telugu",
    "Tajik",
    "Uyghur",
    "Urdu",
    "Uzbek",
    "Xhosa",
    "Yiddish",
    "Yoruba",
    "Zulu",
]