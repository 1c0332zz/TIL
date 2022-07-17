# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = [3, 10, 20]

result = 0
count = 0

# 3. 반복
for number in numbers:
    result += number 
    count += 1

print("결과: {}".format(result/count))