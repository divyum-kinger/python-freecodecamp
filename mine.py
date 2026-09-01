from anthropic import Anthropic
from anthropic.types import TextBlock
from dotenv import load_dotenv
g
load_dotenv()

client = Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence",
        }
    ],
)

for block in message.content:
    if isinstance(block, TextBlock):
        print(block.text)
