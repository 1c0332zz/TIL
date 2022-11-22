# 정규식

>정규식은 텍스트에서 특정 글자나 단어, 패턴 등을 정확하고 유동적으로 표현하는 식입니다. 
>
>줄여서 regex나 regexp라고도 부르는데 정규식 처리기가 해석할 수 있도록 정해진 문법에 따라 사용하여야
>합니다

* 문자열 비교나 처리를 하기 위한 아주 똑똑한 와일드 카드 표현식

### 정규식의 이해

* 기호로 되어 있어 굉장히 효과적이지만 조금 어려움 
* 한 번 배우면 활용할 곳이 많음 
* 정규식은 그 자체로 하나의 언어입니다 
* 특수(marker) 문자로 이루어진 언어로 문자만을 사용해서 프로그래밍을 하는 개념 
* 축약된 ‘형식 언어’의 한 종류



---

### 정규식 코드

* ^ = 라인의 처음을 매칭
* $ = 라인의 끝을 매칭
* . = 임의의 문자를 매칭 (와일드 카드)
* \s = 공백 문자를 매칭
* \S = 공백이 아닌 문자를 매칭
* \* = 바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 표기함.
* *? = 바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
* \+ = 바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 표기함
* +? =바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
* [aeiou] = 명세된 집합 문자에 존재하는 단일 문자와 매칭. “a”, “e”, “i”, “o”, “u” 문자만 매칭되는 예제
* [a-z0-9]  = - 기호로 문자 범위를 명세할 수 있다. 소문자이거나 숫자인 단일 문자만 매칭되는 예제.
* ( ) = 괄호가 정규표현식에 추가될 때, 매칭을 무시한다. 하지만 findall()을 사용 할 때 전체 문자열보다 매칭된 문자열의 상세한 부속 문자열을 추출할 수 있게 한다.

### 정규식 모듈

* 정규식을 사용 전 “import re” 명령어로 라이브러리를 불러오기 
* re.search() 를 사용하면 find() 메소드를 쓴 것처럼 정규식에 매칭되는 문자열을 찾을 수 있음 
* re.findall() 을 사용하면 정규식에 맞는 문자열 추출 가능 (find() 와 slicing: var[5:10] 을 조합한 것과 유사)



### 텍스트에서 문자 패턴 찾기

> mbox-short.txt 파일에서 'From:'이라는 문자 패턴이 포함된 문장을 찾아 출력하는 프로그램입니다. 여기에서는 find() 메소드를 사용했습니다.

```python
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
```

* 정규표현식을 사용하기 위해서는 re(regular expression) 모듈을 import 해야 하고, re.search()가 find() 메소드와 같은 역할을 해주는 부분입니다.

```python
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)
```

### **텍스트에서 시작 패턴 찾기**

> 'From:'으로 시작하는 문장을 출력하는 프로그램입니다.

```python
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
```

* 정규표현식으로 표현하려면 다음과 같이 '^'라는 특수 문자를 사용하면 됩니다.

```python
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)
```

### **특수 문자를 활용한 문자 패턴 찾기**

* ^ : 문장의 시작을 의미
* . : 어떤 문자 한 글자
* \* : 앞의 문자가 여러 번 반복될 수 있음을 의미
* \+ : 앞의 문자가 1번 이상 나타남을 의미
* \S : 공백 문자가 아닌 한 개의 문자
  (\는 역슬래시와 같은 문자임)

따라서, 다음과 같은 문자열들은 모두 '^X.*:'라는 패턴을 통해 찾을 수 있습니다.

- X-Sieve: CMU Sieve 2.3
- X-DSPAM-Result: Innocent
- X-DSPAM-Confidence: 0.8475
- X-Content-Type-Message-Body: text/plain

그리고 다음과 같은 문자열들은 '^X-\S+:' 패턴으로 찾을 수 있으며,

- X-Sieve: CMU Sieve 2.3
- X-DSPAM-Result: Innocent

다음의 문자열은 'X-'와 ':' 사이에 공백 문자가 아닌 문자가 포함되지 않았기 때문에 '^X-\S+:' 패턴으로 찾을 수 없습니다.

- X-: Very short
- X-Plane is behind schedule: two weeks

### **패턴 추출하기**

* '[0-9]+'은 0부터 9까지 문자가 1번 이상 반복되는 패턴을 의미합니다. 이것은 즉, 정수로 이루어진 데이터를 찾는 것입니다. 또한 findall 메서드는 x라는 문자열에 존재하는 패턴('[0-9+]')을 모두 리스트로 저장해주는 기능을 합니다.

```python
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

# ['2', '19', '42']
```

* 'A','E','I','O','U'로 이루어진 패턴을 찾아 출력하는 코드이지만 x 문자열에 해당되는 패턴이 없어서 빈 리스트를 출력합니다. 여기서 알 수 있는 사실은 정규 표현식에서는 소문자와 대문자를 구분한다는 사실입니다.

```python
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[AEIOU]+',x)
print(y)

# [] (빈 리스트 출력)
```

### **탐욕적 방식의 패턴 찾기**

만약 다음 문장에서 '^F.+:'라는 패턴과 일치하는 부분을 찾는다면,

x = 'From: Using the : character'

- From:
- From: Using the :

두 가지 부분이 모두 패턴과 일치하게 됩니다.

> 이럴 때는 다음과 같이 가장 긴 패턴을 찾아주는데, 이것을 '탐욕적 방식의 패턴 찾기'라고 부릅니다. 일치하는 여러 패턴이 있을 경우 가장 긴 것을 선택한다는 의미입니다.

```python
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# ['From: Using the :']

# 반대로 비탐욕적 방식의 패턴은 ?를 붙여주면 가장 짧은것을 선택

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
```

### **원하는 부분만 추출하기**

*  '@' 문자 앞 뒤로 공백이 아닌 문자가 오는 문자열 패턴을 찾아줍니다. 따라서 다음과 같이 이메일 주소의 패턴이 추출됩니다.

```python
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y)
# ['stephen.marquard@uct.ac.za’]

# 이메일 주소만 추출
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)',x)
print(y)
```



### **이메일 호스트를 추출하는 다양한 방법**

```python
# 문자열 메소드를 사용하는 방법
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# 21
sppos = data.find(' ',atpos)
print(sppos)
# 31
host = data[atpos+1 : sppos]
print(host)
# uct.ac.za

# split 메소드를 활용하는 방법
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
# 'uct.ac.za'

# 정규식을 사용한 방법
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#  '^ '는 공백문자가 아닌 문자를 의미하며, '^'가 중간에 들어갈 경우 뒤에 오는 문자를 제외한 패턴을 의미
y = re.findall('@([^ ]*)',lin)
print(y)
# ['uct.ac.za']

# 더 정교한 패턴
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)
# ['uct.ac.za']
```

### 예외 문자

```python
# '$' 문자가 포함된 패턴을 찾을 때 역슬래시(\)를 사용
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)

# ['$10.00']
```

### 패턴 추출 및 최댓값 찾기

```python
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
```

