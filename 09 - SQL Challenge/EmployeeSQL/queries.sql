--Query #1: List the following details of each employee: employee number, last name, first name, sex, and salary.

SELECT emp.emp_no, emp.last_name, emp.first_name, emp.sex, s.salary
	FROM employees emp
	JOIN salaries s
	on emp.emp_no = s.emp_no;

--Query #2: List first name, last name, and hire date for employees who were hired in 1986.

SELECT emp.first_name, emp.last_name, emp.hire_date
	FROM employees emp
	WHERE EXTRACT(YEAR FROM emp.hire_date) = 1986;

--Query #3: List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

SELECT mgr.dept_no, dept.dept_name, mgr.emp_no, emp.last_name, emp.first_name
	FROM dept_manager mgr
	JOIN departments dept
		on mgr.dept_no = dept.dept_no
	JOIN employees emp
		on mgr.emp_no = emp.emp_no; 
	
--Query #4: List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
	FROM employees emp
	JOIN dept_emp
		on emp.emp_no = dept_emp.emp_no
	JOIN departments dept
		on dept.dept_no = dept_emp.dept_no;

--Query #5: List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

SELECT emp.first_name, emp.last_name, emp.sex
	FROM employees emp
	WHERE emp.first_name = 'Hercules' AND emp.last_name LIKE 'B%';

--Query #6: List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
	FROM employees emp
	JOIN dept_emp
		on emp.emp_no = dept_emp.emp_no
	JOIN departments dept
		on dept.dept_no = dept_emp.dept_no
	WHERE dept.dept_name = 'Sales';

--Query #7: List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
	FROM employees emp
	JOIN dept_emp
		on emp.emp_no = dept_emp.emp_no
	JOIN departments dept
		on dept.dept_no = dept_emp.dept_no
	WHERE dept.dept_name = 'Sales' OR dept.dept_name = 'Development';

--Query #8: In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT last_name, COUNT(last_name) AS "Count"
	FROM employees
	GROUP BY last_name
	ORDER BY "Count" DESC;


