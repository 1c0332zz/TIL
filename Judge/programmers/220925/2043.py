# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QJ_8KAx8DFAUq

P, K = map(int, input().split())
cnt = 1
while 1:
    if P != K:
        cnt += 1
        K += 1
    else:
        print(cnt)
        break