# https://www.acmicpc.net/problem/10816
import sys
sys.stdin = open("10816_숫자 카드2.txt")

N = int(input())
cards = list(map(int, input().split()))
nums = {}

# 딕셔너리에 집어넣기
for i in cards:
    if i not in nums:
        nums[i] = 1
    else:
        nums[i] += 1

M = int(input())
card = list(map(int, input().split()))

for j in card:
    if j in nums:
        print(nums[j], end=' ')
    else:
        print(0, end=' ')



















# N = int(input())
# cards = list(map(int, input().split()))
# M = int(input())
# card = list(map(int, input().split()))

# result = [0] * M

# for i in range(len(card)):
#     for j in cards:
#         if j == card[i]:
#             result[i] += 1
# print(*result)