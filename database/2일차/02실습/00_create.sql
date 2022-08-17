-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare


-- 추가되어 있는 모든 데이터의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare;

-- 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 
SELECT MAX(age), MIN(age) FROM healthcare;

-- 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare; 

-- 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE height>=160 AND height<=170; 

--실패 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 
SELECT waist FROM healthcare WHERE is_drinking=1 AND waist != '' ORDER BY waist DESC LIMIT 5;

-- 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE va_left>1.5 AND va_right>1.5 AND is_drinking=1;

-- 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE blood_pressure<120;

-- 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.
SELECT AVG(waist) FROM healthcare WHERE blood_pressure>=140;

-- 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(height)를 출력하시오.
SELECT AVG(height), AVG(height) FROM healthcare WHERE gender=1;

-- 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.
SELECT MAX(height) FROM healthcare;
SELECT id, height, weight FROM healthcare WHERE height=195 ORDER BY weight DESC LIMIT 1, 1;

-- BMI가 30이상인 사람의 수를 출력하시오. 
SELECT COUNT(*) FROM healthcare WHERE (weight / ((height * height) * 0.0001) >= 30);

-- 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.
SELECT id, weight / ((height * height) * 0.0001) FROM healthcare WHERE smoking = 3 ORDER BY weight / ((height * height) * 0.0001) DESC LIMIT 5;