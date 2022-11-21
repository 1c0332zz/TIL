# 문자열 메소드를 사용하는 방법
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
21
sppos = data.find(' ',atpos)
print(sppos)
31
host = data[atpos+1 : sppos]
print(host)
# uct.ac.za

# split 메소드를 활용하는 방법
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
# 'uct.ac.za'