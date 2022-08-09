# https://www.acmicpc.net/problem/2588

x = int(input())
y = input()

for i in y[::-1]:
    print(x*int(i))
print(x*int(y))