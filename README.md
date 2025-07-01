# 🤖 CODE AI AGENT

A simple AI-powered code agent that uses OpenAI to help you generate and run Python code from your browser, secured with a login.

---

## 🚀 Features

- ✅ Secure login (basic password authentication)
- ✅ Ask coding questions
- ✅ Get Python code answers
- ✅ Run the agent in your browser with Streamlit
- ✅ Deployable on Streamlit Cloud

---

## 📂 Project Structure

code_ai_agent/
│ app.py
│ main.py
│ code_ai_agent.py
│ requirements.txt
│ index.html
│ README.md
└── venv/ (ignored by .gitignore)

---

## 🔑 Setup

1. **Clone this repo:**
   ```bash
   git clone https://github.com/nagasrikharreddy/CODE-AI-AGENT.git
   cd CODE-AI-AGENT
Create virtual environment (optional but recommended):

python -m venv venv
Activate virtual environment:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Run locally:

streamlit run app.py
Login credentials:
The login is simple for now — update app.py to set your own USERNAME and PASSWORD.

☁️ Deploy on Streamlit Cloud
Push your code to GitHub ✅

Go to https://streamlit.io/cloud

Click 'New app'

Connect your repo: nagasrikharreddy/CODE-AI-AGENT

Select app.py as the main file

Click 'Deploy'

Done! 🎉

🗝️ Environment Variables
Store your OpenAI API Key safely:

Locally:

export OPENAI_API_KEY="YOUR_API_KEY"
Or add it to .env and load with python-dotenv.

On Streamlit Cloud:

Go to App Settings → Secrets

Add:

ini

OPENAI_API_KEY = "YOUR_API_KEY"
🧩 License
This project is for learning and personal use only.

Made with ❤️ by Naga Srikhar Reddy

---

## ✅ How to use

- Save this as `README.md` in your project folder.
- Commit and push:
  ```bash
  git add README.md
  git commit -m "Add README.md"
  git push
