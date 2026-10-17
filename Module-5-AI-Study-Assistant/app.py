import os
import streamlit as st
from google import genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure page
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Study Assistant")
st.write("Learn faster with the help of Generative AI.")

# Check API key
if not api_key:
    st.error("Gemini API key not found. Please configure the .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

# User inputs
topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Object-Oriented Programming"
)

option = st.selectbox(
    "Choose what you want AI to generate:",
    [
        "Simple Explanation",
        "Short Notes",
        "Quiz Questions",
        "Study Plan"
    ]
)

generate_button = st.button("Generate")


if generate_button:

    if not topic.strip():
        st.warning("Please enter a topic first.")

    else:

        if option == "Simple Explanation":

            prompt = f"""
            Explain {topic} in simple language for a beginner.
            Use an easy example.
            Keep the explanation clear and concise.
            """

        elif option == "Short Notes":

            prompt = f"""
            Create short study notes about {topic}.
            Use headings and bullet points.
            Focus on the most important concepts.
            """

        elif option == "Quiz Questions":

            prompt = f"""
            Create 5 beginner-friendly multiple-choice questions
            about {topic}.

            Provide:
            1. Question
            2. Four options
            3. Correct answer
            4. Short explanation
            """

        else:

            prompt = f"""
            Create a 7-day beginner study plan for learning {topic}.

            For each day include:
            - Topic to study
            - What to practice
            - One small task
            """

        with st.spinner("AI is generating your response..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash", 
                    contents=prompt
            )

                st.subheader("AI Response")
                st.write(response.text)

            except Exception as e:

                st.error("Something went wrong while contacting the AI model.")
                st.write(str(e))