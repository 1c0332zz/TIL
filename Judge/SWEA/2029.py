import sys
sys.stdin = open("2029_input.txt", "r")

T = int(input()) # 3

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(test_case, a // b, a % b))