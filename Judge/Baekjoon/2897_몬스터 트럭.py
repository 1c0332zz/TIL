# https://www.acmicpc.net/problem/2897
from pprint import pprint
import sys
sys.stdin = open("2897_몬스터 트럭.txt")










# 행, 열, 주차장 입력받음
# R, C = map(int, input().split())
# parking = [list(input().split()) for _ in range(R)]

# all, one, two, three, four = 0, 0, 0, 0, 0
# for i in range(R - 1):  # 인덱스 벗어나지 않게 설정
#     for j in range(C -1):

#         arr = []
#         for x in range(2):  # 혜빈이의 차 크기
#             for y in range(2):
#                 arr.append(parking[i + x][j + y])

#         if '#' in arr:
#             continue
        
#         if arr.count('.') == 4:
#             all += 1
#         elif arr.count('X') == 4:
#             four += 1
#         elif arr.count('X') == 3:
#             three += 1
#         elif arr.count('X') == 2:
#             two += 1
#         elif arr.count('X') == 1:
#             one += 1

# print(all, one, two, three, four, sep='\n')