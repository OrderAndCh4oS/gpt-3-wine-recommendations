import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')

def main():
    engines = openai.Engine.list()
    for engine in engines.list:
        print(engine.id)

    completion = openai.Completion.create(
        engine="babbage",
        prompt="How did you die:",
        temperature=0.3,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,

    )

    print(completion.choices[0].text)


if __name__ == '__main__':
    main()
