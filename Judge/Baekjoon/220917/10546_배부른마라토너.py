# https://www.acmicpc.net/problem/10546
import sys
sys.stdin = open("10546_배부른마라토너.txt")


N = int(input())
player = {}

for _ in range(N):
    A = input()
    if A not in player:
        player[A] = 1
    else:
        player[A] += 1

for _ in range(N-1):
    B = input()
    player[B] -= 1
    if player[B] == 0:
        player.pop(B)

print(list(player.keys())[0])

# for k, v in player.items():
#     if v >= 1:
#         print(k)
#         break