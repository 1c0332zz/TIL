from pprint import pprint
import sys
sys.stdin = open('21_무방향 그래프 표현하기.txt')

# 입력값 받아줌.
n, m = map(int, input().split())
edge = []
for i in range(m):
    edges = list(map(int, input().split()))
    edge.append(edges)

# 인접 행렬
matrix = [[0] * (n+1) for _ in range(n+1)]

for i in edge:
    v1, v2 = i[0], i[1]
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1
    
pprint(matrix)


# 인접 리스트
graph = [[] for _ in range(n+1)]

for j in edge:
    v1, v2 = j[0], j[1]
    graph[v1].append(v2)
    graph[v2].append(v1)
pprint(graph)
