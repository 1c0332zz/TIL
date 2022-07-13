![1](README.assets/1.PNG)

## 파이썬이란?

* Easy to Iearn
  * 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지않음
    * 예시 : 변수에 별도의 타입지정이 필요 없음 (동적 타이핑 언어)
* 문법 표현이 매우 간결하여 프로그래밍 경험이 없어도 짧은 시간 내에 마스터할 수 있음
  * 예시 : 문장을 구분할 때 중괄호({,}) 대신 들여쓰기를 사용
* 인터프리터 언어(interpreter)
  * 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
  * 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음


![image-20220711204827468](README.assets/image-20220711204827468.png)

* 객체 지향 프로그래밍
  * 파이썬은 객체지향 언어이며, 모든것이 객체로 구현되어 있음
    * 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든것

## 파이썬 개발환경

* IDLE (Intergrated Development and Learning Environment)
  * 내장 프로그램으로 파이썬 설치 시 기본적으로 설치 → 인터프리터가 대화형 모드로 동작함
    * 여러 줄의 코드가 작성되는 경우 보조 프롬프트(...)가 사용됨
    * 프롬프트( >>>)에 코드를 작성하면 해당 코드가 실행됨
  * • Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반복 실행이 어려움
* IDE(예시 : Pycharm), Text editor(예시 : Visual Studio Code) 등에서 작성한 파이썬 스크립트 파일을 직접 실행

## 기초 문법

### 코드 스타일 가이드

* 코드를 '어떻게 작성할지'에 대한 가이드라인
* 파이썬에서 제안하는 스타일 가이드
  * [PEP8](https://www.python.org/dev/peps/pep-0008/ )
* 기업, 오픈소스 등에서 사용되는 스타일 가이드
  * [Google Style guide](https://google.github.io/styleguide/pyguide.html) 등



### 들여쓰기

- Space Sensitive
  - 문장을 구분할 때, 들여쓰기(indentation)>를 사용
  - 들여쓰기를 할 때는 4칸(space 4번) tap(1번)
    - 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용 → 혼용하면 안됨
      - Tab으로 들여쓰면 계속 탭으로 들여써야 함
      - 원칙적으로는 공백 (빈칸, space) 사용을 권장* PEP8 권장사항

### 변수

* 변수란?

  * 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위한 이름

    * 객체(object) : 숫자 문자 클래스 등 값을 가지고 있는 모든 것
      * 파이썬은 객체지향 언어이며, 모든것이 객체로 구현되어 있음

  * 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에,

    즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수' 라고 불림

  * 변수는 할당 연사자(=)를 통해 값을 **할당**(assignment)
  * type()
    * 변수에 할당된 값의 타입
  * id()
    * 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소 (* 이후, 자세히 다룰 예정)

![image-20220711205326585](README.assets/image-20220711205326585.png)

### 식별자

* 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름
* 규칙
  * 식별자의 이름은 영문 알파벳,언더스코어,숫자로 구성
  * 첫글자에 숫자가 올 수 없음
  * 길이제한이 없고, 대소문자를 구별
  * 다음의 키워드(keyword)는 예약어로 사용할 수 없음


![image-20220711205714735](README.assets/image-20220711205714735.png)

* 내장함수나 모듈 등의 이름으로도 만들면 안됨
  * 기존의 이름에 다른 값을 할당하게 되므로 더이상 동작하지 않음

### 사용자 입력

- input([prompt])
  - 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수
  - 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음
  - **반환값은 항상 문자열의 형태로 반환**

![image-20220711205828305](README.assets/image-20220711205828305.png)



### 주석

* 코드에 대한 설명
  * 중요한 점이나 다시 확인하여야 하는 부분을 표시
  * • 컴퓨터는 주석을 인식하지 않음 사용자만을 위한 것

* 가장 중요한 습관
  * 개발자에게 주석을 작성하는 습관은 매우 중요
  * 쉬운 이해와 코드의 분석 및 수정이 용이
    * 주석은 코드 실행에 영향을 미치지 않을 뿐만 아니라
    *  프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음
* 한 줄 주석
  * 주석으로 처리될 내용 앞에 ‘#’ 을 입력
    * • 한 줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷부분에 작성 할 수 있음


![image-20220711205949747](README.assets/image-20220711205949747.png)



## 파이썬 기본 자료형

![image-20220711210019685](README.assets/image-20220711210019685.png)

* 불린형(Boolean Type) → 참,거짓
* 수치형(Numeric Type)
  * int(정수, integer)
  * float(부동소수점, 실수, floating point number)
  * complex(복소수, complex number)
* 문자열(String Type)
* None



### None

* 파이썬 자료형 중 하나
* 파이썬에서는 값이 없음을 표현하기 위해 None 타입이 존재함
* 일반적으로 반환 값이 없는 함수에서 사용하기도 함

```python
print(type(None))
# <class 'NoneType'>
a = None
print(a)
# None
```



### 불린형(Boolean Type)

* True / False 값을 가진 타입은 bool 
* 비교/논리 연산을 수행함에 있어서 활용됨
* 다음은 모두 False로 변환
  * 0, 0.0, (), [], {}, '', None
* bool() 함수
  * 특정 데이터가 True인지 False인지 검증

```python
bool(0)  #False
bool('') #False
bool([]) #False
bool(1)  #True
bool(-1) #True
bool([1,2,3]) #True
```



### 논리 연산자

* 논리식을 판단하여 참(True)와 거짓(False)를 반환함

| 연산자  | 내용                           |
| ------- | ------------------------------ |
| A and B | A와 B 모두 True시, True        |
| A or B  | A와 B 모두 False시, False      |
| Not     | True를 False로, False를 True로 |

* and : 모두 참인 경우 참, 그렇지 않으면 거짓

| 논리연산자 and  | 내용  |
| --------------- | ----- |
| True and True   | True  |
| True and False  | False |
| False and True  | False |
| False and False | False |

* or : 둥 중 하나만 참이라도 참, 그렇지 않으면 거짓

| 논리연산자 or  | 내용  |
| -------------- | ----- |
| True or True   | True  |
| True or False  | True  |
| False or True  | True  |
| False or False | Fasle |

* not : 참 거짓의 반대의 결과

| 논리연산자 not | 내용  |
| -------------- | ----- |
| not True       | False |
| not False      | True  |

* 예제

```python
num = 100
num >= 100 and num % 3 == 1
# True
```



### 수치형(Numeric Type)

#### 정수(int)

* 모든 정수의 타입은 int



####  실수(Float)

* 정수가 아닌 모든 실수는 float 타입
* 부동소수점
  * 실수를 컴퓨터가 표현하는 방법 - 2진수(비트)로 숫자를 표현
  * 부동소수점에서 실수 연산 과정에서 발생 가능
    * 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의할 것
    * 매우 작은 수보다 작은지를 확인하거나 math모듈 활용

```python
# 아래는 참일까? 거짓일까?
3.14 - 3.02 == 0.12
3.14 - 3.02
# 0.1200000000000001

# 1. 임의의 작은 수
abs(a - b) <= 1e-10
# 2. math 모듈 활용
import math
math.isclose(a, b)
```

#### 복소수(Complex)

* 실수부와 허수부로 구성된 복소수는 모두 complex 타입
  * 허수부를 j로 표현

```python
a = 3+4j
type(a)
# <class 'complex'>
a.real
# 3.0
a.imag
# 4.0
```



#### 산술연산자

기본적인 사칙연산 및 수식 계산

| 연산자 | 내용     |
| ------ | -------- |
| +      | 덧셈     |
| -      | 뺄셈     |
| *      | 곱셈     |
| %      | 나머지   |
| /      | 나눗셈   |
| //     | 몫       |
| **     | 거듭제곱 |



#### 복합 연산자

* 연산과 할당이 함께 이뤄짐

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a **= b | a = a ** b |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |



#### 비교 연산자

* 값을 비교하며, True / False 값을 리턴함

| 연산자 | 내용                        |
| ------ | --------------------------- |
| <      | 미만                        |
| <=     | 이하                        |
| >      | 초과                        |
| =>     | 이상                        |
| ==     | 같음                        |
| !=     | 같지않음                    |
| is     | 객체 아이덴티티(OOP)        |
| is not | 객체 아이덴티티가 아닌 경우 |



### 문자열(String Type)

* 모든 문자열은 str 타입
* 문자열은 작은 따옴표(')나 큰 따옴표 (")를 활용하여 표기
  * 문자열을 묶을 때 동일한 문장부호를 활용
  * PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함


```python
print('hello')
# hello
print(type('hello'))
# <class 'str'>
```

#### 중첩따옴표

* 따옴표 안에 따옴표를 표현할 경우

```python
print("문자열 안에 '작은 따옴표'를 사용하려면 큰 따옴표로 묶는다.")
print('문자열 안에 "큰 따옴표"를 사용하려면 작은 따옴표로 묶는다.')
```

#### 삼중따옴표

* 작은 따옴표나 큰 따옴표를 삼중으로 사용

```python
print('''문자열 안에 '작은 따옴표'나
"큰 따옴표"를 사용할 수 있고
여러 줄을 사용할 때도 편리하다.''')
```

#### 인덱싱

* 인덱스를 통해 특정 값에 전근할 수 있음

```python
s = "abcdefghi"

s[0]     #a
s[1]     #b
s[-1]    #i
s[2:5]   #cde
s[2:5:2] #ce
s[5:2:-1]#fed
s[:3]    #abc
s[5:]    #fghi
s[::]    #abcdefghi’   #s[0:len(s):1]과 동일
s[::-1]  #ihgfedcba’   #s[-1:-(len(s)+1):-1]과 동일
```

#### 결합(Concatenation)

```python
'hello, ' + 'python!'
# 'hello, python!'
```

#### 반복(Repetition)

```python
'hi!' * 3
# 'hi!hi!hi!'
```

#### 포함(Membership)

```python
'a' in 'apple'
# True
'app' in 'apple'
# True
'b' in 'apple'
# False
```

#### 이스케이프

* 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\)를 활용하여 구분

| 예약문자 | 내용(의미)        |
| -------- | ----------------- |
| \n       | 줄 바꿈           |
| \t       | 탭                |
| \r       | 캐리지리턴        |
| \0       | 널(Null)          |
| \\\      | \                 |
| \\'      | 단일인용부호( ' ) |
| \\"      | 단일인용부호( " ) |

* 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\)를 활용하여 구분

```python
print('철수 \'안녕\'')
# 철수 '안녕'
print('이 다음은 엔터.\n그리고 탭\t탭')
# 이 다음은 엔터.
# 그리고 탭 탭
```

#### String Interpolation

* 문자열을 변수를 활용하여 만드는 법
  * %-formatting

```python
name = 'Kim'
score = 4.5
print('Hello, %s' % name)
print('내 성적은 %d' % score)
print('내 성적은 %f' % score)
# Hello, Kim
# 내 성적은 4
# 내 성적은 4.500000
```

* 문자열을 변수를 활용하여 만드는 법

```python
name = 'Kim'
score = 4.5
print(f'Hello, {name}! 성적은 {score}')
# Hello, Kim! 성적은 4.5
pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}')
# '원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368'
```



### 형 변환

#### 자료형 변환 (Typecasting)

* 파이썬에서 데이터 형태는 서로 변환할 수 있음
  * 암시적 형 변환(Implicit)
    * 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 하는 경우
      * bool
      * Numeric type (int, float, complex)

```python
True + 3
# 4
3 + 5.0
# 8.0
3 + 4j + 5
# (8+4j)
```

* 명시적 형 변환(Explicit)

  * 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환 하는 경우

  * int
    * str*, float ⇒ int
  * float
    * str*, int ⇒ float
  * str
    * int, float, list, tuple, dict ⇒ str

```python
# 문자열은 암시적 타입 변환이 되지 않음
'3' + 4
# TypeError: can only concatenate str (not "int") to str

# 명시적 타입 변환이 필요함
int('3') + 4
# 7

# 정수 형식이 아닌 경우 타입 변환할 수 없음
int('3.5') + 5
# ValueError: invalid literal for int() with base 10: '3.5'

float('3.5') + 5
# 8.5
```



### 컨테이너

* 컨테이너란?
  * 여러 개의 값을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음
    * 예시 : List, tuple
* 컨테이너의 분류
  * 순서가 있는 데이터 (Ordered) vs. 순서가 없는 데이터 (Unordered)
  * 순서가 있다 != 정렬되어 있다.


#### 컨테이너 분류

* 시퀀스
  * 문자열(immutable) : 문자들의 나열
  * 리스트 (mutable) : 변경 가능한 값들의 나열
  * 튜플 (immutable) : 변경 불가능한 값들의 나열
  * 레인지 (immutable) : 숫자의 나열
* 컬렉션/비시퀀스
  * 세트 (mutable) : 유일한 값들의 모음
  * 딕셔너리 (mutable) : 키-값들의 모음

#### 시퀀스형 주요 공통 연산자

| 연산             | 결과                                                       |
| ---------------- | ---------------------------------------------------------- |
| s[i]             | s 의 i 번째 항목, 0에서 시작합니다                         |
| s[i:j]           | s 의 i 에서 j 까지의 슬라이스                              |
| s[i:j:k]         | s 의 i 에서 j 까지 스텝 k 의 슬라이스                      |
| s + t            | s 와 t 의 이어 붙이기                                      |
| s * n 또는 n * s | s 를 그 자신에 n 번 더하는 것                              |
| x in s           | s 의 항목 중 하나가 x 와 같으면 True, 그 렇지 않으면 False |
| x not in s       | s 의 항목 중 하나가 x 와 같으면 False, 그 렇지 않으면 True |
| len(s)           | s 의 길이                                                  |
| min(s)           | s 의 가장 작은 항목                                        |
| max(s)           | s 의 가장 큰 항목                                          |



#### 리스트

* 변경 가능한 값들의 나열된 자료형
* 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
* 변경 가능하면(mutable), 반복 가능함(iterable)
* 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분
  * [ 0, 1, 2, 3, 4, 5 ]

* 리스트는 대괄호([]) 혹은 list() 를 통해 생성
* 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
  * 값에 대한 접근은 list[i]


##### 생성과 접근

* 리스트 생성

```python
# 생성
my_list = []
another_list = list()
type(my_list)
# <class 'list'>
type(another_list)
# <class 'list'>
```

* 접근과 변경

```python
# 값 접근
a = [1, 2, 3]
print(a[0])
# 1

# 값 변경
a[0] = '1'
print(a)
# ['1', 2, 3]
```

* 값 추가는 .append()를 활용하여 추가하고자 하는 값을 전달
* 값 삭제는 .pop()을 활용하여 삭제하고자 하는 인덱스를 전달

```python
even_numbers = [2, 4, 6, 8]
even_numbers.append(10)
even_numbers
# => [2, 4, 6, 8, 10]

even_numbers = [2, 4, 6, 8]
even_numbers.pop(0)
even_numbers
# => [4, 6, 8]
```

* 예제

```python
boxes = ['apple', 'banana']
len(boxes)
# 2
boxes[1]
# 'banana'
boxes[1][0]
# 'b'
```



### 튜플(Tuple)

* 불변한 값들의 나열
* 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
* 변경 불가능하며(immutable), 반복 가능함(iterable)
* 항상 소괄호 형태로 정의하며, 요소는 콤마로 구분
  * (0, 1, 3)

##### 생성과 접근

* 소괄호(()) 혹은 tuple()을 통해 생성
* 값에 대한 접근은 리스트와 동일하게 인덱스로 접근
  * 값 변경은 불가능하여 추가/삭제도 불가능함

```python
# 값 접근
a = (1, 2, 3, 1)
a[1]

# 값 변경 => 불가능
a[1] = ‘3’

TypeError Traceback (most recent call last)
1 # 값 변경 => 불가능 ---->
2 a[1] = '3’
TypeError: 'tuple' object does not support item assignment
```



### 레인지(Range)

* 숫자의 시퀀스를 나타내기 위해 사용
  * 기본형 : range(n)
    * 0부터 n-1까지의 숫자의 시퀀스
  * 범위 지정 : range(n, m)
    * n부터 m-1까지의 숫자의 시퀀스
  * 범위 및 스텝 지정 : range(n, m, s)
    * n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스
* 변경 불가능하며(immutable), 반복 가능함(iterable)
* range는 숫자의 시퀀스를 나타내기 위해 사용

```python
range(4)
# range(0, 4)
list(range(4))
# [0, 1, 2, 3]
type(range(4))
# <class 'range'>

#담겨있는 숫자를 확인하기 위하여
#리스트로 형변환
# * 실제 활용시에는 형변환 필요 없음
```



### 비시퀀스형 컨테이너(Associative Container)



#### 세트(set)

* 유일한 값들의 모음(collection)
* 순서가 없고 중복된 값이 없음.
  * 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능
* 변경 가능하며(mutable), 반복 가능함(iterable)
  * 단, 셋은 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음

* 중괄호({}) 혹은 set()을 통해 생성
  * 빈 Set를 만들기 위해서는 set()을 반드시 활용해야 함
* 순서가 없어 별도의 값에 접근할 수 없음



#### 딕셔너리(Dictionary)

* 키-값(key-value) 쌍으로 이뤄진 모음(collection)
  * 키(key)
    * 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함)

  * 값(values)
    * 어떠한 형태든 관계 없음

* 키와 값은 :로 구분 됩니다. 개별 요소는 ,로 구분됩니다
* 변경 가능하며(mutable), 반복 가능함(iterable)
  * 딕셔너리는 반복하면 키가 반환됩니다.


```python
students = {'홍길동': 30, '김철수': 25}
students['홍길동']
# 30
```

##### 생성

* key와 value가 쌍으로 이뤄진 자료구조
  * key는 변경 불가능한 데이터(immutable)만 활용 가능
    * string, integer, float, boolean, tuple, range
  * value는 모든 값으로 설정 가능 (List, Dictionary 등)

```python
dict_c = {[1, 2, 3]: 'hi’}
TypeError Traceback (most recent call last)
----> 1 dict_c = {[1, 2, 3]: 'hi’} 
TypeError: unhashable type: 'list'
```

```python
movie = {
'title': '설국열차',
'genres': ['SF', '액션', '드라마'],
'open_date': '2013-08-01',
'time': 126,
'adult': False,
}

movie['genres']
# ['SF', '액션', '드라마']

movie['actors’]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'actors'
```



##### 딕셔너리(Dictionary) 키-값 추가 및 변경

* 딕셔너리에 키와 값의 쌍을 추가할 수 있음
* 이미 해당하는 키가 있다면 기존 값이 변경

##### 딕셔너리(Dictionary) 키-값 추가 및 변경

* 키를 삭제하고자하면 .pop()을 활용하여 삭제하고자 하는 키를 전달

```python
students = {'홍길동': 30, '김철수': 25}
students.pop('홍길동')
students
# {'김철수': 25}
```

* 키가 없는 경우는 KeyError 발생

```python
students = {'홍길동': 30, '김철수': 25}
students.pop('jane')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'jane'
```

