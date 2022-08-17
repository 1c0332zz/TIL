# https://www.acmicpc.net/problem/23825

N, M = map(int, input().split()) # 두 수를 입력받음

if N // 2 == M // 2:    # N//2와 M//2가 같으면,
    print(N//2)         # 그대로 프린트해서 값을 표시
else:                   # 아니면,
    print(min(N//2, M//2)) # 둘중 나눈수중 작은 수를 표시

