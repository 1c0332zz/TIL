import sys
sys.stdin = open("1933_input.txt", "r")

# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

T = int(input())
for number in range(1, T + 1):
    # 10이랑 나눴을때 나머지가 0이 되는 수 구하기
    if T % number == 0:
    # 만약에 T에 넘버를 나눴을때 0이랑 같으면... 어디에 어떻게 저장을 해야함?
    # 저장할 필요 없고 number를 그대로 사용!
        print(number, end=' ')
