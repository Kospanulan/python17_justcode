-- UNION ---------------------------------------
SELECT product_id, sales_date, revenue FROM online_sales
UNION
SELECT product_id, sales_date, revenue FROM offline_sales;

-- UNION ALL ---------------------------------------
SELECT product_id, sales_date, revenue FROM online_sales
UNION ALL
SELECT product_id, sales_date, revenue FROM offline_sales;





-- SELECT * 
-- FROM online_sales
-- JOIN offline_sales
-- ON online_sales.product_id=offline_sales.product_id;