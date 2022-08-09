from pprint import pprint


# 회전
matrix = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):  # 0, 1, 2
    for j in range(n):  # 0, 1, 2
        rotated_matrix[i][j] = matrix[j][n-i-1]
pprint(rotated_matrix)
