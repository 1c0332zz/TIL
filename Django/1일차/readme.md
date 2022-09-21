# 서버 생성하기

1. 나의 현재 위치 정확하게 확인

```bash
Pong@DESKTOP-BHUR2DO MINGW64 ~/ # 이부분 확인
$
```

2. 가상환경 설정 (venv)

```bash
$ python -m venv [가상환경 입력]
# ls -a로 확인해보면 만들어진 것 확인
```

3. 스크립트 발동 (가상환경 만들기)

```bash
$ source server-venv/scripts/activate
# (가상환경 입력안에 들어왔는지 확인)
```

4. Django install

```bash
# pip list로 확인 후
$ pip install django==3.2.13
```

5. 프로젝트 시작

```bash
# pip list로 확인 후
$ django-admin startproject [프로젝트이름] [시작경로] # (시작경로가 현재폴더면 .)
```

6. 서버 구동

```bash
$ python manage.py runserver
```

7. http://localhost:8000/ 로 확인



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
```

* 삭제 하는법

```bash
$ re -r [폴더]
```

