# From the ollama-python readme: https://github.com/ollama/ollama-python
from decouple import config
from ollama import chat
from ollama import ChatResponse

MODEL = config('MODEL')

# Non-streaming response:
# response: ChatResponse = chat(model=MODEL, messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)

stream = chat(
    model=MODEL,
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
