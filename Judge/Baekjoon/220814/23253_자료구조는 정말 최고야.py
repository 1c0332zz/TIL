# https://www.acmicpc.net/problem/23253
import sys
from sys import stdin

sys.stdin = open('23253_자료구조는 정말 최고야.txt')

# 초기값 입력
N, M = map(int, stdin.readline().split())
# 선언, is_order_possible: 정렬 가능 여부
is_order_possible = True

for _ in range(M):
    stdin.readline()
    # 책 더미 입력
    input_list = list(map(int, stdin.readline().split()))
    # print(sorted(input_list, reverse=True))
    # 책 더미의 정렬 여부 확인
    if input_list != sorted(input_list, reverse=True):
        # 정렬이 일치하지 않을 때
        # 거짓으로 기입 후 break
        is_order_possible = False
        break

# 참이면 Yes
if is_order_possible:
    print('Yes')
else:
    print('No')