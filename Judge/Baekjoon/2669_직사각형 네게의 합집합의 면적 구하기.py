# https://www.acmicpc.net/problem/2669

import sys
from pprint import pprint
sys.stdin = open("2669_직사각형 네게의 합집합의 면적 구하기.txt")

# 100까지라고 했으니까 100칸을 만들어줌
matrix = [[0]*100 for _ in range(100)]

# 총 4열을 입력받으니 반복문으로 입력받을 수 있게 하고,
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 각 좌표의 길이를 구해주고 반복함으로써 그 사이 공간은 모두 1로 채워짐
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

# 리스트 안에 리스트가 있고 면적은 1로 채워져있으니 카운트를 해줌.
cnt = 0
# 반복문으로 하나씩 전부 보면서 1을 찾으면 +1해줌
for i in matrix:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt)