# https://www.acmicpc.net/problem/20291
import sys
sys.stdin = open("20291_파일 정리.txt")

N = int(input())
files = []
for tc in range(N):
    # 확장자 받아오지만, .기준으로 앞에 날려야함 split?
    file = input()
    a = file.split('.')
    files.append(a[1])
files = sorted(files)

dict = {}
for i in files:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
# print(dict)

for k, v in dict.items():
    print(k, v)
