import pandas

df = pandas.read_csv('./kaggle-wine-reviews/winemag-data-130k-v2.csv')

df = df.sample(frac=0.001)
df = df[['description']]
df['prompt'] = ''
df = df[['prompt', 'description']]

df.to_csv('wine-mag-reviews.csv', index=False)
