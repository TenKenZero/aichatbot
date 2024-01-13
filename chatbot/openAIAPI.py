from openai import OpenAI
import os

def ask_openai(message):
    openai_api_key = os.environ["OPENAI_API_KEY"]
    client = OpenAI(api_key=openai_api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo"
    )
    
    return chat_completion.choices[0].message.content