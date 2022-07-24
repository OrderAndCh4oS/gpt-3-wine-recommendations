import csv
import os

import openai
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')


def get_embedding(text, model="text-similarity-curie-001"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']


def main():
    with open("wine_tasting_notes_tagged.csv") as f:
        wine_list = f.readlines()
    wine_list = [x.strip() for x in wine_list]

    df = pd.DataFrame(wine_list)
    df['curie_similarity'] = df[0].apply(lambda x: get_embedding(x, model='text-similarity-curie-001'))
    df['curie_search'] = df[0].apply(lambda x: get_embedding(x, model='text-search-curie-doc-001'))
    df.to_csv('wine_tasting_notes_embeddings__curie_combined.csv', index=False)


if __name__ == '__main__':
    main()
