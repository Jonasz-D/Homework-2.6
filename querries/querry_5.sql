SELECT teachers.teacher_name, subjects.subject_name
FROM teachers
JOIN subjects ON subjects.teacher_id = teachers.id
WHERE teachers.teacher_name = 'Katie Powell'
