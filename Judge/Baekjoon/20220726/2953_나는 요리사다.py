import sys

sys.stdin = open("2953_나는 요리사다.txt")

result = 0  # 합쳐진 변수를 넣을 결과값
idx = 0     # 몇번쨰인지
for i in range(1, 6):                   # 5명의 요리사니까 1~6까지
    score = sum(list(map(int, input().split())))    # 받을때 부터 전부 더해주면 편함
    if score > result:                  # 첫입력받은 점수가 합쳐진 변수보다 크면
        result = score                  # 변수에 저장해놓고
        idx = i                         # 몇번째인지도 같이 저장
print(idx, result)


    
    # max_score = 0
    # sum_score = 0
    # for j in score:
    #     sum_score += j
    #     if sum_score > max_score:
    #         max_score = sum_score
    # print(max_score)