# https://www.acmicpc.net/problem/20001
import sys
sys.stdin = open("20001_고무오리디버깅.txt", encoding='UTF-8')

ducks = []
duck = []
d = input()

while True:
    duck.append(input())

    if duck[0] == "문제":
        ducks.append(duck.pop(0))

    if duck[0] == "고무오리":
        if ducks[0] == "문제":
            ducks.pop(0)
            duck.pop(0)
        else:
            ducks.insert(0, "문제")
            ducks.insert(0, "문제")
            duck.pop(0)

    if duck[0] == "고무오리 디버깅 끝":
        if ducks not in "문제":
            print("힝구")
            break
        else:
            break

if duck[1] == "고무오리 디버깅 끝" and duck[0] == "고무오리 디버깅 끝":
    print("고무오리야 사랑해")