# https://www.acmicpc.net/problem/1157

word = input().upper()      # 입력값을 대문자로 변경
set_word = list(set(word))  # 중복 제거를 위한 리스트변수 
cnt_list = []               # 카운트 숫자를 넣기 위한 리스트변수

for i in set_word:          # 중복제거된 변수를 반복문으로 돌림
    cnt = word.count(i)     # 단어 i를 최초 입력했던 word에서 몇개인지 새어줌
    # print(cnt)            # 출력해봐서 개수와 set_word의 위치가 맞는지 봐줌
    # print(set_word)
    cnt_list.append(cnt)    # 동일하니까 해당 개수를 알파벳의 위치에 입력시켜줌
    # print(cnt_list, set_word)   # 마지막에 [4, 4, 1, 1] ['I', 'S', 'P', 'M'] 로 출력됨
if cnt_list.count(max(cnt_list)) > 1:   # []안에 제일 큰수가 2개 이상이면 ?출력
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))   # []안에 제일큰수가 []안에 어디에 위치해 있지는지를 찾아서
    print(set_word[max_index])                  # 중복을 제거한 리스트안에 어느위치에 있는지 출력