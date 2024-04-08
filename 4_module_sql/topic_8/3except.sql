SELECT product_id, sales_date, revenue FROM online_sales
EXCEPT ALL
SELECT product_id, sales_date, revenue FROM offline_sales;


SELECT product_id, sales_date, revenue FROM offline_sales
EXCEPT
SELECT product_id, sales_date, revenue FROM online_sales;
