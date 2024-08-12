from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

# Access the environment variables
openai_api_key = os.getenv("mushir_key")

user_prompt = "Is investing in farming the best way to boost economy?"

client = OpenAI(
    api_key=openai_api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Be precise and complete, don't respond or output more than 30 words.",
        },
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
    model="gpt-4o-mini",
    temperature=0
)

chat_completion.choices[0].message.content.strip()
