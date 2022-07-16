# 주어진 수 n이 3의 배수이면서 짝수인 경우 '참'을, 
# 거짓인 경우 '거짓'을 출력하시오.
# n=267 참 / n = 14 거짓
# if와 else

n=int(input())
if n % 3 == 0:
    print("참")
else:
    print("거짓")
print(n)