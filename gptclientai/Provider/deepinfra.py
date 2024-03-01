import json
from requests import post

class DeepInfra:
    url = "https://deepinfra.com"
    api = "https://api.deepinfra.com"

    @classmethod
    def create_response(cls, messages: list):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/event-stream",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": f"{cls.url}/chat",
            "Content-Type": "application/json",
            "Flag-Real-Time-Data": "false",
            "Origin": cls.url,
            "Alt-Used": "koala.sh",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

        data = {
            "model": "meta-llama/Llama-2-70b-chat-hf",
            "messages": messages,
            "stream": True
        }

        res = post(
            url = f"{cls.api}/v1/openai/chat/completions",
            json = data,
            headers = headers
        )

        res.raise_for_status()
        first = True
        for chunk in res.iter_lines():
            if not chunk.startswith(b"data: "):
                continue
            try:
                json_line = json.loads(chunk[6:])
                choices = json_line.get("choices", [{}])

                if choices[0].get("finish_reason"):
                    break
                token = choices[0].get("delta", {}).get("content")
                if token:
                    if first:
                        token = token.lstrip()
                    if token:
                        first = False
                        yield token
            except:
                pass