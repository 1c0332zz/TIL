# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

import sys
sys.stdin = open("1986_input.txt", "r")

# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    # N값을 입력하고
    number = 0
    for numbers in range(1, n + 1):
    # N 까지의 숫자니까 렝지로 숫자를 풀어줌
        if numbers % 2 == 0:
            number -= numbers
        #나눴을때 0이면 짝수, 0에다가 -짝수 해줌
        else:
            number += numbers
        # 나머지는 다 홀수니까 0에다가 +홀수 해줌
    print('#{} {}'.format(test_case, number)) # 합쳐진 결과가 나옴?


