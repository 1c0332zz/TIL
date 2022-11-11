# https://www.acmicpc.net/problem/5576

import sys
sys.stdin = open("5576_콘테스트.txt")

# w대학 0~9까지 점수 받음
score_W = []
for i in range(10):
    W = int(input())
    score_W.append(W)

# k대학 10~19까지 점수 받음
score_K = []
for j in range(10):
    K = int(input())
    score_K.append(K)

# 점수 높은순으로 정렬
score_W.sort(reverse=True)
score_K.sort(reverse=True)

# 점수높은 3개만 가져와서 변수에 더해줌
sum_W = 0
for i in range(0, 3):
    sum_W += score_W[i]

sum_K = 0
for j in range(0, 3):
    sum_K += score_K[j]

# 출력
print(sum_W, sum_K)