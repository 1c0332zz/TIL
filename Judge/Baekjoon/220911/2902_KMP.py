# https://www.acmicpc.net/problem/2902
import sys
sys.stdin = open("2902_KMP.txt")

arr = input()
result = [arr[0]]
for i in range(len(arr)):
    if arr[i] == "-":
        result.append(arr[i+1])

print(*result, sep="")