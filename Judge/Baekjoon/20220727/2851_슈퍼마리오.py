import sys

sys.stdin = open("2851_슈퍼마리오.txt")
scores = [] # 점수를 저장할 리스트
N = 10 # 10개의 정수
for test_case in range(N):  # 총 10줄로 입력되니까 10개로 for문을 돌려줌
    score = int(input())    # 10줄을 입력받을 input
    scores.append(score)    # scores에 입력받은값을 모두 추가해 리스트로 만들어줌.

sum_ = 0            # 누적합을 계산해줄 변수
min_diff = 10e9     # 가장 작은 차이를 비교해줄 수
max_score = 0       # 가장 큰 누적 점수를 넣어줄 변수
for i in range(N):      # 마찬가지로 10번 입력 해줘야함
    sum_ += scores[i]       # 누적합을 나타냄
    diff = abs(100 - sum_)  # abs절대값 함수로 100-누적합을 해주면 100이랑 차이가 나는 수를 diff에 저장해줌
    if diff <= min_diff:     # 100과 차이나는 수가 맥스값이랑 얼마나 차이가 나는지
        min_diff = diff     # 차이가 나는게 가장 좁다면 diff에 새롭게 저장해줌.
        max_score = sum_    # 그리고 차이값을 저장해줌
print(max_score)
