import streamlit as st
import random
import time


st.title("📝 Quiz Application")

queshions =[
    {
        "question": "What is the capital of Pakistan?",
        "option1": ["Islamabad", "Karachi" , "Lahore" , "Quetta"],
        "answer" : "Islamabad"
    },
       {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(queshions)

queshion = st.session_state.current_question

st.subheader(queshion["question"])

selected_option = st.radio("Choose your answer" , queshion["options"], key="answer")
if st.button("Submit Answer"):
    if selected_option == queshion["answer"]:
       st.success("✅ Correct!")
       st.balloons()
    else :
       st.error("❌ Incorrect! the correct answer is " + queshion["answer"])
 
    time.sleep(3)

    st.session_state.current_question = random.choice(queshions)
  # rerun the app to display the next queshion
    st.rerun()
