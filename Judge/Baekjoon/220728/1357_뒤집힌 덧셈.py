# https://www.acmicpc.net/problem/1357

X, Y = list(map(int, input().split()))
Rev = int(str(X)[::-1]) + int(str(Y)[::-1])
print(int(str(Rev)[::-1]))