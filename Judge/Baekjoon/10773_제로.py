import sys
sys.stdin = open('10773_제로.txt')


k = int(input())
money = []

for i in range(k):
    money.append(int(input()))
# print(money)

stack = []

for i in money:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))