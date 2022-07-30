# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open("3456_직사각형 길이 찾기_input.txt")
T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())
    D = 0
    if A == B:
        print(f'#{test_case} {C}')
    elif A == C:
        print(f'#{test_case} {B}')
    elif B == C:
        print(f'#{test_case} {A}')