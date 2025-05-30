import os

from openai import AzureOpenAI
from pydantic import BaseModel

client = AzureOpenAI(azure_endpoint="https://gpt-session-models.openai.azure.com/", azure_deployment="gpt-4.1", api_key=os.getenv("OPENAI_API_KEY"), api_version="2025-04-01-preview")

class Person(BaseModel):
    name: str
    age: int
    email: str

response = client.responses.parse(model="gpt-4.1", instructions="You are assistant in a matrix world", input="Create a person", text_format=Person)

print(response.output_text)
print(response.output_parsed)