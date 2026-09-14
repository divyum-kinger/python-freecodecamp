import os
import json
import re
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(
    api_key=api_key,
    base_url="https://api.llmsrelay.com",
)

model = "claude-haiku-4-5-20251001"


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def extract_json(text):
    """Strip markdown code fences if present, then return the JSON substring."""
    text = text.strip()
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
    if match:
        return match.group(1)
    return text


def chat(messages, system=None, stop_sequences=None, output_schema=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    if output_schema:
        params["output_config"] = {"format": output_schema}

    response = client.messages.create(**params)

    for block in response.content:
        if block.type == "text" and block.text:
            return block.text

    raise ValueError(f"No usable text in response: {response}")


def generate_dataset():
    prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to
evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks.
Generate a JSON object with a "tasks" array. Each item must have exactly one field: "task",
a string describing the task.

* Focus on tasks that can be solved by writing a single Python function, a single JSON
  object, or a single regex
* Focus on tasks that do not require writing much code
* Respond with ONLY the JSON object, no markdown fences, no commentary

Please generate 3 objects.
"""

    schema = {
        "type": "json_schema",
        "json_schema": {
            "name": "eval_dataset",
            "schema": {
                "type": "object",
                "properties": {
                    "tasks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {"task": {"type": "string"}},
                            "required": ["task"]
                        }
                    }
                },
                "required": ["tasks"]
            }
        }
    }

    messages = []
    add_user_message(messages, prompt)
    text = chat(messages, output_schema=schema)
    clean = extract_json(text)
    return json.loads(clean)["tasks"]


if __name__ == "__main__":
    dataset = generate_dataset()
    print(dataset)

    with open('dataset.json', 'w') as f:
        json.dump(dataset, f, indent=2)
