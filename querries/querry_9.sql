SELECT students.student_name, subjects.subject_name
FROM students
JOIN subjects ON subjects.id = grades.subject_id
JOIN grades ON students.id = grades.student_id
WHERE students.student_name = 'Kristen Shepard'
GROUP BY subjects.subject_name