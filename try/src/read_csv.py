import pandas as pd
from datetime import date
from datetime import datetime as dt
import numpy as np

def str2date(date_str):
    return dt.strptime(str(date_str), "%Y년 %m월 %d일").date()

if __name__ == "__main__":
    today = date.today()
    df = pd.read_csv('sample.csv', encoding="CP949")
    df['마감일']=df['마감일'].map('2021년 {}'.format, na_action = 'ignore')
    df['마감일']=df['마감일'].map(str2date, na_action = 'ignore')

    # ongoing_lst : 진행중인 공고
    # finished_lst : 마감된 공고
    # always_lst : 수시채용 공고
    ongoing_lst = df.loc[df['마감일'] < today]
    finished_lst = df.loc[df['마감일'] > today]
    always_lst = df.loc[df['마감일'].isnull()]
    print("진행중인 공고")
    print(ongoing_lst)

    print("마감된 공고")
    print(finished_lst)

    print("수시채용 공고")
    print(always_lst)
