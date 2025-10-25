from deep_translator import GoogleTranslator

class LanguageService:
    rtl_languages = ["ar", "he", "fa", "ur"]

    def __init__(self, default_lang="en"):
        self.default_lang = default_lang

    def detect_language(self, text):
        if any(char in text for char in "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"):
            return "ar"
        elif any(word in text.lower() for word in ["ako", "ikaw", "siya"]):
            return "fil"
        return "en"

    def translate(self, text, source_lang, target_lang):
        if source_lang == target_lang:
            return text
        try:
            return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        except Exception:
            return text

    def get_direction(self, lang_code):
        return "rtl" if lang_code in self.rtl_languages else "ltr"
