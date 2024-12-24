from config import (
    GEMINI_CONFIG,
    MODEL_ID,
    SUPPORTED_LANGUAGES,
    TARGET_LANGUAGE,
    gemini_client,
)


async def translate(text, target_language=TARGET_LANGUAGE):
    if TARGET_LANGUAGE.title() in SUPPORTED_LANGUAGES:
        prompt = f"Translate into {target_language}: {text}"
        translation = await gemini_client.aio.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=GEMINI_CONFIG,
        )
        return "Translation failed." if translation.text is None else translation.text
    return "Target language not supported."
