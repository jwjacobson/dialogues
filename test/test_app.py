import pytest

from httpx import ConnectError

from dialogues.app import create_interlocutors, print_response
from dialogues.misc import names

def test_pytest_setup():
    """
    If you're able to run pytest, this test will pass.
    """
    assert True

class FakeInterlocutor:
    """
    A fake Interlocutor object; right now it just returns a predetermined stream.
    """
    def __init__(self, name, model=None, raise_error=None):
        self.name = name
        self.model = model
        self.raise_error = raise_error

    def send_query(self, query):
        """
        Simulate the streamed response of the real send_query method.
        """
        if self.raise_error == "ConnectError":
            raise ConnectError("Simulated connection error.")
        elif self.raise_error == "OtherError":
            raise Exception("Simulated unexpected error.")

        response_stream = [
            {"message": {"content": "I say "}},
            {"message": {"content": "justice is "}},
            {"message": {"content": "nothing other than "}},
            {"message": {"content": "what is advantageous "}},
            {"message": {"content": "for the stronger."}}
        ]
        
        for chunk in response_stream:
            yield chunk

def test_send_query():
    client = FakeInterlocutor(name="Thrasymachus")
    response = list(client.send_query("What is justice?"))
    result = "".join(chunk['message']['content'] for chunk in response)
    expected = "I say justice is nothing other than what is advantageous for the stronger."

    assert result == expected

def test_print_response_happy(capsys):
    client = FakeInterlocutor(name="Thrasymachus")
    query = "What is justice?"

    print_response(client, query)
    output = capsys.readouterr().out.rstrip()
    expected = "I say justice is nothing other than what is advantageous for the stronger."
    
    assert output == expected

def test_print_response_connect_error(capsys):
    client = FakeInterlocutor(name="Thrasymachus", raise_error="ConnectError")
    
    with pytest.raises(SystemExit) as e:
        print_response(client, "What is justice?")
    
    output = capsys.readouterr().out.rstrip()
    expected = 'Could not contact the server. Are you sure ollama is running? (Type in a terminal ollama serve to start ollama)'

    assert output == expected
    assert e.value.code == 1

def test_create_interlocutors():
    interlocutor_1, interlocutor_2 = create_interlocutors()

    assert interlocutor_1.name in names
    assert interlocutor_2.name in names
    assert interlocutor_1.name != interlocutor_2.name