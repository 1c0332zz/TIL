# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = [] # 모든 수를 더했을때 나온 결과
    reuslt = [] # 모든 숫자들을 더했을때 나오는 값을 담을 변수(중복X)
    for i in range(len(numbers)): # 리스트안의 수를 인덱스별로 i에 담음
        for j in range(len(numbers)): # 마찬가지로 리스트안의 수를 인덱스별로 j에 담음
            if i == j: # j와 i가 같으면 무시해줌 ex)2+2 1+1 3+3 4+4 1+1
                continue # 무시하는 함수
            reuslt.append(numbers[i] + numbers[j]) # numbers[i] = 정의되었던 numbers의 i번째에 해당하는 수와 j번째에 해당하는 수를 더한 후 reuslt에 포함시켜준다.
        answer = list(set(reuslt)) # 모든 중복된 수를 제거 한 후 리스트로 감싸줌
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
