

## WHERE

* Table users 생성

```sqlite
CREATE TABLE users (
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	age INTEGER NOT NULL,
	country TEXT NOT NULL,
	phone TEXT NOT NULL,
	balance INTEGER NOT NULL
);
```

* csv파일 정보를 테이블에 적용하기

```sqlite
sqlite> .mode csv
sqlite> .import users.csv isers
sqlite> .tables
classmates examples users
```

* 특정 조건으로 데이터 조회하기

```sqlite
SELECT * FROM 테이블이름 WHERE 조건;
```

