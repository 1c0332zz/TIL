# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

import sys
sys.stdin = open("2071_input.txt", "r")

T = int(input()) # 3

for tset_case in range(1, T + 1):
    i = 0
    count = 0
    numbers = list(map(int, input().split()))
    for number in numbers:
        i += number
        count += 1
    print('#{} {}'.format(tset_case, round(i/count)))
