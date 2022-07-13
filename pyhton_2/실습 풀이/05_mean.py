# 1. 문제 제공
# 3, 10, 20이라는 요소로 구성된 리스트를 
# numbers 라는 변수에 할당을 했습니다.
numbers = [3, 10, 20]

# 2. 값 초기화
result = 0
count = 0

# 3. 반복
for number in numbers:
    result = result + number
    # result += number
    count = count + 1
    # count += 1

print(result/count)
# print(sum(numbers)/len(numbers))