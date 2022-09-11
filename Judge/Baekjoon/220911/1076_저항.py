# https://www.acmicpc.net/problem/1076
import sys
sys.stdin = open("1076_저항.txt")

electronics = {
    "black" :	[0, 1],
    "brown" :	[1,10],
    "red"	: [2, 100],
    "orange" : [3, 1000],
    "yellow" : [4, 10000],
    "green" : [5, 100000],
    "blue" : [6, 1000000],
    "violet" : [7, 10000000],
    "grey" : [8, 100000000],
    "white" : [9, 1000000000],
}

electronic = []
for _ in range(3):
    arr = input()
    electronic.append(arr)

a = electronics[electronic[0]]
b = electronics[electronic[1]]
c = electronics[electronic[2]]

print(int(str(a[0]) + str(b[0])) * c[1])