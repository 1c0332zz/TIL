import sys

sys.stdin = open("2846_오르막길.txt")

T = int(input())
list_ = list(map(int, input().split()))
result_list = []
result = 0

for i in range(1, len(list_)): # 오르막길을 찾기 위해서 인덱싱
    if list_[i] > list_[i-1]: # 오르막길은 현재 값 > 이전 값
        result += list_[i] - list_[i-1] # 누적된 값을 더해줌
        # result_list.append(result)
    else:
        result_list.append(result) # 아닐경우 여태 합을 저장해줌
        result = 0 # 그리고 0으로 초기화

result_list.append(result) # 반복문이 다 끝나면 리스트값을 넣어줌
print(max(result_list)) # 큰 수 출력