import os
from openai import OpenAI
import streamlit as st

# Initialize OpenAI client
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Define questions
questions = [
    {
        "text": """Find the sum: 38,075 + 991,002 + 75,600 =""",
        "answer": "1096677",
        "type": "sum"
    },
    {
        "text": """Find the difference: 6,732,189 - 5,401,207 =""",
        "answer": "1330982",
        "type": "difference"
    },
    {
        "text": """Find the product: 6 × 230,000 =""",
        "answer": "1380000",
        "type": "product"
    },
    {
        "text": """Divide: 3,051,000 ÷ 5 =""",
        "answer": "610200",
        "type": "division"
    },
]

# Initialize session state variables
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

if 'user_score' not in st.session_state:
    st.session_state.user_score = 0

if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ''

def check_answer(user_input):
    """Checks the user's answer and updates score."""
    correct_answer = questions[st.session_state.current_question_index]["answer"]
    if user_input == correct_answer:
        st.session_state.user_score += 1
        return f"Correct! You earned 1 mark. Your score is now {st.session_state.user_score}"
    else:
        return f"Incorrect. The correct answer is {correct_answer}"

# Main application logic
if __name__ == "__main__":
    if st.session_state.current_question_index < len(questions):
        question_text = questions[st.session_state.current_question_index]["text"]
        st.write(question_text)

        # User input and answer check
        user_answer = st.text_input("Answer", value=st.session_state.user_answer)

        if st.button("Submit Answer"):
            feedback = check_answer(user_answer)
            st.write(feedback)

            # Store the user's answer temporarily to clear it later
            st.session_state.user_answer = user_answer

    # Button to display next question (if available)
    if st.session_state.current_question_index < len(questions) - 1:
        if st.button("Next Question"):
            # Move to the next question and clear previous answer
            st.session_state.current_question_index += 1
            st.session_state.user_answer = ''
            # Rerun the app to clear previous content and display the next question
            st.experimental_rerun()