# https://www.acmicpc.net/problem/20001
import sys
sys.stdin = open("20001_고무오리디버깅.txt", encoding='UTF-8')

strat = input()
duck = []

while True:
    A = input()
    if A == "문제":
        duck.append(A)
    if A == "고무오리":
        if not duck:
            duck.append("문제")
            duck.append("문제")
        else:
            duck.pop(0)
    if A == "고무오리 디버깅 끝":
        break

if len(duck) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")