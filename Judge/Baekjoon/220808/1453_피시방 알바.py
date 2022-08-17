# https://www.acmicpc.net/problem/1453

# 손님수 입력
T = int(input())
# 거절당하는 손님 개수 변수
cnt = 0
# 컴퓨터 100대
computer = [0] * 100
# 몇번자리에 앉을껀지 
guest = list(map(int, input().split()))

# 자리 반복문돌리고
for i in guest:
    # 컴퓨터100대중에 0이고 그자리 앉으면 입력해줌
    if computer[i-1] == 0:
        computer[i-1] = i
    # 아니면 카운트1
    else:
        cnt += 1
print(cnt)