word = 'banana'
# print(word)
result = {}

# 문자열을 반복하면서 알파벳 하나씩이 char
for char in word: 
    # 만약에 기존에 키가 없으면, 1으로 초기화를 하고
    if char not in result:
        result[char] = 1
    # 키가 있으면, 기존 값에 더하자!
    else:
        result[char] = result[char] + 1

print(result)
# # 키-값의 쌍 추가
# result['a'] = 0
# print(result)

