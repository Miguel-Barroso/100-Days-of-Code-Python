import config

"""This module will take the stock_news_message and translate it into the given language."""
import openai

api_key = config.os.getenv("OPEN_AI_API_KEY")

client = openai.OpenAI(api_key=api_key)  # Instatiates a new Open AI Client

# To see which models are available using the current API key
# models = client.models.list()
# for model in models.data:
#     print(model.id)


def get_translation(text, target_lang=""):
    prompt = f"Translate the following news article into {target_lang} while keeping the meaning and tone accurate:\n\n"
    f"{text}"

    r = client.chat.completions.create(
        model="text-davinci-002",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return r.choices[0].message.content
