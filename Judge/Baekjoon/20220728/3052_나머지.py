# https://www.acmicpc.net/problem/3052
# set함수 쓰니......그냥 해결
result = []                 # 나눈값을 저장해줄 리스트 생성
for i in range(10):         # 10회에 걸쳐 입력받는다함.
    N = int(input())        # 입력10번해줌
    result.append(N % 42)   # 입력한걸 42로 나누고 나머지를 리스트변수에 저장
print(len(set(result)))     # 리스트에 저장한걸 set으로 중복제거....그리고len으로 개수 출력 끝........



# cnt_ = 0                        # 카운트를 세어줄 변수
# result = []                     # 나눈값을 저장해줄 변수리스트
# for n in range(10):        # 10줄이니까 10번반복
#     N = int(input())            # 입력값
#     for i in [N]:               # 입력값을 나눠야하니까 반복돌림
#         if [i % 42] != result:  # 입력값을 42로 나눳을때 여태 나눳던 수랑 같은게 없으면
#             result + [i%42]     # 나눈값을 저장해줄 변수에 저장
#             cnt_ += 1           # 그리고 카운트 +1
#         elif [i % 42] == result:  # 42로 나눴을때 나눴던 수랑 같으면
#             result + [i%42]     # 그 수 그대로 저장?
# print(cnt_)                     # 실패......................................
