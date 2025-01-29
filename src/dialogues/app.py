# From the ollama-python readme: https://github.com/ollama/ollama-python

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1:latest', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)