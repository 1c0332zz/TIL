N = int(input())

for number in range(1, N + 1): # 1부터 N까지의 모든 수의 분해합을 탐색
    split_sum = 0 # 분해합을 저장할 변수

    for digit in str(number): # 각 자리수를 문자열로 변환하고
        split_sum = split_sum + int(digit) # 각자리수의 합을 split_sum에 저장시켜줌
    split_sum = split_sum + number
    
    if split_sum == N:
        print(number)
        break
else:
    print('0')