import sys
sys.stdin = open("20001_고무오리디버깅.txt", encoding='UTF-8')

stack = []

while True:
    _input = sys.stdin.readline().split("\n")[0]

    if _input == "문제":
        stack.append(_input)
    
    if _input == "고무오리":
        if not stack:
            stack.append("문제")
            stack.append("문제")
        else:
            stack.pop()

    if _input == "고무오리 디버깅 끝":
        break

print("고무오리야 사랑해" if not stack else "힝구")

