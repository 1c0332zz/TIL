# https://www.acmicpc.net/problem/2530
import sys
sys.stdin = open("2530_인공지능 시계.txt")

H, M, S = map(int, input().split())
D = int(input())

# H, M, S = 14, 30, 0
# D = 200

S += D
M += S // 60
H += M // 60
print(H % 24, M % 60, S % 60)

# while D >= 60:
#     if  D >= 60:
#         M = M + D // 60
#         S = S + (D % 60)
#         D = D % 60
#     if M >= 60:
#         H = H + M // 60
#         M = M % 60
#     if H >= 24:
#         H = H - 24
#     # if D < 60:
#     #     S = D + S
#     #     if S >= 60:
#     #         M = M + (S // 60)
#     #         S = S % 60
#     if S >= 60:
#         M = M + (S // 60)
#         S = S - 60
