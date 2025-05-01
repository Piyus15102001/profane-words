
from fastapi import FastAPI
from pydantic import BaseModel
from better_profanity import profanity
import re

app = FastAPI()
profanity.load_censor_words()

class TextInput(BaseModel):
    text: str

def find_profanities(text):

    profane_words = profanity.CENSOR_WORDSET
    found = set()
    for word in profane_words:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            found.add(word)
    return list(found)

@app.post("/check_profanity")
async def check_profanity(input: TextInput):
    user_input = input.text
    has_profanity = profanity.contains_profanity(user_input)
    censored_text = profanity.censor(user_input)
    profane_words = find_profanities(user_input)
    return {
        "original_text": user_input,
        "contains_profanity": has_profanity,
        "censored_text": censored_text,
        "profane_words_found": profane_words
    }

