from openai import OpenAI


MY_API_KEY = "enter API key here"

user_prompt = "What day is today?"

client = OpenAI(
    api_key=MY_API_KEY,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Be precise, don't respond or output more than 10 words.",
        },
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
    model="gpt-3.5-turbo",
    temperature=0
)

chat_completion.choices[0].message.content.strip()
