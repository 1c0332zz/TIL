# 14. 문자의 갯수 구하기
# 'apple' , a 카운트
word = 'applea'
# char는 이름 붙이기
# word의 요소를 하나씩 char 바인딩
count = 0
for char in word:
    if char == 'a':
        # a일때마다 +1
        count += 1
print(count)