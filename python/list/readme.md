# 리스트

## 1) 배열

여러 데이터들이 연속된 메모리 공간에 저장되어 있는 자료구조

* 인덱스(Index)를 통해 데이터에 빠르게 접근 
* 배열의 길이는 변경 불가능 → 길이를 변경하고 싶다면 새로 생성 
* 데이터 타입은 고정

![image-20220804213803971](readme.assets/image-20220804213803971.png)

## 2) 연결 리스트 (Linked List) 

데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조 

* 맨 처음 노드부터 순차적으로 탐색 
* 연결리스트의 길이 자유롭게 변경 가능 → 삽입, 삭제가 편리 
* 다양한 데이터 타입 저장 
* 데이터가 메모리에 연속적으로 저장되지 않음

![image-20220804213752085](readme.assets/image-20220804213752085.png)



![image-20220804213819766](readme.assets/image-20220804213819766.png)



## 파이썬의 리스트

### 메서드

1. .append(원소)

* 리스트 맨 끝에 새로운 원소 삽입

```python
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
# [1, 2, 3, 4, 5, 6]

a = [1, 2, 3, 4, 5]
a.append("a", "b")
print(a)
# [1, 2, 3, 4, 5, ['a', 'b']]
```

2. .pop(인덱스)

* 특정 인덱스에 있는 원소를 삭제 및 반환

```python
a = [1, 2, 3, 4, 5]
b = a.pop()

print(a)
print(b)

# [1, 2, 3, 4]
# 5
```

3. count(원소)

* 리스트에서 해당 원소의 개수를 반환

```python
a = [1, 2, 2, 3, 3, 3]

print(a.count(2))
# 2
```

4. .index(원소)

* 리스트에서 처음으로 원소가 등장하는 인덱스 반환

```python
a = [1, 2, 3, 4, 5]

print(a.index(2))
# 1
```

5) .sort()

* 리스트를 오름차순으로 정렬
* reverse = True 옵션을 통해 내림차순으로 정렬 가능

```python
a = [5, 2, 4, 0, -1]
a.sort()

print(a)
# [-1, 0, 2, 4, 5]

a = [5, 2, 4, 0, -1]
a.sort(reverse=True)

print(a)
# [5, 4, 2, 0, -1]
```

6. .reverse()

* 리스트의 원소들의 순서를 거꾸로 뒤집기

```python
a = [1, 2, 3, 4, 5]
a.reverse()

print(a)
# [5, 4, 3, 2, 1]
```



### 내장함수

1. len

* 리스트의 길이(원소의 개수)를 반환

```python
a = [1, 2, 3, 4, 5]

print(len(a))
# 5
```

2. sum

* 리스트의 모든 원소의 합을 반환

```python
a = [1, 2, 3, 4, 5]

print(sum(a))
# 15
```

3. max

* 리스트의 원소 중 최대값을 반환

```python
a = [1, 2, 3, 4, 5]

print(max(a))
# 5
```

4. min

* 리스트의 원소 중 최소값을 반환

```python
a = [1, 2, 3, 4, 5]

print(min(a))
# 1
```

5. sorted

* 오름차순으로 정렬된 새로운 리스트 반환, 원본 리스트는 변화 없음

```python
a = [5, 2, -1, 0, 1]
b = sorted(a)
c = sorted(a, reverse=True)

print(a) # 원본			[5, 2, -1, 0, 1]
print(b) # 오른차순 정렬	  [-1, 0, 1, 2, 5]
print(c) # 내림차순 정렬	  [5, 2, 1, 0, -1]
```

6. reversed

* 리스트의 순서를 거꾸로 뒤집은 새로운 객체 반환, 원본 리스트는 변화 없음

```python
a = [1, 2, 3, 4, 5]
b = reversed(a)
c = list(reversed(a))

print(a) # 원본			[1, 2, 3, 4, 5]
print(b) # reversed(a)	  <list_reverseiterator object at 0x000000298CE25E740>	  
print(c) # list(reversed(a)) [5, 4, 3, 2, 1]
```



## 리스트 컴프리헨션(List comprehension)

* 리스트 컴프리헨션(리스트 내포)란, 코드 한 줄만으로 새로운 리스트를 만드는 방법이다.

```python
number = []
for i in range(5):
    numbers.append(i)

print(numbers)
# [0, 1, 2, 3, 4]
# 아래와 같이 변경 할 수 있다.

numbers = [i for i in range(5)]

print(numbers)
# [0, 1, 2, 3, 4]

# if문으로 필터링도 가능
odd_numbers = [i for i in range(10) if i % 2 == 1]

print(odd_numbers)
# [1, 3, 5, 7 ,9]
```



