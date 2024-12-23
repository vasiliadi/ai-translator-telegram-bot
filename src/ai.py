from config import (
    GEMINI_CONFIG,
    MODEL_ID,
    SUPPORTED_LANGUAGES,
    TARGET_LANGUAGE,
    gemini_client,
)


def translate(text, target_language=TARGET_LANGUAGE):
    if TARGET_LANGUAGE.title() in SUPPORTED_LANGUAGES:
        prompt = f"Translate into {target_language}: {text}"
        translation = gemini_client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=GEMINI_CONFIG,
        )
        if translation.text is None:
            return "Translation failed."
        return translation.text
    return "Target language not supported."
