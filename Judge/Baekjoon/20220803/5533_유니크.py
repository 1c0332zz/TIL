# https://www.acmicpc.net/problem/5533

import sys
sys.stdin = open("5533_유니크.txt")

# 열이 몇개인지 받아준다.
n = int(input())

# 3게임을 하니까 한게임씩 집어넣을 리스트를 만들어 준다
one = []
two = []
three = []

# 표로 만들어 주는 열을 행으로 바꿔서 만들어 준다.
for i in range(n):
    a, b, c = list(map(int, input().split()))
    one.append(a)
    two.append(b)
    three.append(c)

# 각 열에 카운트가 1개이면 점수에 +를 해주고 출력한다.
for j in range(n):
    score = 0
    if one.count(one[j]) == 1:
        score += one[j]
    if two.count(two[j]) == 1:
        score += two[j]
    if three.count(three[j]) == 1:
        score += three[j]
    print(score)










# matrix = [list(map(int, input().split())) for _ in range(n)]

# # 열마다 반복을 돌려주고
# for i in range(n):
#     reuslt = 0
#     for j in range(3):
#         score = matrix[i][j]
#         if score == matrix[][j]