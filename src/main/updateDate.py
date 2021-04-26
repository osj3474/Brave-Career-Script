import re
from datetime import date
from datetime import datetime as dt

def updateDate(input):
    p = re.compile('\<h2> 최종 업데이트 : \d+월 \d+일 \(\w\) 🔥\<\/h2\>')

    week = ['월', '화', '수', '목', '금', '토', '일']
    today = date.today()
    today = today.strftime('%m월 %d일 ')
    day = '({}) 🔥'.format(str(week[dt.today().weekday()]))
    today = '  <h2> Today : ' + today + day + '</h2>'

    with open(input, 'r') as f:
        new_file = list()
        while True:
            line = f.readline()
            if not line: break
            if re.findall(p, line.strip()):
                new_file.append(today)
                line = '\n'
            new_file.append(line)

    with open(input, 'w') as doc:
        doc.writelines(new_file)




