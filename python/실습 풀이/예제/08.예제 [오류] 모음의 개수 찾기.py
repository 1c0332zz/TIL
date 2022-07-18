# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)


word = ('HappyHaksick')

count = 0

for char in word:
    if char in 'aeiou':
        count = count + 1

print(count)

# 14일 수업때 말씀하셧던 위의 예제는 a만 출력하게 되므로 수정하였습니다.
# 예제와 같이 하려면 char == 'a', char == 'e' 이런식으로 풀어줘야 합니다!