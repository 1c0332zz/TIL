# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# 첫번째로 큰수를 어느공간에 넣어놓고 나머지수를 다시 변수에 입력하여 그 변수중에 제일 큰수의 값을 나타낸다

numbers = [0, 20, 100, 40]
max_num = numbers[0]
second_number = numbers[0]

for n in numbers:
    if max_num < n:
        second_number = max_num
        max_num = n
    elif second_number < n and n <max_num:
        second_number = n
print(second_number)
