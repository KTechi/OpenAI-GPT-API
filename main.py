import openai

openai.api_key = '***************************************************'

while True:
    prompt = input()
    print('prompt', prompt)
    if prompt in ['q', 'Q', 'quit', 'Quit']:
        break
    try:
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {
                    'role': 'user',
                    'content': prompt,
                },
            ],
        )
        result = response.choices[0]['message']['content'].strip()
    except Exception as e:
        print('Exception', e)
        break
    else:
        print('result', result)
