import sys
sys.stdin = open("6996_애너그램.txt")

T = int(input())
for _ in range(T):
    A, B = input().split()
    if sorted(A) == sorted(B):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')


# insert로도 풀 수 있을 것 같음