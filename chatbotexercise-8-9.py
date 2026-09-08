import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

from anthropic import Anthropic

client = Anthropic(
    api_key=api_key,
    base_url="https://api.llmsrelay.com",
)

model = "claude-haiku-4-5-20251001"

def add_user_message(messages, text):
    user_message = {"role":"user", "content":text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role":"assistant", "content":text}
    messages.append(assistant_message)

def chat(message):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

messages = []

while True:
    user_input = input("> ")

    add_user_message(messages, user_input)
    answer = chat(messages)
    add_assistant_message(messages, answer)
    print(answer)
