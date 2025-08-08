-- 📄 Примеры команд SQL (подсказки):
-- ===========================
-- Как создать таблицу:
-- CREATE TABLE table_name (
--     column1 datatype,
--     column2 datatype,
--     ...
-- );

-- Как вставить данные:
-- INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');

-- Как обновить данные:
-- UPDATE table_name SET column1 = 'new_value' WHERE some_condition;

-- Как добавить новый столбец:
-- ALTER TABLE table_name ADD COLUMN column_name datatype;

-- Как удалить таблицу:
-- DROP TABLE table_name;

-- ===========================
-- 📋 Задания (выполняйте TODO):
-- ===========================


-- ✅ TODO 1: Создайте таблицу "Employees" с полями:
-- Name (TEXT), Position (TEXT), Department (TEXT), Salary (NUMERIC)

-- 📝 Напишите здесь CREATE TABLE
-- Пример:
CREATE TABLE Employees (
    Name TEXT,
       Position TEXT,
       Department TEXT,
       Salary NUMERIC
       );


-- ✅ TODO 2: Вставьте несколько записей в таблицу "Employees"

-- 📝 Напишите здесь INSERT INTO
-- Пример:
INSERT INTO Employees (Name , Position, Department, Salary) VALUES
('Alice', 'Manager', 'Sales', 6000),
('Roma', 'Developer', 'IT', 4500),
('Max', 'Salesperson', 'Sales', 3500),
('Alexei', 'Developer', 'IT', 5000);


-- ✅ TODO 3: Измените должность одного из сотрудников на более высокую

-- 📝 Напишите здесь UPDATE
-- Пример:
UPDATE Employees 
SET Position = "Senior Developer" 
WHERE Name = 'Alexei';


-- ✅ TODO 4: Добавьте новое поле "HireDate" (DATE) в таблицу "Employees"

-- 📝 Напишите здесь ALTER TABLE
-- Пример:
ALTER TABLE Employees 
ADD COLUMN HireDate DATE;


-- ✅ TODO 5: Добавьте дату приема на работу для всех сотрудников

-- 📝 Напишите здесь UPDATE для каждого сотрудника
-- Пример:
UPDATE Employees SET HireDate = '2020-01-10' WHERE Name = 'Alexei';
UPDATE Employees SET HireDate = '2021-03-15' WHERE Name = 'Max';
UPDATE Employees SET HireDate = '2022-06-01' WHERE Name = 'Alice';
UPDATE Employees SET HireDate = '2021-10-20' WHERE Name = 'Roma';


-- ✅ TODO 6: Найдите всех сотрудников с должностью "Manager"

-- 📝 Напишите здесь SELECT
-- Пример:
SELECT * FROM Employees WHERE Position = "Manager"


-- ✅ TODO 7: Найдите всех сотрудников с зарплатой больше 5000

-- 📝 Напишите здесь SELECT
-- Пример:
SELECT * FROM Employees WHERE Salary > 5000;


-- ✅ TODO 8: Найдите всех сотрудников, которые работают в отделе "Sales"

-- 📝 Напишите здесь SELECT
-- Пример:
SELECT * FROM Employees WHERE Department = "Sales";


-- ✅ TODO 9: Найдите среднюю зарплату всех сотрудников

-- 📝 Напишите здесь SELECT AVG(...)
-- Пример:
SELECT AVG(Salary) AS AverageSalary FROM Employees;


-- ✅ TODO 10: Удалите таблицу "Employees"

-- ⚠️ ВНИМАНИЕ: Эта команда удалит таблицу и все данные!
-- Выполняйте её только после того, как закончите все задания выше.

-- 📝 Напишите здесь DROP TABLE
-- Пример:
DROP TABLE Employees;


-- 🎯 *Задание с повышенным уровнем сложности:*
-- Реализуйте задачи 6–9 в виде ХРАНИМЫХ ФУНКЦИЙ или ПРОЦЕДУР.

-- Подсказка:
-- CREATE FUNCTION или CREATE PROCEDURE
-- BEGIN ... END

-- Пример вызова:
-- CALL имя_процедуры();

-- 📝 Напишите здесь свои CREATE FUNCTION / PROCEDURE

CREATE PROCEDURE GetSalesEmployees()
BEGIN
    SELECT * FROM Employees WHERE Department = "Sales"
END

CALL GetSalesEmployees();
