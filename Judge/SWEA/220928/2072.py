import sys
sys.stdin = open("2072.txt")

T = int(input())

for tc in range(1, T+1):
    arr = map(int, input().split())
    result = 0
    for i in arr:
        if i % 2 == 1:
            result += i
    print(f'#{tc} {result}')
