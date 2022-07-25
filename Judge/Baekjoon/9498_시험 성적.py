T = int(input())

# if 90 <= T <= 100:
#     print('A')
# elif 80 <= T <= 89:
#     print('B')
# elif 70 <= T <= 79:
#     print('C')
# elif 60 <= T <= 69:
#     print('D')
# else:
#     print('F')

# 위에 코드 조금이라도 줄여서... 다시

if 90 <= T:
    print('A')
elif 80 <= T:
    print('B')
elif 70 <= T:
    print('C')
elif 60 <= T:
    print('D')
else:
    print('F')