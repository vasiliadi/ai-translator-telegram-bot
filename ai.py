from config import gemini_flash_model, TARGET_LANGUAGE, SUPPORTED_LANGUAGES
from google.api_core import retry


@retry.Retry(predicate=retry.if_transient_error)
def translate(text, target_language=TARGET_LANGUAGE):
    if TARGET_LANGUAGE.title() in SUPPORTED_LANGUAGES:
        prompt = f"Translate into {target_language}: {text}"
        translation = gemini_flash_model.generate_content(prompt)
        return translation.text
    return "Target language not supported."
