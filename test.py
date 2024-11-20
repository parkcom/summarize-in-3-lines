import openai
import os
import json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant designed to output JSON",
        },
        {"role": "user", "content": "2024년 월드시리즈에서는 누가 우승했어?"},
    ],
)

# print(response)
print(response.choices[0].message.content)
# print(response.usage)

