# https://www.acmicpc.net/problem/2776
import sys
sys.stdin = open("2776_암기왕.txt")

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    note1 = {n:0 for n in note1}
    M = int(input())
    note2 = list(map(int, sys.stdin.readline().split()))
    
    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)

    # 이게 더 느리구나,,,
    # for i in range(M):
    #     if note2.pop() in note1:
    #         print(1)
    #     else:
    #         print(0) 