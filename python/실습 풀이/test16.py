# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = 'apple'
b = 0

for a in word:
    if a in ['a', 'e', 'i', 'o', 'u']:
        b = b + 1
print(b)

word = 'Programmuroing'
b=0
for a in word:
    if a in ['a','e','o','u']:
        b=b+1
print('모음의 갯수는 ',b)