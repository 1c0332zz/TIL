import json
a = ('''1회차 송강섭
Hello, Python!
1일차 파이썬 공부 중
2일차 파이썬 공부 중
3일차 파이썬 공부 중
4일차 파이썬 공부 중
5일차 파이썬 공부 중''')

with open("00.txt", 'w', encoding='utf-8') as f:
    f.write(a)
print(a)