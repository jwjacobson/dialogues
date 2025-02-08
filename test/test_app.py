from dialogues.app import create_interlocutors, print_response
from dialogues.misc import names

def test_test():
    """
    If you're able to run pytest, this test will pass.
    """
    assert True

class FakeInterlocutor:
    """
    A fake Interlocutor object; right now it just returns a predetermined stream.
    """
    def __init__(self, name, model=None):
        self.name = name
        self.model = model

    def send_query(self, query):
        """
        Simulate the streamed response of the real send_query method.
        """
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

def test_create_interlocutors():
    interlocutor_1, interlocutor_2 = create_interlocutors()

    assert interlocutor_1.name in names
    assert interlocutor_2.name in names
    assert interlocutor_1.name != interlocutor_2.name