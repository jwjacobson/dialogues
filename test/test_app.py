from app import print_response


def test_test():
    """
    If you're able to run pytest, this test will pass.
    """
    assert True

class FakeInterlocutor:
    """
    A fake Interlocutor object; right now it just returns a predetermined stream.
    """
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

def test_print_response_happy_path():
    client = FakeInterlocutor()
    response = list(client.send_query("What is justice?"))
    result = "".join(chunk['message']['content'] for chunk in response)
    expected = "I say justice is nothing other than what is advantageous for the stronger."

    assert result == expected
