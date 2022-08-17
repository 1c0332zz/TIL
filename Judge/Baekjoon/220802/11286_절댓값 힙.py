import heapq
import sys

sys.stdin = open("11286_절댓값 힙.txt")

# 연산의 개수 입력
N = int(input())
# 리스트를 담아줄 변수
list_ = []

for i in range(N):
    # 두번째 입력값 입력 후 리스트로 만들어줌
    list_.append(int(sys.stdin.readline())) 
# 값을 추가해줄 리스트를 만듬
heap = []
for number in list_:
    # n이 0이랑 같지 않으면 절대값이랑 본래의 값을 같이 리스트에 담아줌.
    if number != 0:
        heapq.heappush(heap, (abs(number),number))
    else:
        # n이 0이고 더이상 숫자의 개수가 존재하지 않으면 0을 입력해주고 끝냄
        if len(heap) == 0:
            print(0)
        # n이 0이면 제일앞에수를 꺼내주고 같은 리스트에 담긴 본래의값도 삭제시킴
        else:
            print(heapq.heappop(heap)[1])