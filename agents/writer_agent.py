
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("prompts/writer_prompt.txt", "r", encoding="utf-8") as f:
    writer_prompt = f.read()

def generate_proposal(data):
    prompt = writer_prompt + "\n\nExtracted Info:\n" + str(data)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that drafts proposals."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
