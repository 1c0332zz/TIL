# https://www.acmicpc.net/problem/17249

arr = input()
cnt_ = 0
for i in arr:
    if i == '@':
        cnt_ += 1
    elif i == '(':
        break

cnt__ = 0
arr_ = arr[::-1]
for j in arr_:
    if j == '@':
        cnt__ += 1
    elif j == ')':
        break

print(cnt_, cnt__)