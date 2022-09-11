# https://www.acmicpc.net/problem/14720
import sys
sys.stdin = open("14720_우유축제.txt")

N = int(input())
milk = map(int, input().split())
cnt = 0
cnt_ = 0

for i in milk:
    if i == cnt:
        cnt += 1
        cnt_ += 1
        if cnt == 3:
            cnt = 0
print(cnt_)
    