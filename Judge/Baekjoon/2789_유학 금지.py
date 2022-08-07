# https://www.acmicpc.net/problem/2789

arr = 'CAMBRIDGE'
n = input()

for i in arr:
    for j in n:
        if j in i:
            n = n.replace(i, "")
print(n)
