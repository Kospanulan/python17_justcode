SELECT * FROM users;

-- Typecasting
SELECT id, name, surname, cast(age as VARCHAR(30)) FROM users;
SELECT id, name, surname, age::VARCHAR(30) FROM users;

-- Default in func
SELECT id, name, coalesce(surname, ''), age FROM users;
-- INSERT INTO users (name, age)
-- VALUES ('TEST1', 22),
-- 		('TEST3', 34)

-- SORT NULLs
SELECT id, name, surname, age FROM users
ORDER BY age ASC NULLS FIRST;

-- INSERT INTO users (name, surname)
-- VALUES ('TEST2', 'test_agov'),
-- 		('TEST4', 'age_testov')













































