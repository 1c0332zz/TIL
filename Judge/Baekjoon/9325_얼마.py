# https://www.acmicpc.net/problem/9325
import sys

sys.stdin = open("9325_얼마.txt")
T = int(input())

for tc in range(T):
    # 차,옵션개수 가격 입력받고
    car = int(input())
    option_cnt = int(input())
    # 총 금액을 반복문 아래에 넣어서 한싸이클 끝나면 초기화 시켜줌
    amount = 0
    # 옵션개수만큼 반복문 돌림
    for i in range(option_cnt):
        # 옵션개수, 가격 입력받고 둘이 곱하고 총금액에 더해줌.
        cnt, option = map(int, input().split())
        amount += (cnt * option)
    # 한줄씩 출력
    print(car + amount)