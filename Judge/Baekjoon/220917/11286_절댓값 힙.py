# https://www.acmicpc.net/problem/11286
import heapq
import sys

sys.stdin = open("11286_절대값 힙.txt", encoding='UTF-8')

N = int(input())
list_ = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if list_:
            print(heapq.heappop(list_)[1])
        else:
            print(0)
    else:
        heapq.heappush(list_, (abs(x), x))