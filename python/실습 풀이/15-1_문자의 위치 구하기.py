# 추가문제 
# 문자열 word가 주어질 때, 해당 문자열에서 `a` 의 모든 위치(index)를 출력해주세요.
# `find()` `index()` 메서드 사용 금지

word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        result.append(idx)
print(result)
