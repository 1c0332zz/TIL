numbers = [0, 20, 100, 40]
max_number = float("-inf")
second_number = float("-inf")

# 1. 전체 숫자를 반복
for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_number < n:
        # 최대값이었던 것이 두번째로 큰 수
        second_number = max_number
        max_number = n
    # elif second_number < n < max_number:
    elif second_number < n and n < max_number:
        second_number = n
print(second_number)