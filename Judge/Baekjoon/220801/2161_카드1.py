# https://www.acmicpc.net/problem/2161

from collections import deque


T = int(input())
list_ = []

for i in range(1, T + 1):
    list_.append(i)
# print(list_) [1, 2, 3, 4, 5, 6, 7]이 여기에 다 담김!

result = [] # 버린카드를 담을 리스트
queue = deque(list_)    # deque 함수에 리스트를 담아주고 변수로 지정해줌. 
# print(queue) deque([1, 2, 3, 4, 5, 6, 7])라고 출력됨

while len(queue) > 1:     # 이런식으로 조건문을 사용하면 1자리수가 남을떄까지 돌게됨
    print(queue.popleft(), end=' ') # popleft로 맨 왼쪽숫자를 출력에 담아주고 
    queue.append(queue.popleft())   # 맨 왼쪽숫자를 맨 오른쪽으로 옮긴다
print(queue[0]) # 이미 맨왼쪽숫자는 출력예정이니 queue의 숫자한개만 출력을 넣어준다