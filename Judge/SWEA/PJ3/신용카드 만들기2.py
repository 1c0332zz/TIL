# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open("신용카드 만들기2_input.txt")

T = int(input())

for test_case in range(1, T+1):
    card_number = list(input())
    if card_number[0] == (card_number[0][3]):
        print(card_number)


        # 아직 카드의 첫번쨰 숫자에 접근하는 방법을 잘 모르겠습니다..ㅠㅠ