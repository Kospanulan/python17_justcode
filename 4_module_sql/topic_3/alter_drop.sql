-- ADD column
ALTER TABLE table1 ADD created_at TIMESTAMP;

-- DROP column
-- ALTER TABLE table1 ADD test VARCHAR(30);
ALTER TABLE table1 DROP test;

-- ALTER Column Type
ALTER TABLE table1 ALTER name TYPE VARCHAR(30);

-- ALTER Column Constraint
ALTER TABLE table1 ALTER created_at SET DEFAULT NOW();

-- RENAME column
ALTER TABLE table1 RENAME name TO first_name;
-- ALTER TABLE table1 RENAME first_name TO name;

-- RENAME table
ALTER TABLE table1 RENAME TO new_table;
-- ALTER TABLE new_table RENAME TO table1;

-- DROP table
-- CREATE TABLE new_table(
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(30)
-- )
DROP TABLE new_table;





