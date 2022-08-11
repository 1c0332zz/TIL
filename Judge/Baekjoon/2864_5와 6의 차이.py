# https://www.acmicpc.net/problem/2864
a, b = list(input().split())

n = int(a.replace('5', '6')) + int(b.replace('5', '6'))
m = int(a.replace('6', '5')) + int(b.replace('6', '5'))
print(m, n)