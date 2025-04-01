# sql.py

import sqlite3
import streamlit as st

def save_candidate_form_data(full_name, email, phone, experience, desired_positions, location, tech_stack):
    """Saves candidate form data to the database."""
    try:
        conn = sqlite3.connect("candidates.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                experience INTEGER NOT NULL,
                desired_positions TEXT NOT NULL,
                location TEXT NOT NULL,
                tech_stack TEXT NOT NULL
            )
        """)

        cursor.execute("""
            INSERT INTO candidates (full_name, email, phone, experience, desired_positions, location, tech_stack)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (full_name, email, phone, experience, ', '.join(desired_positions), location, tech_stack))

        conn.commit()
        conn.close()
        return True 
    except sqlite3.IntegrityError:
        return "Error: Candidate with this email already exists."

def store_answer(email, question, answer):
    """Stores candidate answers to questions."""
    conn = sqlite3.connect("answers.db")
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        """)

    cursor.execute("""
            INSERT INTO answers (email, question, answer)
            VALUES (?, ?, ?)
        """, (email, question, answer))

    conn.commit()
    conn.close()
    return True  