# Git 기본적인 순서 & 명렁어

## 1. 환경설정 하기

* Step 1 : 유저이름 설정

  ```git config --global user.name "name"```

  ![name](README.assets/name.PNG)

* Step 2 : 이메일 설정

  ```git config --global user.email "email"```

  ![Email](README.assets/Email.PNG)

* Step 3 : 정보 확인

  ```git config --list```

  ![list](README.assets/list.PNG)

## 2. Github에 처음 코드 업로드하기

1. 초기화

   ```git init```

   

2. 추가할 파일 더하기

   ```git add .``` OR ```git add 파일명 ```

   

3. 상태 확인

   ```git status```

   

4.  버전만들기 (히스토리 필수)

   ```git commit -m "test"```

   

5. GitHub Repository랑 내 로컬이랑 연결

   ```git remote add origin https://github.com/[GitHubUsername]/[Repositoryname].git```

   

6. GitHub로 올리기

   ```git push origin master```

## 3. GitHub에 계속 업데이트 하는법

1. 추가할 파일 더하기

   ```git add .``` OR ```git add [파일명] ```

   

2. 상태 확인

   ```git status```

   

3.  버전만들기 (히스토리 필수)

   ```git commit -m "[test]"```

   

4. GitHub로 올리기

   ```git push origin master```



* TIL에 계속 업로드 할 때, 이 스텝만 계속 반복하면 됨.



## GitHub로 협업하기

1. Github에서 Clone(복제)할 주소 입력

   `git clone [원격저장소 주소] [Repository]` 

2. 수정 및 추가를 위한 내 브랜치 생성

   `git checkout -b [branch]`

3. 내 브랜치 에 버전 업데이트

   `git add .`

   `git commit -m "  "`

4. 원격 저장소에 내 브랜치 업데이트

   `git push origing master <- [원격저장소] [브랜치]`

5. Github 저장소에서 Pull Request 실행

6. 소유자가 master에 브랜치를 병합

7. 브랜치 삭제

8. 다시 버전 가져오기(pull)

   `git checkout origin master <- [원격저장소] [브랜치]`