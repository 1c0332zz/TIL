# https://www.acmicpc.net/problem/2897
from pprint import pprint
import sys
sys.stdin = open("2897_몬스터 트럭.txt")

# 행, 열, 주차장 입력받음
R, C = map(int, input().split())
matrix = [list(input().split()) for _ in range(C)]
# pprint(matrix) 
# >>> [['#..#'], 
# >>>  ['..X.'], 
# >>>  ['..X.'], 
# >>>  ['#XX#']]

# 델타 탐색?
for i in matrix:
    for j in i:
        if matrix[i][j] == '.':
            if matrix[i][j+1] =='.':

