# # 입력을 받습니다.
# string = input("입력> ")

# #출력합니다.
# print("자료:",string)
# print("자료형:", type(string))

# # 입력을 받습니다.
# string = input("입력> ")
# p = int(string) # 2줄로 설명해놨지만 1줄로 줄이고 싶다면 p = int(input("입력> ")) 이렇게 하면된다~
# # # 출력합니다.
# print("입력 + 100:", p + 100)

# string_a = input("입력A> ")
# int_a = int(string_a)

# string_b = input("입력B> ")
# int_b = int(string_b)

# print("문자열 자료:", string_a + string_b)
# print("숫자 자료:", int_a + int_b)

#===========================================================

#inch단위를 cm단위로 변환

# # 숫자를 입력합니다.
# raw_input = input("inch 단위의 숫자를 입혁해주세요: ")

# # 입력받은 데이터를 숫자 자료형으로 변경하고, cm단위로 변경합니다.
# inch = int(raw_input)
# cm = inch * 2.54

# # 출력합니다.
# print(inch, "inch는 cm 단위로", cm, "cm입니다.")

#===========================================================

#원의 둘레 및 넓이 구하기
str_input = input("원의 반지름> ")
num_input = int(str_input)

print("반지름:", num_input)
print("둘레:", 2 * 3.14 * num_input)
print("넓이:", 3.14 * num_input * num_input)
