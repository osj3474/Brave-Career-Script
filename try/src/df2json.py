import json
from read_csv import split_recruit

def df2json(df):
    result = df.to_json(orient="index")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    input_csv_file = 'sample.csv'
    content_lst = split_recruit(input_csv_file)
    name_lst = ['timeclose', 'ongoing', 'finished', 'always']
    for i in range(len(content_lst)):
        json_content = df2json(content_lst[i])
        with open(name_lst[i]+'.json', 'w') as f:
            f.writelines(json_content)

