# 서버 생성하기

1. 나의 현재 위치 정확하게 확인

```bash
Pong@DESKTOP-BHUR2DO MINGW64 ~/ # 이부분 확인
$
```

2. 가상환경 생성 (venv)

```bash
$ python -m venv [가상환경이름]
# ls -a로 확인해보면 만들어진 것 확인
```

3. 가상환경 실행

```bash
$ source [가상환경이름]/scripts/activate
# (가상환경 입력안에 들어왔는지 확인)
# source대신 .으로도 가능
```

4. django lts버전 설치

```bash
# pip list로 확인 후
$ pip install django==3.2.13
```

5. requirements.txt 생성 & gitignore 생성

```bash
$ pip freeze > requirements.txt
```

6. django 프로젝트 생성

```bash
# pip list로 확인 후
$ django-admin startproject [프로젝트이름] [시작경로] # (시작경로가 현재폴더면 .)
```

7. 앱 생성

```bash
# ls 명령어 입력 후 현재 경로에서 manage.py 파일 확인
$ python manage.py startapp [앱이름]
```

8. 앱 적용 및 만들기

1. settings.py의 INSTALLED_APPS=[ ] 안에 입력 [0]번째로

2. url = path([index], views.[함수명])
   * index = 요청 받은 주소
   * views.[함수명] = 응답 해줘야 하는 함수
   * from [앱이름] import views 

3. view = 종착역

   * def [함수명] (요청한 사람의 정보[보통 request]) : 

     return render(함수 객체[request], template_name, context[사용할 데이터, 딕셔너리])

4. templates 
   * 실제 내용을 보여주는데 사용되는 파일
   * app 폴더 안의 templates폴더
   * app_name/templates/

9. 서버 구동

```bash
$ python manage.py runserver
# http://localhost:8000/ 로 확인
```

11. pip install black(가상환경마다)

## 기타

* 이동

```bash
$ cd [폴더명]/
```

* 뒤로이동

```bash
$ cd ..
```

* 현재폴더

```bash
$ .
```

* 목록확인

```bash
$ ls
```

* 가상환경 끄는법

```bash
$ deactivate
ctrl + c
```

* 삭제 하는법

```bash
$ re -r [폴더]
```



URL = 순수이동 (마우스)

FROM = 입력을 받고

