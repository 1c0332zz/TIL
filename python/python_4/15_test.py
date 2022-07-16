# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word = 'banana'

# 문자로 순회하는 것이 아니라
# 인덱스로 접근해서 쓰자.
# 원하는 숫자? 0 1 2 3 4 5
# 얻는 방법은? renge(len(word)) => range(6) => 0 ~ 5
for idx in range(len(word)):
    if word[idx] == "a":
        print(idx)
        break
else:
    print(-1)

