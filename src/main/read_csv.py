import pandas as pd
from datetime import date
from datetime import datetime as dt
from datetime import timedelta

def str2date(date_str):
    return dt.strptime(str(date_str), "%Y-%m-%d").date()

def split_recruit(input):
    today = date.today()
    df = pd.read_csv(input, encoding="CP949")

    # df['마감일']=df['마감일'].map('2021년 {}'.format, na_action = 'ignore')
    df['마감일']=df['마감일'].map(str2date, na_action = 'ignore')

    df['공고'] = df.apply(lambda row: "<a href='{}' target='_blank'> {} </a>".format(row['링크'], row['공고명']), axis=1)
    del df['링크']
    del df['공고명']
    df = df[['공고', '마감일']]

    # ongoing_lst : 진행중인 공고
    # timeclose_lst : 마감임박 공고
    # finished_lst : 마감된 공고
    # always_lst : 수시채용 공고
    timeclose_lst = df[(df['마감일'] >= today) & (df['마감일'] <= today+timedelta(days= 3))].sort_values(by=['마감일']).reset_index(drop=True)
    ongoing_lst = df.loc[df['마감일'] > today+timedelta(days= 3)].sort_values(by=['마감일']).reset_index(drop=True)
    finished_lst = df.loc[(df['마감일'] < today) & (df['마감일'] > today-timedelta(days= 15))].sort_values(by=['마감일'], ascending=False).reset_index(drop=True)
    finished_lst['공고'] = finished_lst['공고'].map('~~{}~~'.format)
    always_lst = df.loc[df['마감일'].isnull()].reset_index(drop=True)
    always_lst['마감일'] = always_lst['마감일'].fillna("수시(채용시 마감)")


    return timeclose_lst, ongoing_lst, finished_lst, always_lst


if __name__ == "__main__":
    timeclose_lst, ongoing_lst, finished_lst, always_lst = split_recruit('sample.csv')
    # 결과 확인
    print("[마감임박 공고]")
    print(timeclose_lst)

    print("[진행중인 공고]")
    print(ongoing_lst)

    print("[마감된 공고]")
    print(finished_lst)

    print("[수시채용 공고]")
    print(always_lst)

