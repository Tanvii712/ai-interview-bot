from llm import ask_llm

def evaluate_answer(question, answer):
    prompt = f"""
    Evaluate this answer:

    Question: {question}
    Answer: {answer}

    Give:
    - correctness (0-10)
    - clarity (0-10)
    - depth (0-10)
    - strengths
    - weaknesses
    - improvements
    """
    return ask_llm(prompt)