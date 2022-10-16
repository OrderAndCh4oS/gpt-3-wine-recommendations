import os
from pprint import pprint

import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('OPEN_AI_API_KEY')

def main():
    fine_tunes = requests.get('https://api.openai.com/v1/fine-tunes', headers={'Authorization': f'Bearer {api_key}'})

    pprint(fine_tunes.json())


if __name__ == '__main__':
    main()
