
SELECT students.student_name, subjects.subject_name, AVG(grades.grade)
FROM grades
JOIN students ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE subjects.subject_name = 'English'

GROUP BY grades.student_id 
ORDER BY AVG(grades.grade) DESC
LIMIT 1



