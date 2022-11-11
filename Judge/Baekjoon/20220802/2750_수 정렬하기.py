import sys
sys.stdin = open("2750_수 정렬하기.txt")

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

for i in sorted(arr):
    print(i)