# Adapted from the sample code in the ollama-python readme: https://github.com/ollama/ollama-python
from decouple import config
from httpx import ConnectError
from ollama import chat
from ollama import ChatResponse
import sys

MODEL = config('MODEL')
DEFAULT_QUERY = config('DEFAULT_QUERY')

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
        except ConnectError as e:
            print(f"ConnectError: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)

        return stream


client = Interlocutor(model=MODEL)


def print_response(chat_client, query):
    try:
        stream = chat_client.send_query(query)
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
    except ConnectError:
        print("Could not contact the server. Are you sure ollama is running?")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    

if __name__ == "__main__":
    print_response(client, DEFAULT_QUERY)