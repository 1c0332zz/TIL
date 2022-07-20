# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

import sys
sys.stdin = open("2019_input.txt", "r")

T = int(input())
i = 0
for number in range(0, T + 1):
    # 각 수자를 제곱해 주면 된다. 2**n
    print(2**number, end=' ')
