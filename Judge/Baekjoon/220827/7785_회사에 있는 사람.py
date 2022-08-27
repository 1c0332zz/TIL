# https://www.acmicpc.net/problem/7785
import sys
sys.stdin = open("7785_회사에 있는 사람.txt")

N = int(sys.stdin.readline())
arr = {}
for tc in range(N):
    staff = sys.stdin.readline().split()
    arr[staff[0]] = staff[1]
# print(arr)

arr = sorted(arr.items(), reverse=True)
# print(arr)

for i in arr:
    if 'enter' in i:
        print(i[0])



# for k, v in arr.items():
#     if v == 'enter':
#         print(k)