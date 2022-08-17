import sys
sys.stdin = open("1100_하얀칸.txt")

# 8x8의 체스판을 만들어줌
matrix = [list(input()) for _ in range(8)] 

cnt = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if 'F' in matrix[i][j]:
                cnt += 1
print(cnt)
