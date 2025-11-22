from deep_translator import GoogleTranslator


def translate(text: str, language: str) -> str:
    """
    this is for translation into other languages
    """

    
    if language == "en":
        return text

    try:
        translated = GoogleTranslator(source="auto", target=language).translate(text)
        return translated
    except Exception:
        
        return f"(translation unavailable) {text}"
