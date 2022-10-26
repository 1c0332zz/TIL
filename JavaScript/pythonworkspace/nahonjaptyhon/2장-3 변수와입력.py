# 변수 : snakecase
# 변할 수 있는 숫자
# 어떠한 데이터에 이름을 붙인 것
# pi(식별자) = 3.14(값)

#변수 선언과 할당
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)
print("원의 넓이 =", pi * r * r)

# 복합 대입 연산자
# a = a + 1
# a += 1
print("------------------")
# a = a - 1
# a -= 1
pi = 3.14
pi = pi + 10
pi += 10
pi -= 10 # pi = pi - 10
print("pi=", pi)
print("----------------------------")

#input()함수의 결과는 무조건 문자열
string = input("인사말을 입력하세요>")
print(string)


a = input("첫 번째 숫자를 입력해주세요")
b = input("두 번째 숫자를 입력해주세요")

print(a+b)