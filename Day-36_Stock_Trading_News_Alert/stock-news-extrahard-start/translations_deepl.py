import config

"""This module will take the stock_news_message and translate it into the given language."""
import deepl

api_key = config.os.getenv("DEEPL_API_KEY")

def get_translation(text, target_lang="JA"):
    translator = deepl.Translator(api_key)

    r = translator.translate_text(text, target_lang=target_lang)

    return r.text
