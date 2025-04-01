# main.py

import streamlit as st
from langchain_groq import ChatGroq
import sql  

# Initialize AI Model

def initialize_llama():
    return ChatGroq(
        max_tokens=100,
        temperature=1,
        groq_api_key="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",  
        model_name="llama-3.3-70b-versatile"
    )

llm = initialize_llama()

def generate_interview_questions(tech_stack):
    prompt = f"""
    You are an expert interviewer. Generate 3 technical questions based on the following tech stack: {tech_stack}.
    """
    response = llm.invoke(prompt)
    questions = response.content.strip().split("\n")
    return questions[:3]  # Return top 3 questions
    
def candidate_form():
    with st.form("candidate_details"):
        full_name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email address")
        phone = st.text_input("Phone Number", placeholder="Enter your phone number")
        years_experience = st.number_input("Years of Experience", min_value=0, step=1)
        desired_positions = st.multiselect(
            "Desired Position(s)",
            ["AI/ML Engineer", "Data Scientist", "Software Engineer", "DevOps Engineer"],
        )
        current_location = st.text_input("Current Location", placeholder="Enter your current location")
        tech_stack = st.text_area("Tech Stack (comma-separated)", placeholder="e.g., Python, TensorFlow, SQL")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not all([full_name, email, phone, years_experience, desired_positions, current_location, tech_stack]):
                st.error("Please fill in all required fields.")
                return

            result = sql.save_candidate_form_data(
                full_name, email, phone, years_experience, desired_positions, current_location, tech_stack
            )
            if result is True:
                st.success("Candidate data saved successfully!")
                interview_questions_and_answers(email,tech_stack) #collect answers.
                
def interview_questions_and_answers(email, tech_stack):
    questions = generate_interview_questions(tech_stack)
    for idx, question in enumerate(questions, 1):
                    st.write(f"**Q{idx}:** {question}")  # Display question
                    st.text_area(f"Your Answer for Q{idx} ")
                
            
            
                    
            