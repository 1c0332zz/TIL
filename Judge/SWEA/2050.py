# 주어진 알파벳을 숫자로 변환하라.

import sys
sys.stdin = open("2050_input.txt", "r")

T = input() # 3
for i in T:
    print(ord(i) - 64, end =' ') 
    # 아스키 코드에서 문자를 숫자로 변환 # ord<<