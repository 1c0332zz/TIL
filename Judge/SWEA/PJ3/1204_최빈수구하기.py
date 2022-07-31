# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJCO4t6cCMDFASv&contestProbId=AV13zo1KAAACFAYh&probBoxId=AYJCO4t6cCQDFASv&type=PROBLEM&problemBoxTitle=1%EC%A3%BC%EC%B0%A8&problemBoxCnt=7

import sys
sys.stdin = open("1204_최빈수 구하기_input.txt")

T = int(input())
for tset_case in range(1, T+1):

    idx = int(input())                         
    score = list(map(int, input().split()))     # 점수를 받아옴                        
    max_score = max(score)                      # 가장 높은 점수를 함수로 지정해줌
    # print(max_score)                          # 이유: 가장높은점수로 0을 사용해 리스트함수를 만들면 0의 개수가 순서대로 1~100까지 나열됨 이걸로 점수를 찾아냄
    score_list = [0] * 1001                     # [0, 0, 0]이런식으로 생성 여기서 0번째인덱스는 1점 1번째 인덱스는 2점 이런식으로...하지만 나중에 1000번째에 이상한 수가떠서 1000개로 정의함
    # print(score_list)                         

    for i in score:                             # 점수마다 i에 넣어주고 
        score_list[i] += 1                      # 점수가 41이면 41번째 인덱스에 들어가서 +1해야함
    # print(score_list[1000])                   # 프린트를 해보면 각 점수별로 중복이 몇개인지 나옴 근데 1000번쨰는 뭐지?
    # print(f'score_list의 index를 1부터라고 했을 때, 최빈값은 {score_list.index(max(score_list))+1} 이며, 총 {max(score_list)}번 나왔다')
        result = []                             # 결과를 담기위한 리스트를 정의함 중복때매
        max_list = max(score_list)              # 제일큰수들을 리스트안에 넣어줌
        for j in range(len(score_list)):        # 0번째부터 돌려줌
            if score_list[j] == max_list:       # 리스트의 N번째가 제일큰 리스트랑 같은지 확인
                result.append(j)                # 같으면 리스트에 담아줌
    print(f'#{idx} {max(result)}')              # 그중 제일 큰수 찾아서 프린트


