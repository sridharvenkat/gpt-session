import os
from openai import AzureOpenAI

client = AzureOpenAI(azure_endpoint="https://gpt-session-models.openai.azure.com/", azure_deployment="gpt-4.1", api_key=os.getenv("OPENAI_API_KEY"), api_version="2025-04-01-preview")

chat_response = client.chat.completions.create(
    model="gpt-4.1",    
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

response = client.responses.create(
    model="gpt-4.1",
    instructions="You are a pirate, and you must respond in pirate speak.",
    input="Write a one-sentence bedtime story about a unicorn."    
)

print(chat_response.choices[0].message.content.strip())
print(response.output_text.strip())