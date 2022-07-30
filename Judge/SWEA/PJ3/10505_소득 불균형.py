# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJCO4t6cCMDFASv&contestProbId=AXNP4CvauaMDFAXS&probBoxId=AYJCO4t6cCQDFASv&type=PROBLEM&problemBoxTitle=1%EC%A3%BC%EC%B0%A8&problemBoxCnt=7

import sys
sys.stdin = open("10505_소득 불균형_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    result = 0
    # print(result//N, N)
    for i in income:                # 값을 하나씩 비교함.
        if i <= sum(income) // N:   # 모든 값을 합한거에 N을 나눳을때 i가 더 작으면
            result += 1             # +1씩 해줌
        else:                       # 아니면 패스
            continue
    print(f'#{test_case} {result}')

 # N자리 더하고 N으로 나누면 평균값이 나옴.
 # 평균보다 작은 income의 개수를 구함