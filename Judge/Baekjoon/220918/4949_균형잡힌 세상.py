import sys
sys.stdin = open("4949_균형잡힌 세상.txt")


while True:
    word = input().rstrip()
    if word == ".":
        break
    arr = []
    temp = True

    for i in word:
        if i == "(" or i == "[":
            arr.append(i)
        
        elif i == ")":
            if not arr or arr[-1] == "[":
                temp = False
                break
            elif arr[-1] == "(":
                arr.pop()
        
        elif i == "]":
            if not arr or arr[-1] == "(":
                temp = False
                break
            elif arr[-1] == "[":
                arr.pop()
        
    if len(arr) == 0 and temp == True:
        print("yes")
    else:
        print("no")



# while 1:
#     d=input()
#     if d=='.':
#         break
#     q=[]

#     for i in d:
#         if not i in '()[]':
#             continue
#         q.append(i)
        
#         while len(q)>=2 and(q[-2]=='('and q[-1]==')'or q[-2]=='['and q[-1]==']'):
#             q.pop()
#             q.pop()
#     print('no'if q else'yes')