
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	surname VARCHAR(30)
);


SELECT * FROM users;



CREATE TABLE table3 (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	surname VARCHAR(30),
	age INTEGER
);

SELECT * FROM table3;



CREATE TABLE table4 (
	id 			SERIAL 		PRIMARY KEY,
	name 		VARCHAR(30) UNIQUE NOT NULL,
	surname 	VARCHAR(30) DEFAULT 'Ivanov',
	age 		INTEGER 	CHECK (age > 7)
);

SELECT * FROM table4;



























