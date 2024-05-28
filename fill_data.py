import faker, sqlite3
from random import choices, randint

NUMBER_OF_STUDENTS = 40
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 7
NUMBER_OF_TEACHERS = 4
NUMBER_OF_GRADES_PER_STUDENT = 20
LIST_OF_SUBJETS = ['Math', 'Art', 'English', 'Music', 'History', 'Science', 'Geography', 'Physical education']


def generate_fake_data(number_of_students, number_of_groups, number_of_subjects, 
                       number_of_teachers, list_of_subjects):
    fake_students = []
    fake_groups = []
    fake_subjects = []
    fake_teachers = []
    fake_grades = []

    fake_data = faker.Faker()

    for _ in range(number_of_students):
        fake_students.append(fake_data.name())

    for group in range(number_of_groups):
        group_name = f'Group {group + 1}'
        fake_groups.append(group_name)

    for subject in range(number_of_subjects):
        fake_subjects.append(list_of_subjects[subject])

    for _ in range(number_of_teachers):
        fake_teachers.append(fake_data.name())

    #creating a list of grades
    fake_grades = []
    grade = 2
    while grade <= 6:
        fake_grades.append(grade)
        grade += 0.5

    return fake_students, fake_groups, fake_subjects, fake_teachers, fake_grades


def prepare_data(students, groups, subjects, teachers, grades, number_of_teachers, number_of_students, number_of_groups, number_of_grades_per_student, number_of_subjects):
    data_for_students = []
    for student in students:
        group_id = randint(1, number_of_groups)
        data_for_students.append((student, group_id))

    data_for_groups = []
    for group in groups:
        data_for_groups.append((group, ))

    data_for_subjects = []
    for subject in subjects:
        data_for_subjects.append((subject, randint(1, number_of_teachers)))

    data_for_teachers = []
    for teacher in teachers:
        data_for_teachers.append((teacher, ))

    data_for_grades = []
    for student in range(1, number_of_students + 1):
        num_of_grade = 0
        while num_of_grade < number_of_grades_per_student:
            data_for_grades.append((student, randint(1, number_of_subjects), choices(grades)[0]) )
            num_of_grade += 1

    return data_for_students, data_for_groups, data_for_subjects, data_for_teachers, data_for_grades


def insert_data_to_db(students, groups, subjects, teachers, grades):
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()

        sql_to_students = '''INSERT INTO students(student_name, group_id)
        VALUES (?, ?)'''
        cur.executemany(sql_to_students, students)

        sql_to_groups = '''INSERT INTO groups(group_name)
        VALUES (?)'''
        cur.executemany(sql_to_groups, groups)

        sql_to_subjects = '''INSERT INTO subjects (subject_name, teacher_id)
        VALUES (?, ?)'''
        cur.executemany(sql_to_subjects, subjects)

        sql_to_teachers = '''INSERT INTO teachers (teacher_name)
        VALUES (?)'''
        cur.executemany(sql_to_teachers, teachers)

        sql_to_grades = '''INSERT INTO grades(student_id, subject_id, grade)
        VALUES(?, ?, ?)'''
        cur.executemany(sql_to_grades, grades)

        con.commit()


if __name__ == '__main__':
    students, groups, subjects, teachers, grades = generate_fake_data(NUMBER_OF_STUDENTS, NUMBER_OF_GROUPS, NUMBER_OF_SUBJECTS, 
                    NUMBER_OF_TEACHERS, LIST_OF_SUBJETS)
    
    students, groups, subjects, teachers, grades = prepare_data(students, groups, subjects, teachers, grades, NUMBER_OF_TEACHERS, 
                                                                NUMBER_OF_STUDENTS, NUMBER_OF_GROUPS, NUMBER_OF_GRADES_PER_STUDENT, NUMBER_OF_SUBJECTS)
    insert_data_to_db(students, groups, subjects, teachers, grades)