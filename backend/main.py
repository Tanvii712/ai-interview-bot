from fastapi import FastAPI
from agent import generate_questions
from evaluation import evaluate_answer

app = FastAPI()

# memory (simple)
session = {
    "scores": []
}



@app.post("/questions")
def get_questions(data: dict):
    return {
        "questions": generate_questions(data["role"], data["experience"])
    }

@app.post("/evaluate")
def evaluate(data: dict):
    return {
        "result": evaluate_answer(data["question"], data["answer"])
    }
@app.post("/followup")
def get_followup(data: dict):
    return {
        "followup": follow_up(data["question"], data["answer"])
    }
@app.get("/report")
def report():
    return {
        "message": "Final report feature added"
    }