# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict
def solution(clothes):
    dic = defaultdict(list)
    res = 1
    for item, key in clothes:
        dic[key].append(item)

    for key in dic.keys():
        res *= len(dic[key]) + 1

    res -= 1
    return res

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))