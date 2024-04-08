SELECT * FROM departments;
SELECT * FROM employees;

UPDATE departments
SET city='Karaganda'
WHERE city='Astana';

-- 1 --------------------
SELECT e.id, 
	   e.first_name,
	   e.city as employees_city, 
	   d.id, 
	   d.name, 
	   d.city 
FROM employees as e
JOIN departments as d
ON e.department_id=d.id AND e.city=d.city;

-- 4 ----------------------------

SELECT e.id, 
	   e.first_name,
	   e.salary, 
	   d.id as department_id, 
	   d.name
FROM employees as e
JOIN departments as d
ON e.department_id=d.id
ORDER BY salary DESC
LIMIT 3








