SELECT * FROM artists;

-- 앨범(albums) 테이블의 데이터를 출력하세요.
-- 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.
SELECT * FROM albums ORDER BY title DESC LIMIT 5;

-- 고객(custmoers) 테이블의 행 개수를 출력하세요.ABORT
-- 단, 컬럼명을 고객수로 출력하세요.
SELECT COUNT(*) AS '고객수' FROM customers;

-- 고객(customers)테이블에서 고객이 사는 나라가 usa인 고객의 FirstName, LastName을 출력하세요.
-- 단, 각각의 컬럼명을 이름, 성으로 출력하고, 이름을 기준으로 내림차순으로 5개 까지 출력하세요.
SELECT FirstName AS '성', LastName AS '이름' FROM customers WHERE Country = 'USA' ORDER BY LastName DESC LIMIT 5;

-- 송장(invoices)테이블에서 BillingPostalCode NULL이 아닌 행의 개수를 출력하세요.
-- 단, 컬럼명을 송장수로 출력하세요.
SELECT COUNT(*) AS '송장수' FROM invoices WHERE BillingPostalCode NOT NULL;

-- 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.
SELECT * FROM invoices WHERE BillingState ISNULL ORDER BY InvoiceDate DESC LIMIT 5;

-- 8. 송장(InvoiceDate)테이블에서 InvoiceDate의 년도가 2013인 행의개수를 출력하세요.
SELECT COUNT(*) FROM invoices WHERE strftime("%Y", InvoiceDate) = '2013';

-- 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.
SELECT 
    CustomerId AS '고객ID', 
    FirstName AS '성', 
    LastName AS '이름' 
FROM customers 
WHERE FirstName 
LIKE 'L%';

-- 10. 고객(customers)테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
-- 단, 각각의 컬럼명을 고객 수, 나라로 출력하고 고객 수 상위 5개의 나라만 출력 하세요.
SELECT 
    COUNT(*) AS "고객 수", 
    Country AS "나라"
FROM customers 
GROUP BY Country
ORDER BY "고객 수" DESC
LIMIT 5;

-- 11. 앨범(albums)테이블에서 가장 많은 앨범이 있는 Artist의 AristId와 앨범 수를 출력하세요.
SELECT 
    ArtistId, 
    COUNT(*) AS "앨범 수"
FROM albums
GROUP BY ArtistID
ORDER BY "앨범 수" DESC
LIMIT 1;

-- 12. 앨범(albums)테이블에서 보유 앨범 수가 10개 이상인 Artist의 ArtistId와 앨범 수를 출력하세요.
-- 단, 앨범 수를 기준으로 내림차순으로 출력하세요.
SELECT
    ArtistId,
    COUNT(*) AS "앨범 수"
FROM albums
GROUP BY ArtistID
HAVING "앨범 수" >= 10
ORDER BY "앨범 수" DESC;

-- 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.
-- 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.
SELECT 
    COUNT(*) AS "고객 수",
    Country,
    State 
FROM customers
WHERE state NOT NULL
GROUP BY Country, State
ORDER BY Country DESC, "고객 수" DESC
LIMIT 5;

-- 14. 고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.
-- `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 
SELECT 
    CustomerId,
    CASE
        WHEN Fax ISNULL THEN "X"
        ELSE "O"
        END AS "Fax 유/무"
FROM customers
ORDER BY CustomerId
LIMIT 5;

-- 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.
-- 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.
-- cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.



-- 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
SELECT
    Name
FROM Artists
WHERE ArtistId = (
    SELECT
        ArtistId
    FROM (
        SELECT 
            artistid,
            COUNT(*) AS "앨범 수"
        FROM albums
        GROUP BY artistid
        ORDER BY "앨범 수" DESC
        LIMIT 1
    )
);

-- 17 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.
SELECT
    Name
FROM genres
WHERE Genreid = (
    SELECT Genreid
    FROM ( SELECT
            Genreid,
            COUNT(*) AS "장르 수"
        FROM tracks
        GROUP BY Genreid
        ORDER BY "장르 수"
        LIMIT 1
    )
);