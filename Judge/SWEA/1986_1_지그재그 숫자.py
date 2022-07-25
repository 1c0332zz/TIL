# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

import sys
sys.stdin = open("1986_input.txt", "r")

# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    if n % 2 == 1:
        print('#{} {}'.format(test_case, (n+1)/2))
    else:
        print('#{} {}'.format(test_case, (-n/2)))
