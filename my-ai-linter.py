import os
from anthropic import Anthropic
import sys

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

api_definition = sys.argv[1]
ruleset = sys.argv[2]

with open(api_definition, 'r') as file:
    api_contents = file.read()

with open(ruleset, 'r') as file:
    ruleset_contents = file.read()

prompt = f"""Here is an OpenAPI document: <document>{api_contents}</document>

Lint the OpenAPI document based on the following rules:
{ruleset_contents}
"""

# print(prompt)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="claude-3-opus-20240229",
)

print(message.content)