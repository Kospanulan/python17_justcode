SELECT * FROM users;

-- LIKE, case-sensitive, case-insensitive  ----------------------------------------
SELECT * FROM users
WHERE name LIKE '%ES%';
-- WHERE name LIKE '%Y%r%';
-- WHERE name LIKE 'Ye%';

SELECT * FROM users
WHERE surname LIKE '____';
-- WHERE surname LIKE '%t__';
-- WHERE surname LIKE '%o_';

SELECT * FROM users
WHERE LENGTH(surname)=4;


-- BETWEEN -----------------------------
SELECT * FROM users
WHERE age BETWEEN 10 AND 25
-- WHERE age > 10 AND age < 25


-- IN ---------------------------
-- ['Leskov', 'Tolebi', 'Khan']
SELECT * FROM users
WHERE surname IN ('Leskov', 'Tolebi', 'Khan')


SELECT * FROM users
WHERE NOT surname='Khan';


SELECT * FROM users
WHERE NOT surname IN ('Leskov', 'Tolebi', 'Khan')

-- T AND T = T
-- T AND F = F

-- NOT True = False
-- NOT False = True




















































