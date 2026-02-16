CREATE TABLE employees(
   id INT GENERATED ALWAYS AS IDENTITY,
   first_name VARCHAR(40) NOT NULL,
   last_name VARCHAR(40) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE employee_audits (
   id INT GENERATED ALWAYS AS IDENTITY,
   employee_id INT NOT NULL,
   last_name VARCHAR(40) NOT NULL,
   changed_on TIMESTAMP NOT NULL
);

CREATE OR REPLACE FUNCTION log_last_name_changes()
RETURNS Trigger
language plpgsql
AS
$$
BEGIN
	if NEW.last_name <> OLD.last_name THEN
		INSERT INTO employee_audits(employee_id, last_name, changed_on)
		VALUES (NEW.id, NEW.last_name, NOW());
	end if;
	RETURN NEW;
END;
$$;

-- The OLD represents the row before the update while the 
-- NEW represents the new row that will be updated. 
-- The OLD.last_name returns the last name before the update and the NEW.last_name returns the new last name.


CREATE TRIGGER last_name_changes
BEFORE UPDATE
ON employees
FOR EACH ROW
EXECUTE PROCEDURE log_last_name_changes();

INSERT INTO employees (first_name, last_name)
VALUES ('John', 'Doe');

INSERT INTO employees (first_name, last_name)
VALUES ('Lily', 'Bush');

SELECT * FROM employees;

UPDATE employees
SET last_name = 'Brown'
WHERE ID = 2;

SELECT * FROM employee_audits;

-------------------------------------------------------
----------------- INSTEAD OF triggers -----------------
-------------------------------------------------------

DROP TABLE IF EXISTS employees;
CREATE  TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
CREATE TABLE salaries (
    employee_id INT,
    effective_date DATE NOT NULL,
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0,
    PRIMARY KEY (employee_id, effective_date),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
INSERT INTO employees (name)
VALUES
   ('Alice'),
   ('Bob')
RETURNING *;

INSERT INTO salaries
VALUES
   (1, '2024-03-01', 60000.00),
   (2, '2024-03-01', 70000.00)
RETURNING *;

CREATE VIEW employee_salaries
AS
SELECT e.employee_id, e.name, s.salary, s.effective_date
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id;


CREATE OR REPLACE FUNCTION update_employee_salaries()
RETURNS TRIGGER AS
$$
DECLARE
    p_employee_id INT;
BEGIN
    IF TG_OP = 'INSERT' THEN
	-- insert a new employee
        INSERT INTO employees(name)
        VALUES (NEW.name)
		RETURNING employee_id INTO p_employee_id;
	-- insert salary for the employee
        INSERT INTO salaries(employee_id, effective_date, salary)
		VALUES (p_employee_id, NEW.effective_date, NEW.salary);
	ELSIF TG_OP = 'UPDATE' THEN
	    UPDATE salaries
		SET salary = NEW.salary
		WHERE employee_id = NEW.employee_id;

    ELSIF TG_OP = 'DELETE' THEN
        DELETE FROM salaries
		WHERE employee_id = OLD.employee_id;
	END IF;
	RETURN NULL;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER instead_of_employee_salaries
INSTEAD OF INSERT OR UPDATE OR DELETE
ON employee_salaries
FOR EACH ROW
EXECUTE FUNCTION update_employee_salaries();

INSERT INTO employee_salaries (name, salary, effective_date)
VALUES ('Charlie', 75000.00, '2024-03-01');

SELECT * FROM employees;


DELETE FROM employee_salaries
WHERE employee_id = 3;

SELECT * FROM salaries;

SELECT
  event_object_table AS table_name,
  trigger_name
FROM
  information_schema.triggers
WHERE
  event_object_table = 'employees'
GROUP BY
  table_name,
  trigger_name
ORDER BY
  table_name,
  trigger_name;


SELECT
  tgname AS trigger_name
FROM
  pg_trigger
WHERE
  tgrelid = 'employees' :: regclass
  AND tgisinternal = false
ORDER BY
  trigger_name;






---------------------------------------------------------
------------------- EVENT TRIGGERS ----------------------
---------------------------------------------------------
CREATE TABLE audits (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    event VARCHAR(50) NOT NULL,
    command TEXT NOT NULL,
    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION audit_command()
RETURNS EVENT_TRIGGER
AS $$
BEGIN
    INSERT INTO audits (username, event , command)
    VALUES (session_user, TG_EVENT, TG_TAG );
END;
$$ LANGUAGE plpgsql;


CREATE EVENT TRIGGER audit_ddl_commands
ON ddl_command_end
EXECUTE FUNCTION audit_command();


CREATE TABLE regions(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);



SELECT * FROM audits;




