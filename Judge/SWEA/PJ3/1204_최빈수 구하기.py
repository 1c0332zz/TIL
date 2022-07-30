# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJCO4t6cCMDFASv&contestProbId=AV13zo1KAAACFAYh&probBoxId=AYJCO4t6cCQDFASv&type=PROBLEM&problemBoxTitle=1%EC%A3%BC%EC%B0%A8&problemBoxCnt=7

import sys
sys.stdin = open("1204_최빈수 구하기_input.txt")

# T = int(input())

# for tset_case in (1, T+1):
#     idx = int(input())                         
#     arr = map(int, input().split())    
#     score = dict()                             
#     for i in score:                 
#         score.get(i)        
#         if score == i:             
#             score.get() + i               
# print(score)


T = int(input())
for i in range(T):
    idx = int(input())
    arr = list(map(int, input().split()))
    score = dict()
    for s in arr:
        if s in score:
            score[s] += 1
        else:
            score[s] = 1
    _max = max(score.values())

    print('#', end='')
    print(idx, next(key for key, value in score.items() if value == _max))