# https://www.acmicpc.net/problem/1110
n = int(input())
num = n
cnt = 0

# while 1:
#     if len(num) == 1:
#         num = '0' + num
#     sum_ = str((int(num[0])) + (int(num[1])))
#     num = num[-1] + sum_[-1]
#     cnt += 1
#     if num == n:
#         print(cnt)
#         break

while 1:
    a = num // 10   # 2
    b = num % 10    # 6
    c = (a+b) % 10  # 8
    num = (b * 10) + c

    cnt += 1
    if(num == n):
        break

print(cnt)