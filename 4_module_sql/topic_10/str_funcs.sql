SELECT *, LENGTH(category) as "len of category" FROM products;

SELECT LENGTH('te st');

-----------------------------------------------------------------
SELECT UPPER('test');
SELECT LOWER('Test');

SELECT *, UPPER(category), LOWER(category) FROM products;

---------------------------------------------------------
SELECT CONCAT('Hello', ' ', 'World');

SELECT 
	*,
	CONCAT (product_name, ' (', product_id, ')') AS info 
FROM products;

--------------------------------------------------------------

SELECT SUBSTRING('hello world' FROM 7 FOR 3);

SELECT 
	*,
	SUBSTRING (product_name FROM 9 FOR 1) AS product 
FROM products;

---------------------------------------------------------------

SELECT ABS(-11);  -- ABSOLUTE

SELECT ROUND(45.2);
SELECT ROUND(45.5);
SELECT ROUND(45.537, 2);

SELECT CEIL(45.15);
SELECT FLOOR(45.5)

---------------------------------------------------------

SELECT NOW();

-- DAY, MONTH, YEAR
SELECT EXTRACT('DOY' FROM NOW());  -- Day Of Year
SELECT EXTRACT('DOW' FROM NOW());  -- Day Of Week

SELECT EXTRACT('DOY' FROM TIMESTAMP '2024-03-20T00:00:00');
SELECT EXTRACT('DOW' FROM TIMESTAMP '2024-01-01T00:00:00'); -- weekday()

SELECT EXTRACT('EPOCH' FROM NOW());
SELECT EXTRACT('DECADE' FROM TIMESTAMP '2024-03-20T00:00:00');
SELECT EXTRACT('CENTURY' FROM TIMESTAMP '2001-01-01T00:00:00');

-----------------------------------------------------------------
SELECT DATE_TRUNC('CENTURY', NOW())

-----------------------------------------------------------------




















