# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjKXKALcDFAUq

A , B = map(int, input().split())
if A == 1 and B == 3:
    print("A")
elif A == 3 and B == 1:
    print("B")
elif A > B:
    print("A")
elif A < B:
    print("B")
