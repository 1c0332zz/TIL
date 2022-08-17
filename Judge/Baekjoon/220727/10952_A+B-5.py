# https://www.acmicpc.net/problem/10952
import sys

sys.stdin = open("10952_A+B-5.txt")

while 1:
    A, B = map(int, input().split())
    if A + B == 0:
        break
    else:
        result = A + B
    print(result)