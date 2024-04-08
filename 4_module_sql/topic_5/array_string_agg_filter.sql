SELECT * FROM new_users;


SELECT 
	role_name, 
	COUNT(id), 
-- 	array_agg(username)
	string_agg(username, '; ')

FROM new_users
GROUP BY role_name;







SELECT 
	role_name, 
	COUNT(id) as overall_count,
	COUNT(id) FILTER (WHERE created_at BETWEEN '2020-01-01' AND '2021-01-01') as year_2020,
	COUNT(id) FILTER (WHERE created_at BETWEEN '2021-01-01' AND '2022-01-01') as year_2021,
	COUNT(id) FILTER (WHERE created_at BETWEEN '2022-01-01' AND '2023-01-01') as year_2022,
	COUNT(id) FILTER (WHERE created_at BETWEEN '2023-01-01' AND '2024-01-01') as year_2023,
	COUNT(id) FILTER (WHERE created_at BETWEEN '2024-01-01' AND '2025-01-01') as year_2024
FROM new_users
GROUP BY role_name;








SELECT 
	role_name, 
	COUNT(id) as year_2021
FROM new_users
WHERE created_at BETWEEN '2021-01-01' AND '2022-01-01'
GROUP BY role_name;




































