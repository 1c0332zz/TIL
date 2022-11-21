import re
# 정규식 표현을 사용할 때
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)

# x라는 문자열에서 정수 형태의 데이터를 모두 추출하여 y에 저장
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
# ['2', '19', '42']

# 'A','E','I','O','U'로 이루어진 패턴을 찾아 출력하는 코드이지만 x 문자열에 해당되는 패턴이 없어서 빈 리스트를 출력
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[AEIOU]+',x)
print(y)
# [] (빈 리스트 출력)

# 정규식을 사용한 방법
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#  '^ '는 공백문자가 아닌 문자를 의미하며, '^'가 중간에 들어갈 경우 뒤에 오는 문자를 제외한 패턴을 의미
y = re.findall('@([^ ]*)',lin)
print(y)
# ['uct.ac.za']