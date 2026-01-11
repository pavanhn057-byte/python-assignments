CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(30)
);

CREATE TABLE roles (
    role_name VARCHAR(50),
    package INT
);
INSERT INTO employees VALUES
(1, 'Amit', 20, 'Mumbai'),
(2, 'Sumith', 21, 'Delhi'),
(3, 'Rahul', 20, 'Chennai'),
(4, 'Rohan', 22, 'Mumbai'),
(5, 'Arjun', 20, 'Pune');

INSERT INTO roles VALUES
( 'Developer', 50000),
( 'Data Analyst', 40000),
( 'Test engineer', 30000),
( 'HR', 45000);
-- AND condition
SELECT * FROM employees
WHERE age = 20 AND city = 'Mumbai';

-- OR condition
SELECT * FROM employees
WHERE city = 'Delhi' OR city = 'Chennai';

-- NOT condition
SELECT * FROM employees
WHERE NOT city = 'Mumbai';

-- ORDER BY age (Ascending)
SELECT * FROM employees
ORDER BY age ASC;

-- ORDER BY fee (Descending)
SELECT * FROM roles
ORDER BY package DESC;

-- LIKE (name starts with A)
SELECT * FROM employees
WHERE name LIKE 'A%';

-- LIKE (course name ends with Dev)
SELECT * FROM roles
WHERE role_name LIKE '%r';