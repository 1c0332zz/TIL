import sys
sys.stdin = open("20001_고무오리디버깅.txt", encoding='UTF-8')

A = input()
if A == '고무오리 디버깅 시작' :
    pro = 0
    while(True) :
        B = input()
        if B == '고무오리 디버깅 끝' :
            if pro == 0 :
                print('고무오리야 사랑해')
                break
            else :
                print('힝구')
                break
        elif B == '문제' :
            pro += 1
        elif B == '고무오리' and pro == 0 :
            pro += 2
        elif B == '고무오리' and pro != 0 :
            pro -= 1