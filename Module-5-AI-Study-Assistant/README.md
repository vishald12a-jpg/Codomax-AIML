# 📚 AI Study Assistant

An AI-powered study assistant built using Python, Streamlit, and Google Gemini API.

## 📌 Project Overview

The AI Study Assistant helps students learn technical topics using Generative AI.

Users can enter a topic and choose what they want the AI to generate.

## ✨ Features

- Simple topic explanations
- Short study notes
- Multiple-choice quiz questions
- 7-day study plans
- Beginner-friendly web interface
- Generative AI integration using Gemini API

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- python-dotenv

## 🔄 Application Workflow

```text
User enters topic
        ↓
Selects AI feature
        ↓
Python application creates prompt
        ↓
Gemini API
        ↓
AI generates response
        ↓
Response displayed in Streamlit
```

## 📂 Project Structure

```text
Module-5-AI-Study-Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

> The `.env` file contains the API key and must not be uploaded to GitHub.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR-GITHUB-REPOSITORY-URL
```

### 2. Open the project

```bash
cd Module-5-AI-Study-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the API key

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 7. Run the application

```bash
streamlit run app.py
```

## 🎯 Learning Outcomes

Through this project, I learned:

- How Generative AI applications work
- How to use an AI API
- How to create effective prompts
- How to use Python with an AI service
- How to protect API keys using environment variables
- How to build a simple Streamlit application
- How AI can support learning and productivity

## 🚀 Future Improvements

Possible future improvements include:

- Conversation history
- Subject-wise study resources
- Difficulty selection for quizzes
- Automatic quiz scoring
- Downloadable study notes
- User authentication
- Database integration

## 👨‍💻 Author

Vishal D  
