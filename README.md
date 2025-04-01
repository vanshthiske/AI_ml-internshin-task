Project Title: AI/ML Intern Assignment: TalentScout Hiring Assistant  
Project Description: This project involves the development of an intelligent Hiring Assistant chatbot for 
"TalentScout," a fictional recruitment agency specializing in technology placements. The application is 
designed to streamline the initial candidate screening process by gathering essential information and 
posing relevant technical questions based on the candidate's declared tech stack.  
Purpose: The primary goal of this project is to demonstrate the ability to:  
• Utilize Large Language Model Meta AI (llama) effectively for candidate interaction.  
• Design and implement a user-friendly interface for chatbot interaction.  
• Develop prompts that guide the LLM to gather information and generate relevant technical 
questions. 
• Handle data securely and comply with privacy standards. 
Functionality: 
User Interface (Streamlit): 
A clean and intuitive web interface is developed using Streamlit, allowing candidates to interact with the 
chatbot. 
The interface provides an easy way for candidates to input their data. 
The interface provides clear and sequential question and answer sections.  
Candidate Information Gathering: 
The chatbot collects essential candidate details, including: 
• Full Name 
• Email Address  
• Phone Number 
• Years of Experience  
• Desired Position(s)  
• Current Location  
• Tech Stack  
Technical Question Generation:  
Based on the candidate's specified tech stack, the chatbot generates tailored technical questions to assess 
their proficiency. *  
Technical Specifications: 
• Programming Language: Python * ** 
• Libraries: Streamlit: (for the web interface). LangChain Groq: (for interacting with the Groq llama). *  
• SQLite3: for database operations.  
• LLAMA: Groq LLM (llama-3.3-70b-versatile)  
• Prompt Engineering: Prompts are designed to accurately gather candidate information and 
generate relevant technical questions.  
The code is divided into 3 files:  
app.py, main.py, and sql.py.  
How to Run: 
Install Libraries: 
pip install streamlit langchain-groq 
Run the App: 
streamlit run app.py  
