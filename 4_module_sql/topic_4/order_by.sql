
SELECT * FROM new_users
OFFSET 50
LIMIT 5;


SELECT * FROM new_users
ORDER BY username;

SELECT DISTINCT name, surname FROM users;





-- 1 -----------
SELECT * FROM new_users
ORDER BY created_at
LIMIT 5;

-- 2 -----------
SELECT * FROM new_users
WHERE role_name='guest'
ORDER BY created_at DESC
LIMIT 5;


-- 3 -----------
SELECT DISTINCT role_name FROM new_users;


































































