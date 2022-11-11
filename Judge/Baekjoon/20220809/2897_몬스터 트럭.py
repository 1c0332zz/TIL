# https://www.acmicpc.net/problem/2897
from pprint import pprint
import sys
sys.stdin = open("2897_몬스터 트럭.txt")

# 행, 열, 주차장 입력받음
R, C = list(map(int, input().split()))
matrix = [list(input()) for _ in range(R)]  # 문자열을 떨어트려 놔야 해서 split안씀

# [['#', '.', '.', '#'],
#  ['.', '.', 'X', '.'],
#  ['.', '.', 'X', '.'],
#  ['#', 'X', 'X', '#']]

dr = [0, 1, 1]
dc = [1, 1, 0]

# 부순 횟수를 저장할 리스트
# 5개가 필요함
break_count_list = [0] * 5
# 이중 반복문
for r in range(R):
    for c in range(C):
        # 차를 부순 횟수는 탐색을 할 때마다 초기화(0)
        break_count = 0

        # 조건1. 기준 좌표가 빌딩(#)이면 안된다.
        if matrix[r][c] == "#":
            continue 
        # 이 다음 반복문의 코드들을 무시하고, 다음 값을 탐색
        # 성립이 안되는 조건들은 contunue로 지나가고
        # 조건이 성립 될 때만 정상적인 코드를 실행한다.
        
        # 조건2. 기준 좌표가 차라면 부순 횟수 +1
        if matrix[r][c] == "X":
            break_count += 1
        '''
        델타 탐색
        '''
        for d in range(3):
            next_r = r + dr[d]
            next_c = c + dc[d]
            # 조건1. 범위를 벗어나면 안된다.
            if not (-1 < next_r < R and -1 < next_c < C):
                break

            # 조건2. 탐색 좌표에 빌딩이 있으면 안된다.
            if matrix[next_r][next_c] == "#":
                break

            # 조건3. 탐색 좌표에 차가 있으면 부순 횟수를 + 1
            if matrix[next_r][next_c] == "X":
                break_count += 1

        # break를 만나지 않고 for문이 끝나면
        # 혜빈이가 정상적으로 주차를 함.
        else:
            break_count_list[break_count] += 1

for count in break_count_list:
    print(count)


