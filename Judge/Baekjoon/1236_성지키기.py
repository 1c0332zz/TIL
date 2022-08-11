# https://www.acmicpc.net/problem/1236
import sys
sys.stdin = open("1236_성지키기.txt")

# 행과 열을 받아준다.
n, m = map(int, input().split())

# 행열을 만들어줌
matrix = [list(input()) for _ in range(n)]  

# 숫자를 카운트하기 위한 변수 생성
cnt = 0
cnt2 = 0

# 행을 한번씩 반복해줌.
for i in range(n):
    # 행 안에 X가 없으면 +1을 해줌
    if 'X' not in matrix[i]:
        cnt += 1

# 추가로 열도 반복해 줘야함.
for j in range(m):
    # 열 안에서 행을 다시 한번 반복해줌으로써 열에 X가 없으면 +1을 해줌 
    if 'X' not in [matrix[i][j] for i in range(n)]:
        cnt2 += 1

# 두 수중 큰 수를 출력함.
print(max(cnt, cnt2))