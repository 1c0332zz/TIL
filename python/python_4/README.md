

# 데이터 구조

## 시퀀스(순서가 있는 데이터 구조)

### 문자열(String Type)

* 문자들의 나열
  * 모든 문자는 str 타입
* 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기
  *  문자열을 묶을 때 동일한 문장부호를 활용
  * PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

#### 문자열 탐색

- .find(x)
  - x의 첫 번째 위치를 반환. 없으면, -1을 반환함.

```python
print('apple'.find('p'))
# 1
print('apple'.find('k'))
# -1
```

- .index(x)
  - x의 첫 번째 위치를 반환. 없으면, 오류 발생

```python
print('apple'.index('p’))
# 1
'apple'.index('k')
# -------------------------------------------
# ValueError Traceback (most recent call last)
# ----> 1 'apple'.index('k')
# ValueError: substring not found
```

#### .split(sep=None, maxsplit=-1)

*  문자열을 특정한 단위로 나눠 리스트로 반환 
  * sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음.  
  * maxsplit이 -1인 경우에는 제한이 없음.

```python
print('a,b,c'.split('_’))
# ['a,b,c']
print('a b c'.split())
# ['a', 'b', 'c'
```

#### 'separator'.join([iterable])

* 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환
  * iterable에 문자열이 아닌 값이 있으면 TypeError 발생



### 리스트(list)

* 변경 가능한 값들의 나열된 자료형
* 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음 
* 변경 가능하며(mutable), 반복 가능함(iterable) 
* 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분 리스트(List) 정의 

```python
[ 0, 1, 2, 3, 4, 5 ]
```



| 문법                   | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| L.append(x)            | 리스트 마지막에 항목 x를 추가                                |
| L.insert(i, x)         | 리스트 인덱스 i에 항목 x를 삽입                              |
| L.remove(x)            | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 항목이 존재하지 않을 경우, ValueError |
| L.pop()                | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거        |
| L.pop(i)               | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
| L.extend(m)            | 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)   |
| L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| L.reverse()            | 리스트를 거꾸로 정렬                                         |
| L.sort()               | 리스트를 정렬 (매개변수 이용가능)                            |
| L.count(x)             | 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환             |



## 컬렉션(순서가 없는 데이터 구조)

### 세트(set)

* 유일한 값들의 모음(collection) 
* 순서가 없고 중복된 값이 없음. 
  * 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능 
* 변경 가능하며(mutable), 반복 가능함(iterable) 
  * 단, 세트는 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있



### 딕셔너리(Dictionary)

* 키-값(key-value) 쌍으로 이뤄진 모음(collection) 
  * 키(key)
    * 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함) 
  * 값(values) 
    * 어떠한 형태든 관계 없음
* 키와 값은 :로 구분 됩니다. 개별 요소는 ,로 구분됩니다. 
* 변경 가능하며(mutable), 반복 가능함(iterable) 
  * 딕셔너리는 반복하면 키가 반환됩니다.

```python
students = {'홍길동': 30, '김철수': 25}
students['홍길동']
# 30
```



* .get(key[,default]) 
  * key를 통해 value를 가져옴 
  * KeyError가 발생하지 않으며, default 값을 설정할 수 있음(기본: None)

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
print(my_dict.get('pineapple'))
# None
print(my_dict.get('apple'))
# 사과
print(my_dict.get('pineapple', 0))
# 0
```

