import streamlit as st
from openai import OpenAI

# ---- Streamlit page settings ----
st.set_page_config(page_title="🤖 CODE AI AGENT", page_icon="💻")
st.title("🤖 CODE AI AGENT")
st.write("This is a simple coding assistant powered by OpenAI's GPT models.")

# ---- Sidebar for API key ----
api_key = st.sidebar.text_input(
    "🔑 Enter your OpenAI API Key",
    type="password",
    help="You can get your API key from https://platform.openai.com/account/api-keys"
)

# ---- User input ----
prompt = st.text_area(
    "💬 Ask your coding question:",
    placeholder="e.g., Write a Python function to read a CSV file.",
    height=150
)

# ---- Check for key and prompt ----
if st.button("🚀 Generate Code"):
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar.")
    elif not prompt.strip():
        st.warning("⚠️ Please enter a question or instruction.")
    else:
        # Create OpenAI client with user key
        client = OpenAI(api_key=api_key)

        # Make the request
        with st.spinner("Thinking... 🤖"):
            response = client.chat.completions.create(
                model="gpt-4o",  # or "gpt-4-turbo" if you prefer
                messages=[
                    {"role": "system", "content": "You are a helpful AI coding assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
        # Output
        answer = response.choices[0].message.content
        st.subheader("✅ Answer:")
        st.code(answer, language="python")
