# %% Import libraries
%pip install anthropic python-dotenv

# %% Load env
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

# just check if key is loaded
# print("Key loaded:", bool(api_key))
# print("Key prefix:", api_key[:7] if api_key else "NO KEY")

# %% Create API code
from anthropic import Anthropic

client = Anthropic(
    api_key=api_key,
    base_url="https://api.llmsrelay.com"
)

model = "claude-haiku-4-5-20251001"

# %% Make a request
# very very imp functions to maintain chat log basically using API
def add_user_message(messages, text):
    user_message = {"role":"user", "content":text}
    messages.append(user_message)

def add_assistent_message(messages, text):
    assistent_message = {"role":"assistent", "content":text}
    messages.append(assistent_message)

def chat(message):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

# %%
#messages list create
messages=[]

# add in the initial user message
add_user_message(messages, "Define Binary Code in 1 sentence")

# just uncomment this to test
# messages

# pass the list of messages into chat to get an answer
answer = chat(messages)

answer #print

# take the answer and add it to the chat "log"
add_assistent_message(messages, answer)
# just uncomment this to test
# messages

# add users follow up question
add_user_message(messages, "Write another sentence")

# call chat again to get final answer
answer = chat(messages)
answer
    