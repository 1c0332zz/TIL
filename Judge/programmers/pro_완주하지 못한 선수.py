# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    dict_ = {}
    # 딕셔너리 안에 다 담는다.
    for i in participant:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1


    for i in completion:
        if dict_[i] == 1:
            del dict_[i]
        else:
            dict_[i] -= 1

    return list(dict_.keys())[0]

print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))