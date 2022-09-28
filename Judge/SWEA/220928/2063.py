# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
sys.stdin = open("2063.txt")

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(arr[N // 2])