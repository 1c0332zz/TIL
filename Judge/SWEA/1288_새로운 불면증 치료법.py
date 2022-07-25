import sys
sys.stdin = open("1288_input.txt", "r")

# 첫 번째 : N번 양
# 두 번째 : 2N번 양
# k 번째 : kN번 양
# 이전에 셌던 번호들의 각 자리수에서 0~9까지의 모든 수를 본것은 몇 번 양을 센 시점?  

T = int(input())
for x in range(1, T + 1): # 몇회를 셀껀지 : x
    N = int(input()) # 몇번째 까지 샐껀지 : N
    sheep = 0 # 양을 센 시점이 언제인지 아웃풋 해줄 변수
    if x * N
