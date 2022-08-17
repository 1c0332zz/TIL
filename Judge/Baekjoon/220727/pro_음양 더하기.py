def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): # 정수를 차례대로 비교할 수 있게 range함수를 사용
        if signs[i] == True:        # 정수의 i번째가 signs의 참이랑 같은 배열이면  
            answer += absolutes[i]  # 정답의 변수에 정수의 i번재를 더하고
        elif signs[i] == False:     # 반대로 정수의 i번째가 거짓이면
            answer -= absolutes[i]  # -를 한다.
    return answer

print(solution([4, 7, 12], [True, False, True]))