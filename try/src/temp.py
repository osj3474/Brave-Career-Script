import pandas as pd

df = pd.read_csv('sample.csv', encoding="CP949")

# df['마감일']=df['마감일'].map('2021년 {}'.format, na_action = 'ignore')
# df['new']=df['공고명'].map("<a href='' target='_blank'> {} </a>".format, na_action = 'ignore')
df['공고']=df.apply(lambda row : "<a href={} target='_blank'> {} </a>".format(row['링크'], row['공고명']), axis=1)
del df['링크']
del df['공고명']
df = df[['공고', '마감일']]
print(df)
