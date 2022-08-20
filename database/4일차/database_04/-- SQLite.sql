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