SELECT groups.group_name, AVG(grades.grade)
FROM grades
JOIN students ON students.id = grades.student_id
JOIN groups ON groups.id = students.group_id
GROUP BY groups.id