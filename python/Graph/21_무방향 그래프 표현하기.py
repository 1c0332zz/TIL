from pprint import pprint
import sys
sys.stdin = open('21_무방향 그래프 표현하기.txt')

# 입력값 받아줌.
n, m = map(int, input().split())
edge = []
for i in range(m):
    edges = list(map(int, input().split()))
    edge.append(edges)

# 인접 행렬을 표현할 0으로 된 메트릭스 생성
matrix = [[0] * (n+1) for _ in range(n+1)]

# 입력값의 리스트 안에 리스트를 i로 반복을 돌려주고
for i in edge:
    # i안에 리스트를 각 0,1을 v1,v2로 정의
    v1, v2 = i[0], i[1]
    # 0으로 된 행렬리스트에 각각 1을 삽입
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1
    
pprint(matrix)


# 인접 리스트를 표현할 리스트 안의 빈리스트 생성
graph = [[] for _ in range(n+1)]

# 입력값의 리스트 안에 리스트를i로 반복으로 돌려주고
for j in edge:
    # i안에 리스트를 각 0,1을 v1,v2로 정의
    v1, v2 = j[0], j[1]
    # 빈 리스트의 v1번째에 해당하는 인덱스 안에 v2를 삽입
    graph[v1].append(v2)
    graph[v2].append(v1)
pprint(graph)
