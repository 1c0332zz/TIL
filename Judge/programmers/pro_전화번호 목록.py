# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

    # answer = True
    # hash_map = {}
    # for phone_number in phone_book:
    #     hash_map[phone_number] = 1
    # for phone_number in phone_book:
    #     temp = ""
    #     for number in phone_number:
    #         temp += number
    #         if temp in hash_map and temp != phone_number:
    #             answer = False
    # return answer


    # for i in range(len(phone_book)): 
    #     pivot = phone_book[i] 
    #     for j in range(i+1, len(phone_book)): 
    #         strlen = min(len(pivot), len(phone_book[j])) 
    #         if pivot[:strlen] == phone_book[j][:strlen]: 
    #             return False 
    # return True

print(solution(["12","123","1235","567","88"]))