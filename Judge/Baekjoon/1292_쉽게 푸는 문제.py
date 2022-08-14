# https://www.acmicpc.net/problem/1292
# [1,2,2,3,3,3,4,4,4,4] 이런 리스트안에 1 3이라는 수를 주면 1번부터 3번까지 더하란소리;;;;;
a,b = map(int,input().split())
 
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
 
print(sum(arr[a:b+1]))
