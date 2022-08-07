# https://www.acmicpc.net/problem/10818
n = int(input())

max_ = -10e9
min_ = 10e9
arr = map(int, input().split())

for i in arr:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i

print(min_, max_)