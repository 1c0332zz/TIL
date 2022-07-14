# 최댓값 구하기
numbers = [-10, -100, -30]
# max_num = float("-inf")
max_num = numbers[0]
# 1. 반복
for n in numbers:
    # print(n)
    # 2. 만약, max값이 n보다 작으면 바꾼다.
    if max_num < n:
        # print('왔냐?')
        max_num = n 
print(max_num)