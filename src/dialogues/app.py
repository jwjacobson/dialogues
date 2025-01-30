# From the ollama-python readme: https://github.com/ollama/ollama-python
from decouple import config
from ollama import chat
from ollama import ChatResponse

MODEL = config('MODEL')
DEFAULT_QUERY = config('DEFAULT_QUERY')

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

class Interlocutor:
    def __init__(self, model):
        self.model = model

    def send_query(self, query):
        try:
            stream = chat(
                model=MODEL,
                messages=[{'role': 'user', 'content': 'What is justice?'}],
                stream=True,
            )
        except Exception:
            raise

        return stream


client = Interlocutor(model=MODEL)


def print_response(chat_client, query):
    stream = chat_client.send_query(query)
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)


if __name__ == "__main__":
    print_response(client, DEFAULT_QUERY)