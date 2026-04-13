🚀 AI Interview Bot (GenAI Project)
📌 Overview

AI-powered interview system that:

Generates interview questions based on role & experience
Evaluates answers using LLM
Provides feedback (correctness, clarity, depth)
🧠 Features
🤖 LLM-powered question generation
📊 Answer evaluation with scoring
⚡ FastAPI backend
🎨 Streamlit frontend
🔐 Secure API key handling (.env)
🛠 Tech Stack
Python
FastAPI
Streamlit
LangChain
OpenAI API
📂 Project Structure
ai-interview-bot/
│── backend/
│   ├── main.py
│   ├── agent.py
│   ├── llm.py
│   ├── evaluation.py
│   ├── .env (ignored)
│
│── frontend/
│   ├── app.py
│
│── requirements.txt
│── README.md
⚙️ Setup Instructions
1. Clone repo
git clone https://github.com/your-username/ai-interview-bot.git
cd ai-interview-bot
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Add API key

Create .env file:

OPENAI_API_KEY=your_key_here
▶️ Run Backend
cd backend
uvicorn main:app --reload
▶️ Run Frontend
cd frontend
streamlit run app.py

📈 Future Improvements
Add voice-based interviews
Add resume-based questions (RAG)
Deploy on cloud (Render / Railway)