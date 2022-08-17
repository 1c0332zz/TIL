# https://www.acmicpc.net/problem/2495

import sys
sys.stdin = open("2495_연속구간.txt")

for _ in range(3):
    arr = input()
    # 전에 숫자랑 비교해줄 변수지정
    number = 0
    # 카운트해준 숫자를 넣어줄 리스트 지정
    max_number = []
    # 0으로 하면 최초 비교했던 본인을 못새어서 1로함
    cnt = 1
    
    # 입력받은만큼 반복문 돌리고
    for i in arr:
        # i가 넘버랑 같지 않으면 넘버랑 i랑 일치시키고 max_number에 cnt를 추가해주고 cnt는 1로 초기화
        if i != number:
            number = i
            max_number.append(cnt)
            cnt = 1
        # 연속되는 수면 cnt에 +1해줘서 몇번 연속되는지 카운트해줌. 그리고 다른수가 나오면 if로 넘어가서 리스트에 추가해주고 cnt는 초기화
        else:
            cnt += 1

    # 이거 안하면 99999999같은 수가 8로 나와야하지만 추가가 안되서 1로 카운트됨. 
    max_number.append(cnt)
    
    # 가장 큰 수를 출력해줌
    print(max(max_number))