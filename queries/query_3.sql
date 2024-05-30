SELECT subjects.subject_name, groups.group_name, AVG(grades.grade)
FROM grades
JOIN subjects ON subjects.id = grades.subject_id
JOIN students ON students.id = grades.student_id
JOIN groups ON groups.id = students.group_id
WHERE subjects.subject_name = 'English'
GROUP BY students.group_id
ORDER BY groups.id