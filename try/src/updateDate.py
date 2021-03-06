import re
from datetime import date
from datetime import datetime as dt

def updateDate(input):
    p = re.compile('\<h2\> Today : \d+ì \d+ì¼ \(\w\) ð¥\<\/h2\>')

    week = ['ì', 'í', 'ì', 'ëª©', 'ê¸', 'í ', 'ì¼']
    today = date.today()
    today = today.strftime('%mì %dì¼ ')
    day = '({}) ð¥'.format(str(week[dt.today().weekday()]))
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




