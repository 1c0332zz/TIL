# https://www.acmicpc.net/problem/9012

import sys
sys.stdin = open("9012_괄호.txt")

T = int(input())
for _ in range(T):
    tb = list(input())
    vps = []
    for i in tb:
        if i == "(":
            vps.append(i)
        elif i == ")":
            if vps:
                vps.pop()
            else:
                print("NO")
                break

    else:
        if len(vps) == 0:
            print("YES")
        else:
            print("NO")











# for _ in range(T):
#     tb = list(input())
#     vps = []
#     cnt = 0
#     while len(tb) != 0:
#         vps.append(tb.pop(0))
#         if len(vps) >= 2:
#             if vps[cnt] + vps[cnt+1] == "()":
#                 vps.pop(cnt)
#                 vps.pop(cnt)
#                 cnt = 0
#             else:
#                 cnt += 1
#         if len(tb) == 0:
#             if vps[cnt] + vps[cnt+1] == "()":
#                 vps.pop(cnt)
#                 vps.pop(cnt)
#             else:
#                 print()

#     if len(tb) + len(vps) == 0:
#         print("YES")

        

            

    # while len(tb) != 0:
    #     vps.append(tb.pop(0))
    #     if vps[0] == "(":
    #         if ")" not in tb:
    #             if len(vps) >= 2:
    #                 if vps[0] + vps[1] == "()":
    #                     vps.clear()
    #                     break
    #                 else:
    #                     tb.append(vps.pop(1))
    #             if len(vps) == 0:
    #                 break
    #             else:
    #                 break
    #     if vps[0] == ")":
    #         break
    #     if len(vps) >= 2:
    #             if vps[cnt] + vps[cnt+1] == "()":
    #                 vps.clear()
    #             else:
    #                 cnt += 1
    #                 vps.append(tb.pop())
    # if len(tb) + len(vps) == 0:
    #     print("YES")
    # else:
    #     print("NO")