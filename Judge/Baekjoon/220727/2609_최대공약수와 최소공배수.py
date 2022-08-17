# https://www.acmicpc.net/problem/2609
A, B = map(int, input().split())
a, b = A, B # a,b 로 정의를 다시 하는 이유는 A,B가 최소공배수 계산에 필요하기 때문

while b != 0: # b가 0이 되면 자동으로 와일문이 종료되도록
    a = a % b # a는 a % b의 몫. 정수이다.
    a, b = b, a # 최소공배수가 나올떄까지 수를 뒤집어서 계속 a%b를 해준다.
print(a) # 최대공약수
print(A*B//a) # 최소공배수 

# for i in range(min(A, B), 0, -1):
#     if A % i == 0 and B % i == 0:
#         print(i)
#         break

# for j in range(max(A, B), (A * B) + 1):
#     if j % A == 0 and j % B == 0:
#         print(j)
#         break

# for j in range(1, B + 1):
#     if B % j == 0:
#         measure_B.append(j)
# # print(measure_B)

# for i in measure_B:
#     for j in measure_A: 
#         if i == j:
#             measure.append(i)
# print(max(measure))