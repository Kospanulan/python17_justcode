-- ALTER TABLE departments ADD city VARCHAR(100);

-- ALTER TABLE employees ADD city VARCHAR(100);
-- ALTER TABLE employees ADD salary INT;

SELECT * FROM employees;
SELECT * FROM departments;

UPDATE departments
SET city='Aqtobe'
WHERE id=4;

SELECT * FROM employees;

UPDATE employees
SET city='Shymkent', salary=200 
WHERE id=5;

INSERT INTO employees (first_name, last_name, department_id, city, salary)
VALUES ('Sasha', 'Pirozhkov', 3, 'Almaty', 450);



CREATE TABLE users1 (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	surname VARCHAR(30),
	city VARCHAR(30),
	age INTEGER
);

CREATE TABLE users2 (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	surname VARCHAR(30),
	city VARCHAR(30),
	spec VARCHAR(30)
)



INSERT INTO users1 (name, surname, city, age)
VALUES ('Sasha', 'Pirozhkov', 'Almaty', 13),
	   ('Max', 'Leskov', 'Almaty', 23),
	   ('Elena', 'S', 'Astana', 25),
	   ('Ayaulym', 'M', 'Karaganda', 45);


INSERT INTO users2 (name, surname, city, spec)
VALUES ('Sasha', 'Pirozhkov', 'Almaty', 'Audit');
-- 		('Elena', 'S', 'Ural', 'IT');
-- 	   ('Evgenyi', 'Leskov', 'Almaty', 'Prepod'),
-- 	   ('Margo', 'P', 'Shymkent', 'Sport'),
-- 	   ('Rauan', 'Inaiyat', 'Petropavl', 'Chess');














































