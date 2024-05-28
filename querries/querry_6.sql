SELECT groups.group_name, students.student_name
FROM groups
JOIN students ON students.group_id = groups.id
WHERE groups.group_name = 'Group 3'
