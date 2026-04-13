import streamlit as st
import requests

st.title("🤖 AI Interview System")

role = st.text_input("Role")
exp = st.selectbox("Experience", ["Fresher", "Mid", "Senior"])

if st.button("Generate Questions"):
    res = requests.post("http://127.0.0.1:8000/questions",
                        json={"role": role, "experience": exp})
    st.write(res.json())

question = st.text_input("Question")
answer = st.text_area("Answer")

if st.button("Evaluate"):
    res = requests.post("http://127.0.0.1:8000/evaluate",
                        json={"question": question, "answer": answer})
    st.write(res.json())