CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT,
    role_id INT
);

-- 1은 admin, 2는 staff, 3은 student
INSERT INTO users VALUES
    (1, '관리자', 1),
    (2, '김철수', 2),
    (3, '이영희', 2);

CREATE TABLE role (
    id INT PRIMARY KEY,
    title TEXT
);

INSERT INTO role VALUES
    (1, 'admin'),
    (2, 'staff'),
    (3, 'student');

CREATE TABLE articles (
    id INT PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INT
);

INSERT INTO articles VALUES
    (1, '1번글', '111', 1),
    (2, '2번글', '222', 2),
    (3, '3번글', '333', 1),
    (4, '4번글', '444', NULL);

-- 확인
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;

-- INNER JOIN
-- A와 B테이블에서 값이 일치하는 것들만
SELECT *
FROM users JOIN role
    ON users.role_id = role.id;

-- 스태프(2)만 출력
SELECT *
FROM users JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;

-- 이름이 내림차순으로 출력하세요.
SELECT *
FROM users JOIN role
    ON users.role_id = role.id
ORDER BY users.name DESC;

-- LEFT OUTER JOIN
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;

-- NULL뺸것
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL

-- FULL OUTER JOIN
SELECT *
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;

-- CROSS JOIN
SELECT *
FROM users CROSS JOIN role

