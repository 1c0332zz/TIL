# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open("신용카드 만들기1_input.txt")

T = int(input())

for test_case in range(1, T+1):
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O  = map(int, input().split())
    i = (A*2)+(C*2)+(E*2)+(G*2)+(I*2)+(K*2)+(M*2)+(O*2)
    j = B + D + F + H + J + L + N
    k = i + j                       # 주어진 예제를 전부 다 대입시킨다..
    for number in range(10):        # 0~9까지 반복문을 돌려준다.
        if (k+number) % 10 == 0:    # k와 number를 더한것이 10으로 나눳을때 나머지가 0이면
            break                   # 브레이크 후 출력
        else:                       # 그게 아니면 건너뛴다..
            continue
    print(f'#{test_case} {number}')