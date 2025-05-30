import os
import json
from openai import AzureOpenAI
from openai.types.responses import ResponseFunctionToolCall
from datetime import datetime
from zoneinfo import ZoneInfo


client = AzureOpenAI(azure_endpoint="https://gpt-session-models.openai.azure.com/", azure_deployment="gpt-4.1", api_key=os.getenv("OPENAI_API_KEY"), api_version="2025-04-01-preview")


def get_datetime():
    """Returns the current date and time in ISO 8601 format."""    
    return datetime.now().isoformat()

response = client.responses.create(
    model="gpt-4.1",  
    tools=[{
        "type": "function",        
        "name": "get_datetime",
        "description": "Returns the current date and time in ISO 8601 format.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        },
        "strict": True        
    }],
    instructions="You are a helpful assistant.",
    input="What is today's date and time?",
)
response_id = response.id
response_function_calls:list[ResponseFunctionToolCall] = response.output

result = get_datetime()
result_dump = {
    "type": "function_call_output",
    "call_id": response_function_calls[0].call_id,
    "output": json.dumps({ "datetime" : result})
}
new_response = client.responses.create(previous_response_id=response_id,
                        input=[result_dump],model="gpt-4.1")

print(new_response.output)




