from fastapi import FastAPI
from pydantic import BaseModel
from rps_logic import play_best_of_three

app = FastAPI()

class FashionDecision(BaseModel):
    option1: str
    option2: str

@app.get("/")
def home():
    return {"message": "Welcome to Fashion RPS API!"}

@app.post("/decide")
def decide_what_to_wear(decision: FashionDecision):
    result = play_best_of_three(decision.option1, decision.option2)
    return result
