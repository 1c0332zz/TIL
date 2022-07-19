# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

numbers = 123
# answer = 0

# for number in str(numbers):
#     answer += int(number)
# print(answer)


# numbers가 0일때 stop
# => int는 0일 때 false
result = 0
while numbers:
    # 몫은 다음 number가 됨.
    # 나머지는 더해 나가면 된다
    result += numbers % 10
    numbers //= 10
print(result)
