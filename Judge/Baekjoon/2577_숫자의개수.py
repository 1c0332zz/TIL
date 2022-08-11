# https://www.acmicpc.net/problem/2577
import sys
from unittest import result

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input()) # 3개의 예제를 한줄씩 입력

reults = list(str(A * B * C)) # 예제를 곱한 값을 문자열로 변경 후 리스트로 감싸줌 
# print(reults, type(reults))
for i in range(0, 10): # 숫자를 0부터 9까지의 숫자를 반복해줄거임 
    print(reults.count(str(i))) # 0~9(문자열)가 reults안에 몇개가 있는지 확인 후 바로 출력