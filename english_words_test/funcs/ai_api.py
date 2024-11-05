import google.generativeai as genai
from decouple import config
api_key = config('API_KEY')


def translate(english_word):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-002")
    response = model.generate_content(f"One word answer only. Translate the English word: {english_word} to Bulgarian.")
    return response.text.lower().rstrip()


def check_english_spelling(english_word: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-002")
    response = model.generate_content(f"One word answer only. The correct spelling of {english_word} is? Example: English word: chairre Correct spelling: chair")
    return response.text.lower().rstrip()


def check_bulgarian_spelling(bulgarian_word: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-002")
    response = model.generate_content(f"One word answer only in Cyrillic alphabet. The correct spelling of the Bulgarian word {bulgarian_word} is :")
    return response.text.lower().rstrip()


if __name__ == '__main__':
    pass