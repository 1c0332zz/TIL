import re

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# find메소를 사용할 때
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

# 정규식 표현을 사용할 때
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line) :
#         print(line)

# x라는 문자열에서 정수 형태의 데이터를 모두 추출하여 y에 저장
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+',x)
# print(y)
# ['2', '19', '42']

# 'A','E','I','O','U'로 이루어진 패턴을 찾아 출력하는 코드이지만 x 문자열에 해당되는 패턴이 없어서 빈 리스트를 출력
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[AEIOU]+',x)
# print(y)
# [] (빈 리스트 출력)

# 탐욕적 방식의 패턴 찾기
# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)
# ['From: Using the :']

#비탐욕적 방식의 패턴 찾기
# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+?:', x)
# print(y)
# ['From:']

# 원하는 부분만 추출하기
# x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('\S+@\S+',x)
# print(y)
# ['stephen.marquard@uct.ac.za’]


# 이메일 주소 패턴에서 이메일 주소 부분만 추출
# x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('^From (\S+@\S+)',x)
# print(y)
# ['stephen.marquard@uct.ac.za']

# 문자열 메소드를 사용하는 방법
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atpos = data.find('@')
# print(atpos)
# 21
# sppos = data.find(' ',atpos)
# print(sppos)
# 31
# host = data[atpos+1 : sppos]
# print(host)
# uct.ac.za

# split 메소드를 활용하는 방법
# line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# words = line.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])
# 'uct.ac.za'

# 정규식을 사용한 방법
# import re 
# lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#  '^ '는 공백문자가 아닌 문자를 의미하며, '^'가 중간에 들어갈 경우 뒤에 오는 문자를 제외한 패턴을 의미
# y = re.findall('@([^ ]*)',lin)
# print(y)
# ['uct.ac.za']

# 더 정교한 패턴
# import re 
# lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('^From .*@([^ ]*)',lin)
# print(y)
# ['uct.ac.za']