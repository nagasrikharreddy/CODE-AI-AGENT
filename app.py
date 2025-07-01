import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load .env
load_dotenv()

# Set up OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# === AUTH CONFIG ===
# Username & password from .env
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")

# Streamlit page config
st.set_page_config(page_title="💻 Code AI Agent", page_icon="💻")

# === LOGIN LOGIC ===
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Login Required")

    input_user = st.text_input("Username")
    input_pass = st.text_input("Password", type="password")
    if st.button("Login"):
        if input_user == USERNAME and input_pass == PASSWORD:
            st.session_state.authenticated = True
            st.success("✅ Login successful! You can now use the app.")
        else:
            st.error("❌ Invalid username or password.")
    st.stop()

# === YOUR APP ===
st.title("💻 Code AI Agent")
st.write("Ask me coding questions. Powered by OpenRouter + GPT-4o.")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input
user_input = st.text_area("Your question:", placeholder="E.g. Write hello world in Python")

# Ask
if st.button("Ask"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful coding assistant."},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=512
                )
                answer = response.choices[0].message.content
                st.session_state.history.append({"question": user_input, "answer": answer})
            except Exception as e:
                st.error(f"Error: {e}")

# Show history
st.subheader("Chat History:")
if st.session_state.history:
    for entry in reversed(st.session_state.history):
        st.markdown(f"**👉 You:** {entry['question']}")
        st.code(entry['answer'], language="python")
else:
    st.info("Ask something to start!")

# Download chat
if st.session_state.history:
    chat_log = ""
    for entry in st.session_state.history:
        chat_log += f"👉 You: {entry['question']}\n\n🤖 AI:\n{entry['answer']}\n\n{'-'*40}\n"
    st.download_button("💾 Download Chat History", chat_log, file_name="chat_history.txt")
