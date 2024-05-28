SELECT s.student_name, AVG(grade) as average_grade
FROM grades
INNER JOIN students AS s ON s.id = grades.student_id
GROUP BY student_id
ORDER BY AVG(grades.grade) DESC
LIMIT 5

