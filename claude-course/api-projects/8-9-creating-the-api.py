# # %% Import libraries
# %pip install anthropic python-dotenv

# # %% load env
# from dotenv import load_dotenv

# load_dotenv()

# # %% create API code main
# from anthropic import Anthropic
# client = Anthropic()
# model = "claude-haiku-4-5-20251001"

# # %% Make a request
# message = client.messages.create(
#     model=model,
#     max_tokens=1000,
#     messages=[
#         {
#             "role":"user",
#             "content":"What is Binary Code? Answer in one sentence"
#         }
#     ]
# )

# # %% print message
# message

import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"), base_url="https://api.llmsrelay.com"
)

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "What is Binary Code? Answer in one sentence."}
    ],
)

print(response.content[0].text)
