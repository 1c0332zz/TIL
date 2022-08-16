CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);


INSERT INTO classmates VALUES
('홍길동', 30, '서울'), 
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

SELECT * FROM classmates;
-- 홍길동|30|서울
-- 김철수|30|제주
-- 이호영|26|인천
-- 박민희|29|대구
-- 최혜영|28|전주

SELECT rowid, name FROM classmates;
-- 1|홍길동
-- 2|김철수
-- 3|이호영
-- 4|박민희
-- 5|최혜영

SELECT rowid, name FROM classmates LIMIT 2;
-- 1|홍길동
-- 2|김철수

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- 3|이호영

SELECT * FROM classmates WHERE address='서울';
-- 홍길동|30|서울

SELECT name FROM classmates WHERE age >= 30;
-- 홍길동
-- 김철수

SELECT DISTINCT age FROM classmates;
-- 30
-- 26
-- 29
-- 28

SELECT DISTINCT address FROM classmates;
-- 서울
-- 제주
-- 인천
-- 대구
-- 전주

DELETE FROM classmates WHERE rowid=5;
SELECT rowid, * FROM classmates;
-- 1|홍길동|30|서울
-- 2|김철수|30|제주
-- 3|이호영|26|인천
-- 4|박민희|29|대구
-- 최혜영 삭제댐

INSERT INTO classmates VALUES('송강섭', 31, '하남');
SELECT rowid, * FROM classmates;
-- 1|홍길동|30|서울
-- 2|김철수|30|제주
-- 3|이호영|26|인천
-- 4|박민희|29|대구
-- 5|송강섭|31|하남

-- 수정
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
SELECT rowid, * FROM classmates;

SELECT rowid, name FROM classmates LIMIT 100;
