# https://www.acmicpc.net/problem/2606
from pprint import pprint
import sys

sys.stdin = open("2606_바이러스.txt")

n = int(input())    # 정점 개수(컴퓨터)
m = int(input())    # 간선 개수(네트워크)
graph = [[] for _ in range(n+1)]
total = 0

# 인접 리스트 생성
for _ in range(m):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

visited =[False] * (n+1)    # 0까지포함시켜서 +1시킴?
def dfs(start): # start에 dfs(1)이 들어옴
    stack = [start] # start = [1]이니까 stack이 1임 
    visited[start] = True   # visited[1]을 방문했으니 트루로 바꿔줌

    while stack:    # 스택이 빌때까지 반복(돌아갈곳이 없을때까지) => len(stack) != 0 같음
        cur = stack.pop() # cur에는 1이 들어감

        for adj in graph[cur]:  # graph[1]이니까 adj엔 2,5가 나옴
            if not visited[adj]:    # 처음엔 visited[2]니까 방문되지 않은거라면
                visited[adj] = True # True로 바꿔줌
                stack.append(adj)   # 그리고 stack엔 2를 넣어줌
dfs(1)  # 1번부터 시작

print(sum(visited)-1) # 자기번호 1 빼고 나머지