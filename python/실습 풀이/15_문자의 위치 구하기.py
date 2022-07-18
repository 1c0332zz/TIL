# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# word = 'banana'
# count = 'a'
# lst = []

# for pos, char in enumerate(word):
#     if(char == count):
#         lst.append(pos)
# print(lst)

word = 'banana'

# 문자로 순회하는 것이 아니라..
# 인덱스로 접근
# 원하는 숫자는? 0, 1, 2, 3, 4, 5
# 얻는 방법은? rang(len(word)) -> renge(6) -> 0~5
for idx in range(len(word)):
    # print(idx(여기서 idx는 0이 될테고), word[idx](여기서 idx는 b가 된다))
    # 그럼 a가 될때 만나면 idx를 출력해서 숫자로 뽑아준다.
    if word[idx] == 'a':
        print(idx)
        #그리고 브레이크! 하면 1만 출력이 됨.
        break
# for문을 다 돌았다는 뜻은 break에 안걸렸다(a가 없다)
# 하지만 이것들이 다 없으면 -1을 출력하도록 만들어줌
else:
    print(-1)


# 2
# a가 있었냐? 없었냐? -> (boolena)
is_a = False

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break
if is_a == False:
    print(-1)