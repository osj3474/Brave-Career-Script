# pip3 install pandas
# pip3 install requests
# pip3 install bs4

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

data = pd.read_csv('/Users/sangjin/Desktop/notice.csv')
data = data.loc[data['Message'].str.contains('http')]
data_lst = data['Message'].tolist()
print(data_lst[0])
result = requests.get(data_lst[0])
print(result.text)
soup = bs(result.text, 'html.parser')
print(soup.find_all("strong", {"class": "tit_jobs"}))
