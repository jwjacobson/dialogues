# Adapted from the sample code in the ollama-python readme: https://github.com/ollama/ollama-python
from random import sample

from decouple import config
from httpx import ConnectError
from ollama import chat
from ollama import ChatResponse
import sys

from .misc import names


MODEL = config('MODEL')
DEFAULT_QUERY = config('DEFAULT_QUERY')

class Interlocutor:
    """
    A partner in a dialogue.
    """
    def __init__(self, name, model=MODEL):
        self.name = name
        self.model = model

    def __repr__(self):
        return f"Interlocutor {self.name}"

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


def create_interlocutors():
    first_name, second_name = sample(names, 2)
    
    interlocutor_1 = Interlocutor(name=first_name)
    interlocutor_2 = Interlocutor(name=second_name)

    return interlocutor_1, interlocutor_2

interlocutor_1, interlocutor_2 = create_interlocutors()

def print_response(chat_client, query):
    try:
        stream = chat_client.send_query(query)
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
    except ConnectError:
        print("Could not contact the server. Are you sure ollama is running? (Type in a terminal ollama serve to start ollama)")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    

def main():
    client = Interlocutor(name="Logos", model=MODEL)
    print_response(client, DEFAULT_QUERY)


if __name__ == "__main__":
    main()