# MDN 문서 복습

## HTML

**HTML**(HyperText Markup Language)은 웹을 이루는 가장 기초적인 구성 요소로, 웹 콘텐츠의 의미와 구조를 정의할 때 사용합니다. HTML 이외의 다른 기술은 일반적으로 웹 페이지의 모양/표현 ([CSS](https://developer.mozilla.org/ko/docs/Web/CSS)), 또는 기능/동작 ([JavaScript](https://developer.mozilla.org/ko/docs/Web/JavaScript))을 설명하는 데 사용됩니다.

### Hypertext(하이퍼텍스트)

웹 페이지를 다른 페이지로 연결하는 링크

* 링크는 웹의 근본적인 속성
* 인터넷에 자료를 올리고 다른 사람이 만든 페이지로 링크

### 마크업 요소

HTML은 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위해 "마크업"을 사용

* [`head`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/head)
* [`title`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title)
* [`body`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/body)
* [`header`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/header)
* [`footer`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/footer)
* [`article`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/article)
* [`section`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/section)
* [`p`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p)
* [`div`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div)
* [`span`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/span)
* [`img`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img)
* [`aside`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/aside)
* [`audio`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/audio)
* [`canvas`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/canvas)
* [`datalist`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/datalist)
* [`details`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/details)
* [`embed`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/embed)
* [`nav`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/nav)
* [`output`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/output)
* [`progress`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/progress)
* [`Video`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video)
* [`ul`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul)
* [`ol`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol)
* [`li`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li)

### 태그

* 문서의 다른 텍스트와 구분하는데 사용합니다.
  * "`<`", 태그 이름, "`>`"
* 태그 안의 요소 이름은 대소문자를 구분하지 않습니다.
  * Ex) `<title>`요소는 `<Title>`, `<TITLE>` 그 외 기타 모든 방법으로 작성 가능



## 그래서 HTML이 무엇일까?

* HTML 은 컨텐츠의 구조를 정의하는 마크업 언어
* HTML은 컨텐츠의 서로 다른 부분들을 씌우거나(wrap) 감싸서(enclose) 다른 형식으로 보이게하거나 특정한 방식으로 동작하도록 하는 일련의 **요소([elements](https://developer.mozilla.org/ko/docs/Glossary/Element))**로 이루어져 있습니다.
* [tags](https://developer.mozilla.org/ko/docs/Glossary/Tag)로 감싸는 것으로 단어나 이미지를 다른 어딘가로 하이퍼링크(hyperlink)하거나 단어들을 이탤릭체로 표시하고 글씨체를 크게 또는 작게 만드는 등의 일을 할 수 있습니다. 
* 예를 들어, 다음과 같은 컨텐츠에 대해

```html
내 고양이는 고약해
<!-- 한 줄의 문장이 독립적인 구문이길 원한다면, 문단 태그(paragraph tags)로 둘러쌈으로해서 그것이 하나의 문단임을 명시할 수 있습니다 -->

<p>내 고양이는 고약해</p>
```

### HTML의 요소 분석

*  요소의 주요 부분
  1. **여는 태그(opening tag)**: 요소의 이름으로 구성되고 (여기에서는 p), 여닫는 꺾쇠괄호로 감싸집니다. 이것은 요소가 시작되는 곳, 또는 효과를 시작하는 곳임을 나타냅니다.
  2. **닫는 태그(closing tag)**: 여는 태그와 같지만, 요소의 이름 앞에 전방향 슬래시가 포함된다는 점이 다릅니다. 이것은 요소의 끝을 나타냅니다. 
  3. **컨텐츠(content)**: 이것은 요소의 내용(content)으로 이 예제에서는 그냥 텍스트입니다.
  4. **요소(element)**: 요소는 여는 태그와 닫는 태그, 그리고 컨텐츠로 이루어집니다.

### 요소  속성

* 속성은 실제 컨텐츠로 표시되길 원하지 않는 추가적인 정보를 담고 있습니다.(눈에 보이지 않는것) 
* 이 예제에서, class 속성을 이용해 나중에 해당 요소를 특정해 스타일이나 다른 정보를 설정할 때 사용할 수 있는 식별자를 지정할 수 있습니다.

* 속성이 항상 가져야 하는 것:
  1. 요소 이름 (또는 요소가 하나 이상 속성을 이미 가지고 있다면 이전 속성)과 속성 사이에 공백이 있어야 합니다.
  2. 속성 이름 뒤에는 등호(=)가 와야 합니다.
  3. 속성 값의 앞 뒤에 열고 닫는 인용부호(" 또는 ')가 있어야 합니다.

### 요소 중첩

*  요소를 다른 요소의 안에 놓을 수 있습니다 
  * **중첩(nesting)**
* 우리 고양이는 **아주** 고약하다라고 표시하길 원한다면, 단어를 강조하는 용도로 사용하는[`strong`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/strong) 요소로 "아주"를 감싸면 됩니다:

```html
<p>내 고양이는 <strong>아주</strong> 고약해</p>
```

### 빈 요소

* 어떤 요소들은 내용을 갖지 않습니다
  * 이것을 **빈 요소(empty elements)**라고 합니다.
* [`img`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img) 요소는 이미 우리 HTML 코드에 있습니다.

```html
<img src="images/firefox-icon.png" alt="My test image"
```

* 이미지 요소는 효과를 주기 위해 컨텐츠를 감싸지 않기 때문에 `<\img>`태그가 없습니다.
* 이 요소의 목적은 HTML 페이지에서 이미지가 나타날 위치에 이미지를 끼워 넣는 것입니다.
* alt=는 위에 설명한 속성입니다.

### HTML 문서 해부

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

살펴볼 것들:

- `<!DOCTYPE html>` : doctype. 아주 오래전 HTML 이 막 나왔을 때 (1991년 2월쯤), doctype은 (자동 오류 확인이나 다른 유용한 것을 의미하는) good HTML로 인정받기 위해 HTML 페이지가 따라야 할 일련의 규칙으로의 연결통로로써 작동하는 것을 의미하였습니다. 하지만, 최근에는 아무도 그런 것들에 대해 신경쓰지 않으며 그저 모든 것이 올바르게 동작하게 하기 위해 포함되어야 할 역사적인 유물일 뿐입니다. 지금은, 그게 알아야 할 전부 입니다.
- `<html></html>` : [`html`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/html) 요소. 이 요소는 페이지 전체의 컨텐츠를 감싸며, **루트(root)** 요소라고도 합니다.
- `<head></head>` : [`head`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/head) 요소. 이 요소는 **HTML 페이지에 포함되어 있는 모든 것들(여러분의 페이지를 조회하는 사람들에게 보여주지 않을 컨텐츠)의 컨테이너 역할**을 합니다. 여기에는 [keywords (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Keyword)와 검색 결과에 표시되길 원하는 페이지 설명, 컨텐츠를 꾸미기 위한 `CSS`, `문자 집합 선언` 등과 같은 것들이 포함됩니다.
- `<body></body>` : [`body`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/body) 요소. 이것은 **페이지에 방문한 모든 웹 사용자들에게 보여주길 원하는 *모든* 컨텐트**를 담고 있으며, 그것이 텍스트일 수도, 이미지, 비디오, 게임, 플레이할 수 있는 오디오 트랙이나 다른 무엇이든 될 수 있습니다.
- `<meta charset="utf-8">` : 이 요소는 문서가 사용해야 할 문자 집합을 utf-8으로 설정합니다(utf-8 문자 집합에는 인간의 방대한 주류 기록언어에 있는 대부분의 문자가 포함되어 있습니다). 본질적으로 여러분이 사용할 수 있는 어떠한 문자 컨텐트도 다룰 수 있습니다. 이 문자 집합을 설정하지 않을 이유가 없으며, 그렇게 설정하면 나중에 발생할 수 있는 일부 문제를 피할 수 있습니다.
- `<title></title>` — [`title`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title) 요소. 이 요소는 **페이지의 제목**을 설정하는 것으로 페이지가 로드되는 브라우저의 탭에 이 제목이 표시됩니다. 이 요소는 **북마크**나 **즐겨찾기**에서 페이지를 설명하는 것으로도 사용됩니다.

### 이미지

```html
<img src="images/firefox-icon.png" alt="My test image">
```

이 요소는 이미지가 나타나야 할 위치에 이미지를 끼워 넣습니다. 이미지 파일의 경로를 포함하는 `src` (source) 속성을 통해 이러한 일을 합니다.

`alt` (alternative) 속성도 존재합니다. — 이 속성에는 다음과 같은 이유로 이미지를 볼 수 없는 사용자들을 위한 설명문(descriptive text)을 지정할 수 있습니다.:

1. 시각 장애자인 경우. 시각 장애가 심한 사용자들은 alt 텍스트(대체 텍스트)를 읽어주는 스크린 리더라는 도구를 자주 사용합니다.
2. 무언가 잘못되어서 이미지를 표시할 수 없는 경우. 예를 들면, `src` 속성 안의 경로를 일부러 틀리게 변경해보세요. 저장한 후에 페이지를 다시 열면, 이미지가 표시되어야할 위치에 My test image 을 보게 될 것입니다.

### 문자 나타내기

제목 요소는 내용의 특정 부분이 제목 또는 내용의 하위 제목임을 구체화 할 수 있게 해줍니다. 책에 중심 제목이 있고 그 다음 각각의 장에 제목을 가지고, 그리고 그 안에 부제가 있는 것과 같은 방식으로 HTML 문서도 제목들을 갖습니다. HTML 은 여섯 단계의 제목을 갖고, [`h1`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Heading_Elements)–[`h6`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Heading_Elements) 여러분은 아마 3-4 만을 주로 사용하게 될겁니다:

```html
<h1>My main title</h1>
<h2>My top level heading</h2>
<h3>My subheading</h3>
<h4>My sub-subheading</h4>
```

### 문단

[<p\>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p) 요소는 문자의 문단을 포함하기 위한 것입니다; 일반적인 문자 내용을 나타낼 때 많이 사용하게 될 것입니다:

```html
<p>This is a single paragraph</p>
```

### 목록

많은 웹의 내용은 목록이기 때문에, HTML은 이것을 위한 특별한 요소를 가지고 있습니다. 목록을 나타내는 것은 항상 최소 두 개의 요소로 구성됩니다. 가장 일반적인 목록의 종류는 순서가 있는 것과 순서 없는 것이 있습니다.

1. **순서 없는 목록은** 쇼핑 목록과 같이 항목의 순서에 관계가 없는 목록을 위한 것입니다. [`ul`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul) 요소로 둘러 쌓여 있습니다.
2. **순서 있는 리스트**는 조리법처럼 항목의 순서가 중요한 목록을 위한 것입니다. [`ol`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol) 요소로 둘러 쌓여 있습니다.

목록의 각 항목은 [`li`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li) (목록 항목) 요소 안에 놓여야 합니다.

아래 문단의 한 부분을 목록으로 분리하길 원한다면:

```html
<p>At Mozilla, we’re a global community of technologists, thinkers, and builders working together ... </p>

<p>At Mozilla, we’re a global community of</p>

<ul>
  <li>technologists</li>
  <li>thinkers</li>
  <li>builders</li>
</ul>

<p>working together ... </p>
```

### 연결

*[a](https://developer.mozilla.org/ko/docs/Web/HTML/Element/a)* 는 "anchor" 의 약자입니다. 문장 안의 어떤 단어를 링크로 만들기 위해, 아래의 순서를 따르시면 됩니다:

```html
<!--문자를 <a>요소로 감싼다.-->
<a>Mozilla Manifesto</a>

<!-- <a>요소에 href속성을 준다 -->
<a href="">Mozilla Manifesto</a>

<!-- 연결하길 원하는 웹 주소를 채운다 -->
<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>
```

