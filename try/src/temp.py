from read_csv import split_recruit
from tabulate import tabulate

input_md_file = 'test.md'
input_csv_file = 'sample.csv'
content_lst = split_recruit(input_csv_file)
ongoing = content_lst[0]
ongoing = ongoing.sort_values(by=['마감일'])
content = tabulate(ongoing, tablefmt="pipe", headers="keys")

print(content)