import json
from datetime import datetime as dt
import pandas as pd
from datetime import date
from datetime import timedelta

def str2date(date_str):
    return dt.strptime(str(date_str), "%Y-%m-%d").date()

# def date2str(date):
#     return dt.strptime(date, "%Y-%m-%d")

def split_recruit(input):
    today = date.today()
    df = pd.read_csv(input, encoding="CP949")
    df['마감일']=df['마감일'].map(str2date, na_action = 'ignore')

    timeclose_lst = df[(df['마감일'] >= today) & (df['마감일'] <= today+timedelta(days= 3))].sort_values(by=['마감일']).reset_index(drop=True)
    ongoing_lst = df.loc[df['마감일'] > today+timedelta(days= 3)].sort_values(by=['마감일']).reset_index(drop=True)
    finished_lst = df.loc[(df['마감일'] < today) & (df['마감일'] < today-timedelta(days= 3))].sort_values(by=['마감일'], ascending=False).reset_index(drop=True)
    always_lst = df.loc[df['마감일'].isnull()].reset_index(drop=True)
    always_lst['마감일'] = always_lst['마감일'].fillna("수시(채용시 마감)")

    return timeclose_lst, ongoing_lst, finished_lst, always_lst

def df2json(df):
    result = df.to_json(orient="index")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    input_csv_file = 'sample.csv'
    content_lst = split_recruit(input_csv_file)
    
    # print(content_lst[0]['마감일'].map(date2str))
    # exit(0)

    name_lst = ['timeclose', 'ongoing', 'finished', 'always']
    for i in range(len(content_lst)):
        json_content = df2json(content_lst[i])
        with open('./json/'+name_lst[i]+'.json', 'w') as f:
            f.writelines(json_content)

