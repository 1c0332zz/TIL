# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    dict_ = {}
    # sum_으로 한개의 리스트로 만들어준 뒤
    sum_ = participant + completion
    # 딕셔너리 안에 다 담는다.
    for i in sum_:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1










    # # 값이 2면 완주함
    # for k, v in dict_.items():
    #     if v != 2:
    #         answer = k      

    return answer


print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))