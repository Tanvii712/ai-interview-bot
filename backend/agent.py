from llm import ask_llm

def generate_questions(role, experience):
    prompt = f"""
    Generate 5 interview questions for:
    Role: {role}
    Experience: {experience}
    """
    return ask_llm(prompt)

def follow_up(question, answer):
    prompt = f"""
    Based on answer:
    Q: {question}
    A: {answer}

    Ask a follow-up question.
    """
    return ask_llm(prompt)