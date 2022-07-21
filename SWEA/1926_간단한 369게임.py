import sys
sys.stdin = open("1926_input.txt", "r")


T = int(input())
clap = ['3', '6', '9'] # 369를 표시해줄 변수?
for number in range(1, T + 1): # 이렇게 해놓으면 1부터 100까지 주르륵 나열
    count = 0 # 369가 뜨면 +1를 해줘서 카운트 개수당 -를 표시해줄 변수!
    for i in str(number): # 만약 123이 들어오면 123안에 3,6,9가 있는지 문자열로 바꿔서 조건문으로 이동시켜서 369의 개수만큼 +1을 해주어 -를 표시해주기 위함!
        if i in clap:
            count += 1
    if count > 0:
        number = '-' * count
    print(number, end=' ')
