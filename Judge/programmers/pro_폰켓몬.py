# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = 0
    dict_ = {}
    N = len(nums) // 2

    for i in nums:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1
    
    if N < len(dict_.keys()):
        answer = N
    else:
        answer = len(dict_.keys())
    return answer

print(solution([3, 1, 2, 3]))