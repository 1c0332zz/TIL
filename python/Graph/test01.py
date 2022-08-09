from pprint import pprint



# 인접 행렬
edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [2, 5],
    [4, 6]
]

n = 7

# n x n 행렬 초기화(0으로 초기화)
matrix = [[0] * n for _ in range(n)]

for edge in edges:
    v1, v2 = edge[0], edge[1]
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

pprint(matrix)