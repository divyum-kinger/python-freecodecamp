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
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is Binary Code? Answer in one sentence"
        }
    ]
)

# %% Print message
message.content[0].text
