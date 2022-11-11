# https://www.acmicpc.net/problem/2309
import sys
sys.stdin = open("2309_일곱 난쟁이.txt")

list = [int(input()) for i in range(9)]

total = sum(list)

for i in range(9):
    for j in range(i+1,9):
        if 100 == total - (list[i] + list[j]): 
            num1,num2=list[i],list[j]

            list.remove(num1)
            list.remove(num2)
            list.sort() # 오름차순 정리

            for i in range(len(list)):
               print(list[i])
            break

    if len(list)<9:
        break


# # 맞는 인덱스 넣어줄 리스트생성
# seven = []
# max_total = 0
# # 반복문 7명이니 7번 돌림
# for a in range(n-5):
#     for b in range(a+1, n-4):
#         for c in range(b+1, n-3):
#             for d in range(c+1, n-2):
#                 for e in range(d+1, n-1):
#                     for f in range(e+1, n):
#                         for g in range(f+1, n):
#                             total = nine[a]+nine[b]+nine[c]+nine[d]+nine[e]+nine[f]+nine[g]
#                             if total == 100:
#                                 max_total = total
#                                 seven = [nine[a], nine[b], nine[c],nine[d],nine[e],nine[f],nine[g]]
                                
#                                 result = sorted(seven)
#                                 for i in result:
#                                     print(i)
                                
#                             break