# 탐욕적 방식의 패턴 찾기
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
['From: Using the :']

#비탐욕적 방식의 패턴 찾기
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
['From:']