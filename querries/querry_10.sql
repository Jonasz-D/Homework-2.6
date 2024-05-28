SELECT students.student_name, teachers.teacher_name, subjects.subject_name
FROM subjects
JOIN teachers ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON students.id = grades.student_id
WHERE teachers.teacher_name = 'Katie Powell' AND students.student_name = 'Kristen Shepard'
GROUP BY subjects.subject_name