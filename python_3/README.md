## 함수 기초

* 함수(Function)
  * 특정한 기능을 하는 코드의 조각(묶음)
  * 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용
* 사용자 함수(Custom Function)
  * 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능
* 내장함수(Built-in Function) 활용
* pstdev 함수 (파이썬 표준 라이브러리 - statistics)



#### 함수 기본 구조

* 선언과 호출(define & call)
  * 함수의 선언은 def 키워드를 활용함
  * 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함
  * 함수는 parameter를 넘겨줄 수 있음
  * 함수는 동작 후에 return을 통해 결과값을 전달함
  * 함수는 함수명()으로 호출
* 입력(Input)
* 범위(Scope)
* 결과값(Output)

## 함수의 결과값(Output)

* 함수는 반드시 값을 하나만 return한다.
  * 명시적인 return이 없는 경우에도 None을 반환한다.
* 함수는 return과 동시에 실행이 종료된다.

## 함수의 입력(Input)

* Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
* Argument : 함수를 호출 할 때, 넣어주는 값
  * 함수 호출 시 함수의 parameter를 통해 전달되는 값
  * Argument는 소괄호 안에 할당 func_name(argument)
    * 필수 Argument : 반드시 전달되어야 하는 argument
    * 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달
    * 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

## 함수의 범위(Scope)

* 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
* scope
  * global scope : 코드 어디에서든 참조할 수 있는 공간
  * local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
* variable
  * global variable : global scope에 정의된 변수
  * local variable : local scope에 정의된 변수
* 객체는 각자의 수명주기(lifecycle)가 존재
  * built-in scope
    * 파이썬이 실행된 이후부터 영원히 유지
  * global scope
    * 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  * local scope
    * 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

## 함수 응용

* 파이썬 인터프리터에는 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음
  * [내장 함수](https://docs.python.org/ko/3/library/functions.html)
* map(function, iterable)
  * 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환
  * 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때