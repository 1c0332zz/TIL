# https://www.acmicpc.net/problem/1598
a, b = map(int, input().split())
a = a - 1
b = b - 1
print(abs((a//4) - (b//4)) + abs((a%4) - (b%4)))