# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open("10804_문자열의 거울상_input.txt")

T = int(input())
for test_case in range(1, T+1):

    arr = list(input())     # 입력할 문자를 리스트로 만들어준다.
    dic_ = {'b' : 'd', 'd' : 'b', 'p' : 'q', 'q' : 'p'} # 문자열을 거울에 비추었을때 나타나는 것처럼 딕셔너리를 짜준다.
    arr.reverse()           # 문자열을 뒤집어준다.
    # print(arr)            # 뒤집어진거 잘 나오는지 확인
    result = ''             # 결과를 넣어줄 문자열 변수 정의
    for i in arr:           # 각 문자열을 반복해줌
        result += dic_[i]   # 해당 문자가 딕셔너리에 매칭되서 결과에 넣어줌
    print(f'#{test_case} {result}')     # 그대로 출력