import sys
sys.stdin = open("25304_영수증.txt")

# 총 금액과 물건의 개수
x = int(input())
n = int(input())

sum_ab = 0
for i in range(n):
    a, b = map(int, input().split())
    sum_ab += (a * b)

if sum_ab == x:
    print('Yes')
else:
    print('No')