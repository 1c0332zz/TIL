# https://www.acmicpc.net/problem/2606
from pprint import pprint
import sys

sys.stdin = open("2606_바이러스.txt")

n = int(input())
m = int(input())
edge = []

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)
pprint(graph)