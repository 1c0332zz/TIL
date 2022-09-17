# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    arr_ = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    answer = ""
    list_ = ""
    for i in s:
        list_ += i
        if len(list_) >= 3:
            for j in range((len(arr))):
                if arr[j] == list_:
                    answer += str(j)
                    list_ = ""
        if i in arr_:
            answer += str(i)
            list_ = ""

    return int(answer)


print(solution("one4seveneight"))

# replace기억했다면 금방 풀었을 텐데........

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)