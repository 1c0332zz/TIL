# https://www.acmicpc.net/problem/2751
import sys
N = int(input())

arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for j in arr:
    print(j)