# app.py

import streamlit as st
import main  # Import main.py

def main_app():
    """Main Streamlit application."""

    st.title("TalentScout Hiring Assistant")
    st.write("Welcome! I'm here to help with your initial screening.")

    main.candidate_form()  # Use the candidate_form from main.py

if __name__ == "__main__":
    main_app()