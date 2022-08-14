# https://www.acmicpc.net/problem/10816
###### 정답XXXXXXX

import sys
sys.stdin = open("10816_숫자 카드2.txt")
# N = 10
# cards = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# # 찾는카드 몇개, 뭘 찾아야하는지
# M = 8
# card = [10, 9, -5, 2, 3, 4, 5, -10]

# 카드 몇개, 적혀있는 카드
N = int(input())
cards = list(map(int, input().split()))
# 찾는카드 몇개, 뭘 찾아야하는지
M = int(input())
card = list(map(int, input().split()))

# 해당 자리에 +1해줄 리스트
result = [0] * M

for i in range(len(card)):
    for j in cards:
        if j == card[i]:
            result[i] += 1
print(*result)