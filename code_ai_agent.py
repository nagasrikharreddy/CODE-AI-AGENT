import os
from openai import OpenAI

# OpenRouter base URL
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def code_ai_agent():
    print("=== OpenRouter Code AI Agent ===")
    print("Ask coding questions or get code examples.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = client.chat.completions.create(
                model="openai/gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful coding assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=512   # ✅ fits free quota!
            )
            print("\nAI:\n", response.choices[0].message.content, "\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    code_ai_agent()
