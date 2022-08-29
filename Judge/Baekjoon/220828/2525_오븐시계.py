# https://www.acmicpc.net/problem/2525

A, B = map(int, input().split())
C = int(input())

hour = (B+C) // 60
min = (B+C) % 60

if B + C >= 60:
    A = A + hour
    if A >= 24:
        A -= 24
    print(A, min)
else:
    if A >= 24:
        A -= 24
    print(A, min)