# 정수 number가 주어질 때, 뒤집어서 출력하기
number = 123

# print(int(str(number)[::-1]))
result = 0
while number: 
    # 이전 결과에 10을 곱하고 
    result *= 10
    # 나머지를 더해주고
    result += number%10
    # number를 깎는다. 
    number //= 10

print(result)
