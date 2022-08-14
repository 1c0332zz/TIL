# https://www.acmicpc.net/problem/10798
import sys
sys.stdin = open('10798_세로읽기.txt')

matrix = [[] for _ in range(15)]

for _ in range(5):
    arr_ = input()
    
    for i in range(len(arr_)):
        matrix[i].append(arr_[i])

arr = []

for i in matrix:
    for j in i:
        arr.append(j)
print(*arr, sep='')