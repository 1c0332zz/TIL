# https://www.acmicpc.net/problem/10101

x = int(input())
y = int(input())
z = int(input())

if x + y + z == 180:
    if x == y == z:
        print('Equilateral')
    elif x == y or y == z or x == z:
        print('Isosceles')
    elif x != y != z != x:
        print('Scalene')
else:
    print("Error")
