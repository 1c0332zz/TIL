# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# numbers = input().split()
# print(sum(numbers))


# map 활용 숫자 쪼개서 입력받기.
numbers = map(int, input().split()) #split과 map 함수를 활용해서 숫자를 다중 입력
# map 함수는 map(적용할 함수, 적용할 값)으로 활용
print(sum(numbers))


# 원인 : input은 문자열으로만 불러온다. 이를 int로 변형해 주어야하는데, 그냥 int로 감싸면 에러가 일어난다.
#        이럴때 map함수를 이용해 숫자를 다중 입력해주면 된다.