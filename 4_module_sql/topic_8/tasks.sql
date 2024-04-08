-- 1 ------------------------------
SELECT product_id, sales_date, revenue, 'online' as "from" FROM online_sales
UNION ALL
SELECT product_id, sales_date, revenue, 'offline' as "from" FROM offline_sales;


-- 2 ------------------------------
SELECT product_id FROM online_sales
WHERE sales_date > '2023-01-01'

EXCEPT ALL

SELECT product_id FROM offline_sales
WHERE sales_date > '2023-01-01';

















