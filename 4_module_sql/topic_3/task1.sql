-- 1
CREATE TABLE all_orders(
	order_id SERIAL PRIMARY KEY,
	user_id INTEGER, 
	product VARCHAR(30), 
	quantity INTEGER, 
	price NUMERIC(2)
);

SELECT * FROM all_orders;

-- 2
ALTER TABLE all_orders ADD created_at TIMESTAMP;
-- ALTER TABLE all_orders ADD ROW 1, 2, 'sdc', 12, 13.22, NOW();

-- 3
ALTER TABLE all_orders ALTER product TYPE VARCHAR(50);

-- 4
ALTER TABLE all_orders DROP user_id;

-- 5
ALTER TABLE all_orders RENAME order_id TO id;

-- 6
ALTER TABLE all_orders RENAME TO orders;

-- 7
DROP TABLE orders;




