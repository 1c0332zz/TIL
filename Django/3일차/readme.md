## Variable routing

### Variable routing의 필요성

* URL 주소를 변수로 사용하는 것을 의미 
* URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음 
* 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

### Variable routing 작성

* 변수는 “<>”에 정의하며 view 함수의 인자로 할당됨 
* 기본 타입은 string이며 5가지 타입으로 명시할 수 있음 
  	1. str 
      * `/` 를 제외하고 비어 있지 않은 모든 문자열 
      * 작성하지 않을 경우 기본 값 
  	2. int 
      * 0 또는 양의 정수와 매치 
  	3. slug 
  	4. uuid 
  	5. path

```python
# urls.py

urlpatterns = [
	...,
	# path('hello/<str:name>/', views.hello),
	path('hello/<name>/', views.hello),
]
```

### View 함수 작성

* variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음

```python
# articles/views.py
def hello(request, name):
	context = {
	'name': name,
	}
return render(request, 'hello.html', context)
```

```html
<!-- articles/templates/hello.html -->

{% extends 'base.html' %}

{% block content %}
	<h1>만나서 반가워요 {{ name }}님!</h1>
{% endblock %}
```

## Django Template

* “데이터 표현을 제어하는 도구이자 표현에 관련된 로직” 
* Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입 
* Template System의 기본 목표를 숙지 
* Django Template System 
  * 데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당

### Django Template Language (DTL)

* Django template에서 사용하는 built-in template system 
* 조건, 반복, 변수 치환, 필터 등의 기능을 제공 
  * Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 Python 코드로 실행되는 것이 아님 
  * Django 템플릿 시스템은 단순히 Python이 HTML에 포함 된 것이 아니니 주의 
* 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심할 것

## Template inheritance

### 템플릿 상속

* 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤 
* 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 ‘skeleton’ 템플릿을 만들 수 있음 
* 만약 모든 템플릿에 부트스트랩을 적용하려면 어떻게 해야 할까? 
  * 모든 템플릿에 부트스트랩 CDN을 작성해야 할까?

### 템플릿 상속에 관련된 태그

```html
{% extends '' %}
```

* 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림 

  ❖ 반드시 템플릿 최상단에 작성 되어야 함 (즉, 2개 이상 사용할 수 없음) 

* 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의 

* 즉, 하위 템플릿이 채울 수 있는 공간 

* 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있음

```html
{% block content %}{% endblock content %}
```

#### 예시

* base라는 이름의 skeleton 템플릿을 작성 
* Bootstrap CDN 작성

```html
<!-- articles/templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- bootstrap CDN 작성 -->
<title>Document</title>
</head>
<body>
	{% block content %}
	{% endblock content %}
	<!-- bootstrap CDN 작성 -->
</body>
</html>
```

* index 템플릿에서 base 템플릿을 상속받음 
* Bootstrap이 적용되었는지 확인

```html
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
	<h1>만나서 반가워요!</h1>
	<a href="/greeting/">greeting</a>
	<a href="/dinner/">dinner</a>
{% endblock content %}
```

* base.html의 위치를 앱 안의 template 디렉토리가 아닌 프로젝트 최상단의 templates 디렉토리 안에 위치하고 싶다면 어떻게 해야 할까? 
* 기본 template 경로가 아닌 다른 경로를 추가하기위해 다음과 같은 코드를 작성

```python
# settings.py
TEMPLATES = [
	{
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [BASE_DIR / 'templates',], # <- 이부분 수정
			'APP_DIRS': True,
			'OPTIONS': {
				'context_processors': [
					'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
      			  ],		
        	},
    },
```

* app_name/templates/ 디렉토리 경로 외 추가 경로를 설정한 것 
* base.html의 위치를 다음과 같이 이동 후 상속에 문제가 없는지 확인

```python
articles/
firstpjt/
templates/
	base.html
```

### [참고]BASE_DIR

```python
# settings.py

BASE_DIR = Path(__file__).resolve().parent.parent
```

* settings.py에서 특정 경로를 절대 경로로 편하게 작성할 수 있도록 Django에서 미리 지정해둔 경로 값 
* “객체 지향 파일 시스템 경로” 
  * 운영체제별로 파일 경로 표기법이 다르기 때문에 어떤 운영체제에서 실행되더라도 각 운영체제 표기법에 맞게 해석될 수 있도록 하기 위해 사용 
  * 자세한 내용은 공식문서에서 확인하기
  * https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib