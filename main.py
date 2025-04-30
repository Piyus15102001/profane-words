from fastapi import FastAPI
from better_profanity import profanity
from typing import Optional

app = FastAPI()

profanity.load_censor_words()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Profanity Filter API!"}

@app.get("/user/{user_id}")
def read_item(user_id: int, q: Optional[str] = None):
    result = {}
    if q:
        result["contains_profanity"] = profanity.contains_profanity(q)
        result["censored_text"] = profanity.censor(q)
    return {"user_id": user_id, "query": q, **result}
