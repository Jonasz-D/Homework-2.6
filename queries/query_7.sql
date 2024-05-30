SELECT groups.group_name, subjects.subject_name, students.student_name, grades.grade
FROM grades
JOIN students ON students.id = grades.student_id
JOIN groups ON students.group_id = groups.id
JOIN subjects ON subjects.id = grades.subject_id
WHERE groups.group_name = 'Group 3' AND subjects.subject_name = 'Math' 

