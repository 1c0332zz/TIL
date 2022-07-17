# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수를 바로 쓰기보다는 반복문을 활용하세요.
# 6
# word = 'happy!'

word = 'happy!'
count = 0

# 모든 문자를 돌면서
for char in word:
# 1씩 증가시킨다.
    count = count +1
print(count)