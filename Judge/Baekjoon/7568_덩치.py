import sys
sys.stdin = open("7568_덩치.txt")

T = int(input())

list_ = []
for tc in range(T):
    x, y = map(int, input().split())
    list_.append((x, y))
    # print(x,y)
# print(list_)

arr = [0] * T
for i in range(T):
    a = list_[i]
    for j in range(T):
        b = list_[j]
        if a[0] > b[0] and a[1] > b[1]:
            arr[j] += 1
    
# print(arr)

for i in arr:
    print(i+1, end=' ')
