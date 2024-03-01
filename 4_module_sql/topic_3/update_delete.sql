SELECT * FROM users;
SELECT * FROM table3;

-- ALTER TABLE users ADD age INTEGER;

-- Update
UPDATE users 
SET age=99, surname='Tolebi'
WHERE surname='20';

-- Delete
-- SELECT * FROM users
DELETE FROM users
WHERE surname='M' OR surname='Kospan';


DELETE FROM table3;




