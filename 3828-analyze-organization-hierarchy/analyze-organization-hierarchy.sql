WITH RECURSIVE hierarchy AS (
    SELECT 
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT 
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        h.level + 1
    FROM Employees e
    JOIN hierarchy h ON e.manager_id = h.employee_id
),
descendants AS (
    SELECT 
        h1.employee_id AS manager_id,
        h2.employee_id,
        h2.salary
    FROM hierarchy h1
    JOIN hierarchy h2 ON h2.employee_id = h1.employee_id
    
    UNION ALL
    
    SELECT 
        d.manager_id,
        e.employee_id,
        e.salary
    FROM descendants d
    JOIN Employees e ON e.manager_id = d.employee_id
)
SELECT 
    h.employee_id,
    h.employee_name,
    h.level,
    COUNT(d.employee_id) - 1 AS team_size,
    SUM(d.salary) AS budget
FROM hierarchy h
LEFT JOIN descendants d ON d.manager_id = h.employee_id
GROUP BY h.employee_id, h.employee_name, h.level
ORDER BY level ASC, budget DESC, employee_name ASC;