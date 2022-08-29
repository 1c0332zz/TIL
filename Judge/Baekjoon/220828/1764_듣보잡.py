# https://www.acmicpc.net/problem/1764
import sys

sys.stdin = open("1764_듣보잡.txt")
n, m = map(int, input().split())
arr = {}
for _ in range(n):
    d = input()
    if d not in arr:
        arr[d] = 1
    else:
        arr[d] += 1

for _ in range(m):
    b = input()
    if b not in arr:
        arr[b] = 1
    else:
        arr[b] += 1
# arr안에 듣보잡은 값이 2로 표시
# print(arr)

list_ = []

for k, v in arr.items():
    if v == 2:
        list_.append(k)
print(len(list_))

for i in sorted(list_):
    print(i)