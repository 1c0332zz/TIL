# https://www.acmicpc.net/problem/2711

# T = int(input())

# for test_case in range(T):
#     a, b = input().split()
#     b = list(b)
#     a = int(a)
#     b.pop(a-1)
#     for i in b:
#         print(i, end="")
# print()



# T = int(input())

# for tc in range(T):
#     num, str_ = input().split()
#     num = int(num)
#     print(str_[:num-1], str_[num:], sep="")

num, str_ = input().split()
num = int(num)
print(str_[:num-1], str_[num:], sep="")