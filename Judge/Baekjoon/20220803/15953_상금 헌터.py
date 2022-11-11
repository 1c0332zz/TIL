# https://www.acmicpc.net/problem/15953
import sys

# sys.stdin = open("15953_상금 헌터.txt")

first_place = [1, 3, 6, 10, 15, 21]
first_money = [500, 300, 200, 50, 30, 10]
second_place = [1, 3, 7, 15, 31]
second_money = [512, 256, 128, 64, 32]

for i in range(int(input())):
    a_money = []
    b_money = []

    a, b = map(int, input().split())
    for i in first_place:
        if a > 21 or a == 0:
            a_money = [0]
        elif a <= i:
            a_money.append(first_money[first_place.index(i)])

    for j in second_place:
        if b > 31 or b == 0:
            b_money = [0]
        elif b <= j:
            b_money.append(second_money[second_place.index(j)])

    print((max(a_money) + max(b_money)) * 10000)