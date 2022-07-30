# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open("문자열의 거울상_input.txt")

T = int(input())
dic_ = {                        # 문자열을 거울에 비추었을때 나타나는 것처럼 딕셔너리를 짜준다.
    'b' : 'd', 'd' : 'b',
    'p' : 'q', 'q' : 'p'
}

for test_case in range(1, T+1):
    str_ = input()              # 단어를 입력해줄 변수를 지정
    for i in list(str_):        # 단어를 넣어주면서 리스트 지정해준다. 한 단어마다 반복될 수 있도록
        print(dic_.keys(i))     # 이렇게 하면 딕셔너리의 값이 나와야될 것 같은데 안나오니까 문제가 막힌다.
        