# https://www.acmicpc.net/problem/1652

import sys
sys.stdin = open("1652_누울 자리를 찾아라.txt")

# 정사각형 크기 n을 받아주고 표로 만들어준다.
n = int(input())
matrix = [list(input()) for _ in range(n)]

cnt = 0
result = 0
# 행
# 열을 먼저 나눠줌
for i in range(n):
    # 밑에서 X를 만나지 못하면 여기까지 cnt가 누적되서 올라오게 되니 잠자리를 +1해주고 cnt초기화해줌
    if cnt >= 2:        
        result += 1
        cnt = 0
    else:
        cnt = 0
    # 행을 나눠줌으로써 2차원리스트로 만들어줌
    for j in range(n):
        # .을 만나면 cnt에 +1를 해주고
        if matrix[i][j] == '.':
            cnt += 1
        # X를 만나고 cnt가 2이상이면 잠자리 +1이고 cnt는 다시 초기화 시켜줌
        elif matrix[i][j] == 'X':
            if cnt >= 2:
                result += 1
                cnt = 0           
            else:
                cnt = 0
# 끝가지 X를 만나지 못한 2이상의 cnt는 결과에 +1해줌.
if cnt >= 2:
    result += 1
    cnt = 0

# 열
# 해석은 위와 같고 행을 나누는게 아니라 열로 나누어줌. [i][j] 위치만 바뀜
result2 = 0
for i in range(n):
    if cnt >= 2:
        result2 += 1
        cnt = 0
    else:
        cnt = 0
    for j in range(n):
        if matrix[j][i] == '.':
            cnt += 1
        elif matrix[j][i] == 'X':
            if cnt >= 2:
                result2 += 1
                cnt = 0           
            else:
                cnt = 0
if cnt >= 2:
    result2 += 1
    cnt = 0


print(result, result2)