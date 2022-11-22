import re 

# 원하는 부분만 추출하기
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y)
# ['stephen.marquard@uct.ac.za’]


# 이메일 주소 패턴에서 이메일 주소 부분만 추출
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)',x)
print(y)
# ['stephen.marquard@uct.ac.za']


# 더 정교한 패턴
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)
# ['uct.ac.za']