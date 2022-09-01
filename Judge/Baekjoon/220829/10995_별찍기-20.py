# https://www.acmicpc.net/problem/10995

T = int(input())
star = ''
for i in range(T): # 홀/짝 줄 구분하여 구분함
    if i % 2 == 0: # 짝수는 오른쪽 공백이 들어간 별
        star = '* ' * T
    else: # 홀수 i는 왼쪽 공백이 들어간 별
        star = ' *' * T
    print(star)