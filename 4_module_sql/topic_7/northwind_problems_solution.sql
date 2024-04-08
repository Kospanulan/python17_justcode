SELECT * FROM products;

SELECT * FROM categories;

SELECT * FROM customers;

SELECT * FROM orders;

SELECT * FROM order_details;



-- 1 -----------------

SELECT c.customer_id, c.company_name, 
	   o.order_id, o.order_date, o.shipped_date
FROM customers as c
LEFT JOIN orders o
ON c.customer_id=o.customer_id
ORDER BY c.customer_id;

-- 2 ------------------

SELECT p.product_name,
	   c.category_name,
	   c.description
FROM products as p
LEFT JOIN categories as c
ON p.category_id=c.category_id
-- 3 Домашнее задание -----------

-- 4 ----------------------------

SELECT c.customer_id, c.company_name, 
	   o.order_id, o.order_date, o.shipped_date
FROM customers as c
INNER JOIN orders o
ON c.customer_id=o.customer_id
WHERE shipped_date IS NOT NULL
ORDER BY c.customer_id;

-- 5 -----------------------------------------

SELECT * FROM suppliers;
SELECT * FROM products;


SELECT s.supplier_id,
	   s.company_name,
	   p.product_id,
	   p.product_name,
	   c.category_name
FROM suppliers as s

INNER JOIN products as p
ON s.supplier_id = p.supplier_id

INNER JOIN categories as c
ON c.category_id=p.category_id

ORDER BY s.supplier_id;

-- 6 ---------------------------------------------

SELECT * FROM order_details;

SELECT order_id, COUNT(order_id), SUM(quantity) FROM order_details
GROUP BY order_id
HAVING COUNT(order_id) > 1;


-- 7 ---------------------------------------------

SELECT c.category_id,
	   c.category_name,
	   SUM(o.unit_price * o.quantity) as overall_price
FROM categories as c

INNER JOIN products as p
ON c.category_id=p.category_id

INNER JOIN order_details as o
ON p.product_id=o.product_id

GROUP BY c.category_id, c.category_name;

