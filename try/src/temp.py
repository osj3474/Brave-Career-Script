import pandas as pd

df = pd.read_csv('sample.csv', encoding="CP949")

df['마감일'] = df['마감일'].fillna("수시(체용시 마감)")
print(df)
