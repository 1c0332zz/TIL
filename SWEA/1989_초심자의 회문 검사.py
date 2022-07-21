import sys
sys.stdin = open("1989_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1): # 5회
    palindrome = input()
    result = ''
    for char in palindrome:
        result = char + result
        # 일단 여기까지 문자열을 거꾸로 뒤집었음. 이제 이 단어가 회문인지 확인
        # palindrome랑 값이 똑같은지?
        if palindrome == result:
            print(f'#{test_case} {1}')
        else:
            print(f'#{test_case} {0}')