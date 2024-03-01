import json
import random
import string
import requests

def get_random_string(length):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

class Koala:
    url = "https://koala.sh"
    session = requests.Session()

    @classmethod
    def create_response(cls, messages: list):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/event-stream",
            "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": f"{cls.url}/chat",
            "Content-Type": "application/json",
            "Flag-Real-Time-Data": "false",
            "Visitor-ID": get_random_string(20),
            "Origin": cls.url,
            "Alt-Used": "koala.sh",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "TE": "trailers",
        }

        data = {
            "input": messages[-1]["content"],
            "inputHistory": [
                message["content"]
                for message in messages
                if message["role"] == "user"
            ],
            "outputHistory": [
                message["content"]
                for message in messages
                if message["role"] == "assistant"
            ],
            "model": "gpt-3.5-turbo",
        }

        response = cls.session.post(f"{cls.url}/api/gpt/", json=data, headers=headers)
        response.raise_for_status()

        for chunk in response.iter_lines():
            if not chunk.startswith(b"data: "):
                continue
            try:
                json_line = json.loads(chunk[6:])
                yield json_line
            except:
                pass