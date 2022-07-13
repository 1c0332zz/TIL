def foo():
    return 1, 2

result = foo()
print(result, type(result)) # (1, 2) <class 'tuple'> 

def no():
    a = 1

result = no() 
print(result, type(result)) # None <class 'NoneType'>


# print 함수는 
# 출력을 해주고, return 값은 없습니다. (None)
a = print('hi')
print(a, type(a)) # None <class 'NoneType'>

a = 'hi'
print(a)
