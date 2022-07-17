# apple를 거꾸로 출력하시오.

word = ('apple')
result = ''

for char in word:
    result = char + result
print(result)

print(word[::-1])

print(''.join(reversed(word)))

for i in range(len(word)):
    print(word[len(word)-i-1], end='')
