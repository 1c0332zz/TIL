# https://www.acmicpc.net/problem/11170

n ,m = map(int, input().split())
card = list(map(int, input().split()))

max_total = 0
# 0, 1, 2
for i in range(n-2):
    # 1, 2, 3
    for j in range(i+1, n-1):
        # 2, 3, 4
        for k in range(j+1, n):
            total = card[i] + card[j] + card[k]

            if max_total < total <= m:
                max_total = total
            if max_total == m:
                break

print(max_total)