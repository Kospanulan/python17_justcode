-- INTERSECT ----------------------------------------
SELECT product_id, sales_date, revenue FROM online_sales

INTERSECT

SELECT product_id, sales_date, revenue FROM offline_sales;

-- INTERSECT ALL ----------------------------------------
SELECT product_id, sales_date, revenue FROM online_sales

INTERSECT ALL

SELECT product_id, sales_date, revenue FROM offline_sales;

