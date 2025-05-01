# from fastapi import FastAPI,requests
# from better_profanity import profanity
# app = FastAPI()
# @app.get('/')
# def home():
#     return user_input,requests
#
# user_input = input("Enter a profane words : ")
#
# if profanity.contains_profanity(user_input):
#     print("the profane words.")
# else:
#     print("the not profane words.")
#
# censored_text = profanity.censor(user_input)
# print(censored_text)

from fastapi import FastAPI, Query
from better_profanity import profanity

app = FastAPI()
profanity.load_censor_words()

@app.get("/")
def check_profanity(text: str = Query(..., description="Text to check for profanity")):
    """
    Check if the input text contains profanity and return the censored version.
    """
    contains = profanity.contains_profanity(text)
    censored = profanity.censor(text)
    return {
        "original_text": text,
        "contains_profanity": contains,
        "censored_text": censored
    }
