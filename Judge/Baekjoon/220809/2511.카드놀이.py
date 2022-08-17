# https://www.acmicpc.net/problem/2511

play1 = list(map(int, input().split()))
play2 = list(map(int, input().split()))
A = 0
B = 0
history = "D"

for i in range(10):
    if play1[i] > play2[i]:
        A += 3
        history = "A"
    elif play1[i] < play2[i]:
        B += 3
        history = "B"
    elif play1[i] == play2[i]:
        A += 1
        B += 1
if A > B :
    print(A, B)
    print("A")
elif A < B:
    print(A, B)
    print("B")
else:
    if history == "A":
        print(A, B)
        print("A")
    if history == "B":
        print(A, B)
        print("B")
    if history == "D":
        print(A, B)
        print("D")