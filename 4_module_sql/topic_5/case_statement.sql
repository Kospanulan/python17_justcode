SELECT 
	id, 
	name, 
	surname, 
	age,
	CASE
		WHEN age < 18 THEN 'Young'
		WHEN age BETWEEN 18 AND 25 THEN 'Young Adult'
		WHEN age > 25 THEN 'Adult'
		ELSE ''
-- 		WHEN age IS NULL THEN ''
-- 		ELSE 'Adult'
		
	END as age_group
FROM users;















-- SELECT 
-- 	id, 
-- 	name, 
-- 	surname, 
-- 	age,
-- 	'Adult' as age_group
-- FROM users;



















































