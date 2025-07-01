import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

# Set up FastAPI
app = FastAPI()

# OpenRouter config
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Request schema
class Query(BaseModel):
    prompt: str

@app.post("/ask")
def ask_code_agent(query: Query):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": query.prompt}
            ],
            max_tokens=512  # fits free quota
        )
        answer = response.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
