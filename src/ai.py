from google.api_core import retry

from config import SUPPORTED_LANGUAGES, TARGET_LANGUAGE, gemini_flash_model


@retry.Retry(predicate=retry.if_transient_error)
def translate(text, target_language=TARGET_LANGUAGE):
    if TARGET_LANGUAGE.title() in SUPPORTED_LANGUAGES:
        prompt = f"Translate into {target_language}: {text}"
        translation = gemini_flash_model.generate_content(prompt)
        return translation.text
    return "Target language not supported."
