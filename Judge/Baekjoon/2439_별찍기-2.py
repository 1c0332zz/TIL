# https://www.acmicpc.net/problem/2439


n = int(input())
star = '*'
stars = ''
for i in range(n): # 반복문을 n개만큼 돌려야함.
    i <= n # i가 n보다 작거나 같을경우
    stars += star # 빈 변수안에 *을 더해줌
    print(stars.rjust(n)) # 바로 출력해주면서 오른쪽정렬함수(n)개 만큼 입력해줌.