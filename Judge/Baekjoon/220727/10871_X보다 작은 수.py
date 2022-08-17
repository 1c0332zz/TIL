# https://www.acmicpc.net/problem/10871
import sys

sys.stdin = open("10871_X보다 작은 수.txt")

N, X = map(int, input().split())
Y = list(map(int, input().split()))

for i in Y:
    if X > i:
        print(i, end=' ')
    else:
        continue
