# https://www.acmicpc.net/problem/8958
import sys
from unittest import result

sys.stdin = open("8958_OX퀴즈.txt")

T = int(input())

for test_case in range(1, T+1):
    OX = input() 
    results = 0                 # 계속 +1씩 더하거나 X를 만나면 0으로 초기화할 변수
    result = 0                  # 나온 값을 계속 더하는 변수
    for i in OX:                # OOOXXXOXOXOX를 각각 반복해준다.
        if i == 'O':            # i가 O랑 같으면 
            results += 1        # results변수에 +1을 해준다. X를 만나지 않는이상 results(+1)이면 계속 +1을 해줌 
        elif i == 'X':          # X를 만나면 
            results = 0         # 연속했던 점수를 다 0으로 바꿔준다
        result += results       # if와 elif을 지날때마다 변수에 계속 저장해준다. 
    print(result)