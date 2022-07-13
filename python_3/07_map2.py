# 직사각형의 넓이를 구하시오.
# 직사각형 세로는 n 가로는 m
# Input 예시
# 10 20

n, m = map(int, input().split())
print(n*m)

# 내장함수를 10을 다 더해주는 함수가 있어요.
def plus10(n):
    return n + 10

numbers = [10, 20, 30]
new_numbers = list(map(plus10, numbers))
print(new_numbers)