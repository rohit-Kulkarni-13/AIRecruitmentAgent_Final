
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("prompts/extractor_prompt.txt", "r", encoding="utf-8") as f:
    extractor_prompt = f.read()

def extract_requirements(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": extractor_prompt},
            {"role": "user", "content": text}
        ]
    )
    content = response.choices[0].message.content.strip()
    try:
        return eval(content) if content.startswith("{") else {"raw": content}
    except:
        return {"raw": content}
