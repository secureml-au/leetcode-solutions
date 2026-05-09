WITH RECURSIVE hierarchy AS (
    SELECT employee_id, 
           employee_name, 
           manager_id, 
           salary, 
           1 AS level
    FROM Employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT e.employee_id, 
           e.employee_name, 
           e.manager_id, 
           e.salary, 
           h.level + 1 AS level
    FROM Employees e
    JOIN hierarchy h ON e.manager_id = h.employee_id
),
subtree AS (
    SELECT employee_id AS root_id, 
           employee_id AS descendant_id,
           salary
    FROM Employees
    
    UNION ALL
    
    SELECT s.root_id, 
           e.employee_id,
           e.salary
    FROM subtree s
    JOIN Employees e ON e.manager_id = s.descendant_id
)
SELECT h.employee_id,
       h.employee_name,
       h.level,
       COUNT(s.descendant_id) - 1 AS team_size,
       SUM(s.salary) AS budget
FROM hierarchy h
JOIN subtree s ON h.employee_id = s.root_id
GROUP BY h.employee_id, h.employee_name, h.level
ORDER BY level ASC, budget DESC, employee_name ASC