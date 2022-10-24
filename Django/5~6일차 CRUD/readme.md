# CRUD

## Namespace

* URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
* app_name attribute를 작성해 URL namespace를 설정

```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
...,
]

# pages/urls.py
app_name = 'pages'
urlpatterns = [
...,
]


# URL 태그의 변화
{% url 'index' %}
# 이렇게 변경
{% url 'articles:index' %}
```

* app_name을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용해야 함. 그렇지 않으면 NoReverceMatch 에러가 발생
* “:” 연산자를 사용하여 지정 
  * 예를 들어, app_name이 articles이고 URL name이 index인 주소 참조는 articles:index가 됨

## Template namespace

*  pages app의 index url (http://127.0.0.1:8000/pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력됨

* Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾 을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함

*  바로 이 속성 값이 해당 경로를 활성화하고 있음

  ```python
  # settings.py
  TEMPLATES = [
      {
          ...,
          'APP_DIRS': True,
          ...
      },
  ]
  ```

  

### 디렉토리 생성을 통해 물리적인 이름공간 구분

* Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 app_name/templates/app_name/ 형태로 변경
* Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것

```bash
articles/
	templates/
		articles/
			index.html
			...
pages/
	templates/
		pages/
            index.html
            ...
```

### 템플릿 경로 변경

* 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정하기

```python
# articles/views.py
return render(request, 'articles/index.html')

# pages/views.py
return render(request, 'pages/index.html')
```



## Naming URL patterns

### Naming URL patterns의 필요성

* 만약 “index/”의 문자열 주소를 “new-index/”로 바꿔야 한다고 가정
* 그렇다면 “index/” 주소를 사용했던 모든 곳을 찾아서 변경해야 하는 번거로움이 발생함

### Naming URL patterns

* 이제는 링크에 URL을 직접 작성하는 것이 아니라 “path()” 함수의 name 인자를 정의해서 사용 • DTL의 Tag 중 하나인 URL 태그를 사용해서 “path()” 함수에 작성한 name을 사용할 수 있음 • 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음 • Django는 URL에 이름을 지정하는 방법을 제공함으로써 view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움