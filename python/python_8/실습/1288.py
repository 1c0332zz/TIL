import sys
sys.stdin = open("1288_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # Input 가져오기 (첫번째 값 -> 1)
    N = int(input())
    N1 = N
    # Set에 계속 추가 예정
    numbers = set()
    # while 반복 => set 길이가 10이 될 때까지
    while True:
        # for 반복 : 숫자를 문자로
        for n in str(N):
        # numbers set에 추가 
            numbers.add(n)
        if len(numbers) == 10:
            break
        # print(n, numbers)
        N += N1
    print(f'#{test_case} {N}')

# N*cnt OK! 