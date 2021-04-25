from markdown import update_md_file
from read_csv import split_recruit
from tabulate import tabulate

input_md_file = '../../README.md'
input_csv_file = 'sample.csv'
keyword_lst = ['# ‼️ 마감 임박 공고', '# 🚌 진행 중인 공고', '# 💫 마감된 공고', '# 📡 수시 채용 공고']
content_lst = split_recruit(input_csv_file)

length = len(content_lst)
for i in range(length):
    content_cleaned = tabulate(content_lst[i], tablefmt="pipe", headers="keys")
    update_md_file(input_md_file, keyword_lst[i], content_cleaned)