# app/utils/i18n.py
from fastapi import Request

translations = {
    "pt-BR": {
        "currency_not_found": "Moeda não encontrada.",
    },
    "en": {
        "currency_not_found": "Currency not found.",
    }
}

def translate(request: Request, key: str) -> str:
    accept_language = request.headers.get("Accept-Language", "en")
    lang = accept_language.split(",")[0].strip()

    return translations.get(lang, translations["en"]).get(key, key)

