import pandas as pd

df = pd.read_csv("author_data.csv")
new_df = pd.DataFrame()

auth = []
p_id = []

for idx, row in df.iterrows():
    for dat in [pub_id.strip() for pub_id in row['pubmed_id'].split(',')]:
        auth.append(row['author'])
        p_id.append(dat)
new_df['authors'] = auth
new_df['pubmed_id'] = p_id

new_df.to_csv('author_from_paper.csv')