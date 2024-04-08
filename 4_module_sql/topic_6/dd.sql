SELECT * FROM employees;
SELECT * FROM departments;

-- INNER JOIN
SELECT * FROM departments as d
INNER JOIN employees as e
ON d.city=e.city AND d.id=e.department_id;


SELECT u1.*, u2.spec FROM users1 as u1
INNER JOIN users2 as u2
ON u1.name=u2.name;


---------------------------------------------

SELECT * FROM departments as d, employees as e
WHERE d.city=e.city AND d.id=e.department_id;


-- LEFT OUTER JOIN
SELECT d.id, d.name, d.city, e.first_name, e.department_id, e.city 
FROM departments as d
LEFT JOIN employees as e
ON d.city=e.city AND d.id=e.department_id;


SELECT u1.*, u2.name, u2.spec FROM users1 as u1
LEFT OUTER JOIN users2 as u2
ON u1.name=u2.name;

-- RIGHT JOIN
SELECT u1.*, u2.name, u2.spec FROM users1 as u1
RIGHT JOIN users2 as u2
ON u1.name=u2.name;


-- FULL JOIN
SELECT u1.*, u2.name, u2.spec FROM users1 as u1
FULL JOIN users2 as u2
ON u1.name=u2.name;




SELECT u1.*, u2.spec FROM users1 as u1
FULL JOIN users2 as u2
ON u1.name=u2.name
WHERE u1.name IS NULL OR spec IS NULL;


SELECT u1.*, u2.spec FROM users1 as u1
LEFT JOIN users2 as u2
ON u1.name=u2.name
WHERE u2.spec IS NULL;


SELECT u1.*, u2.spec FROM users1 as u1
RIGHT JOIN users2 as u2
ON u1.name=u2.name
WHERE u1.name IS NULL;
