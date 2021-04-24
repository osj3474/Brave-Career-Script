import requests
from bs4 import BeautifulSoup as bs
import re

def findByUrl(url):
    r = requests.get(url)
    html_doc = r.content
    soup = bs(html_doc, 'html.parser')
    return soup

default_url = "https://www.bucketplace.co.kr"
dev_url = "https://www.bucketplace.co.kr/recruit/?team=dev"
soup = findByUrl(dev_url)

soup = soup.select_one("div.recruit-page__job-list__list__wrap") # /static에 '개발' 과 다른 직무 있어서 이렇게 1차로 거름.
html_lst = soup.find_all("a", {"class":"recruit-page__job-list__list__wrap__item"})
p = re.compile('href\=\"(.+)\/\"\>')    # href="(recruit_url)" 을 얻어내는 것


url_lst = list()   # 채용 포지션 url
for html in html_lst:
    url = re.findall(p, str(html))
    url_lst.append(url[0])

# comany : '오늘의 집'
# potision : div
# period : '수시'
position_lst = list()
recruit_lst = list()
for u in url_lst:
    recruit_url = default_url + u
    recruit_lst.append(recruit_url)
    soup = findByUrl(recruit_url)
    position = soup.find_all("div", {"class":"position-content__head__name"})
    position = position[0].text
    position_lst.append(position)
    print(position)

length = len(position_lst)
with open('../../../test.md', 'r') as f:
    new_file = list()
    while True:
        line = f.readline()
        if not line: break
        if "# 🚌 진행 중인 공고" == line.strip():
            for i in range(length):
                line = line+("""
- __<a href="{}" target='_blank'>{}</a>__

  - 포지션 : {}

  - 기간 : 수시



""".format(recruit_lst[i], position_lst[i], position_lst[i]+" 채용"))
        new_file.append(line)

with open('./now.md', 'w') as doc:
    doc.writelines(new_file)

# Tips) 하위 클래스 잡을때
# html_lst = soup.select("div.recruit-page__job-list__list__wrap > a.recruit-page__job-list__list__wrap__item")