# https://www.acmicpc.net/problem/9455

import sys
from pprint import pprint
sys.stdin = open("9455_박스.txt")

# 테스트 케이스 받아주고
for tc in range(int(input())):
    # m과 n을 받아줌. 행, 열로 주어짐
    m, n = map(int, input().split())
    # 예제와 반대로 열의 개수로 행을 만들어 줄꺼니까 n만큼 빈 리스트 생성
    matrix = [[] for _ in range(n)]
    # print(matrix)
    
    # 상자 열의 개수만큼 받아야함. 열과 행을 바꿔 입력할꺼니 기존 행 입력
    for i in range(m):
        # a에 상자 목록 넣어주고
        a = list(input().split())
        # 각 행의 인덱스에 쌓아줌
        for j in range(n):
            matrix[j].append(a[j])
# pprint(matrix) 아래와 같은 모양 완성
# [['1', '0', '1', '0', '1'],
#  ['0', '0', '0', '1', '0'],
#  ['0', '1', '0', '0', '1'],
#  ['0', '0', '1', '0', '0']]
# 여기서 오른쪽으로 이동하면서 이동거리를 새어주면 됨

    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][m] == 1:
                
