# https://www.acmicpc.net/problem/5622
dialing = {
    1 : '', 2 : 'ABC', 3 : 'DEF',
    4 : 'GHI', 5 : 'JKL', 6 : 'MNO',
    7 : 'PQRS', 8 : 'TUV', 9 : 'WXYZ',
    0 : ''
}

word = input()
time = 0

# print(range(1, len(dialing)))

for i in word:
    for j in range(1, len(dialing)):
        if i in dialing[j]:
            time += j + 1
print(time)