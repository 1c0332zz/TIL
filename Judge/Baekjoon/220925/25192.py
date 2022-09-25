# https://www.acmicpc.net/problem/25192
import sys
sys.stdin = open("25192.txt")
import sys;input=sys.stdin.readline

cnt = 0
dic = {}
for _ in range(int(input())):
  word = input().strip()
  
  if word=='ENTER':
    cnt += len(dic)
    dic={}
  
  else: 
    dic[word] = 1

print(cnt+len(dic))

# dic = {}
# cnt = 0

# for _ in range(int(input())):
#     word = input()

#     if word == "ENTER":
#         for k, v in dic.items():
#             if v == 1:
#                 cnt += 1
#         dic = {}
    
#     else:
#         if word not in dic:
#             dic[word] = 1

# for key,value in dic.items():
#     if value==1:
#         cnt+=1

# print(cnt)





# N = int(input())
# arr = []
# cnt = 0
# for _ in range(N):
#     word = input()
#     if word == "ENTER":
#         arr = []
#     elif word not in arr:
#         arr.append(word)
#         cnt += 1
# print(cnt)
