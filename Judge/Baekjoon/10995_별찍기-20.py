T = int(input())
star = ''
for i in range(T):
    if i % 2 == 0:
        star = '* ' * T
    else:
        star = ' *' * T
    print(star)