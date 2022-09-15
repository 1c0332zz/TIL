# 문법과 자료형

JavaScript는 **대소문자를 구별**

JavaScript에서는 명령을 [명령문(statement) (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Statement)이라고 부르며, 세미콜론(;)으로 구분

## [선언](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#선언)

[`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var)

변수를 선언. 추가로 동시에 값을 초기화.

[`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let)

블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화.

[`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const)

블록 스코프 읽기 전용 상수를 선언.



### [변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수)

- `var x = 42`와 같이 [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var) 키워드로 변수를 선언할 수 있습니다. 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있습니다.
- `let y = 13`와 같이 [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 혹은 [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let) 키워드로 변수를 선언할 수 있습니다. 이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있습니다. 아래 [변수 스코프](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_스코프)를 참고하세요.