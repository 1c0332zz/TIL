# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# words = list(map(int, input().split()))
# print(words)
# input (I'm Tuotur 6)
# output ["I'm", 'Tutor', '6']

words = input().split()
print(words)


# 원인: list(map)으로 input문자열을 숫자로 변경해주었다. 이를 지워주고 문자열 자체로 출력해준다. 