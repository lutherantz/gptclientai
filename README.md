# `gptclientai` Module

## Overview

The `gptclientai` module provides convenient utility functions for working with chat-based and completion-based responses using various providers. This module includes two main classes: `Chat` for handling chat conversations and `Completion` for generating completions.

#

## Installation

You can install the `gptclientai` module using `pip`:

```bash
pip install gptclientai
```

#

## Usage

1. 'Chat' Class

create_chat_response(provider, messages, stream=False)

Returns a string or an iteration for the chat completion.

### - Parameters

- 'provider': The provider to use (e.g., freegpt.Provider.FreeChatGpt).
- 'messages': Messages of the conversation in a list (e.g., '[{"role": "user", "content": "hello"}]')
- 'stream'  : If "True", returns an iteration; otherwise, returns a string.

### - Example

```python
import gptclientai

if __name__ == "__main__":
    res = gptclientai.Chat.create_chat_response(
        provider = gptclientai.Provider.DeepInfra,
        messages = [
            {
                "role": "user",
                "content": "hello"
            }
        ],
        stream = True
    )

    for chunk in res:
        print(chunk)

# -------------------------
import gptclientai

if __name__ == "__main__":
    res = gptclientai.Chat.create_chat_response(
        provider = gptclientai.Provider.DeepInfra,
        messages = [
            {
                "role": "user",
                "content": "hello"
            }
        ],
        stream = False
    )

    print(res)
```

2. 'Completion' Class

create_completion(provider, prompt, stream=False)

Returns a string or an iteration for the completion.

### - Parameters

- 'provider': The provider to use (e.g., freegpt.Provider.FreeChatGpt).
- 'prompt': Messages for the response (e.g., '"Hello!"')
- 'stream'  : If "True", returns an iteration; otherwise, returns a string.

### - Example

```python
import gptclientai

if __name__ == "__main__":
    res = gptclientai.Completion.create_create_completion(
        provider = gptclientai.Provider.DeepInfra,
        messages = "Hello",
        stream = True
    )

    for chunk in res:
        print(chunk)

# -------------------------
import gptclientai

if __name__ == "__main__":
    res = gptclientai.Completion.create_create_completion(
        provider = gptclientai.Provider.DeepInfra,
        prompt = "Hello",
        stream = False
    )

    print(res)
```

#

## License

This module is licensed under the MIT License - see the LICENSE file for details.

```md
MIT License

Copyright (c) 2024 0xseka/sekateur/seka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```