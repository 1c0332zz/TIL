# https://www.acmicpc.net/problem/2857

import sys
sys.stdin = open("2857_FBI.txt")

arr = []
for i in range(5):
    arr_ = input()
    arr.append(arr_)
FBI = []
for i in range(5):
    if 'FBI' in arr[i]:
        FBI.append(i+1)

if len(FBI) > 0:
    print(*FBI)
else:
    print('HE GOT AWAY!')