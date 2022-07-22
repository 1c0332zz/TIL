# 15. 문자의 위치 구하기 (처음으로)
# 없으면 -1
word = 'bbbbbbbb'

# 1. for - else

# 문자로 순회하는 것이 아니라! 
# 인덱스로 접근해서 쓰자.
# 원하는 숫자? 0, 1, 2, 3, 4, 5
# 얻는 방법은? range(len(word)) => range(6) => 0 ~ 5
for idx in range(len(word)):
    # print(idx, word[idx])
    # 알파벳이 a일때 
    if word[idx] == 'a':
        print(idx)
        break
# for문을 다 돌았다는 뜻은
# 한번도 break에 안걸렸다.
# 즉, a는 없었다.
else:
    print(-1)

# 2. for - else
# a가 있었냐? 없었냐? (boolean)
is_a = False
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break

if not is_a:
    print(-1)