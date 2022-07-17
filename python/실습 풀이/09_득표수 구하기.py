students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
counter = {}

for number in students:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
    
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

