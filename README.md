# OpenAI-GPT-API
A simple template program using GPT-API.

```python
import openai

openai.api_key = '***************************************************'

try:
    prompt = input()
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                'role': 'user',
                'content': prompt,
            },
        ],
    )
except Exception as e:
    print('Exception', e)
else:
    print('response', response)
```
