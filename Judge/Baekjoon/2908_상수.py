# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("2908_상수.txt")

A, B = list(input().split()) # 2개의 숫자를 불러오고
A = int(A[::-1]) # 거꾸로 뒤집어준다
B = int(B[::-1])

if A > B : # if문으로 A가 큰경우 A를 출력시키고
    print(A)
elif A < B: # B가 큰 경우 B를 출력시킨다.
    print(B)