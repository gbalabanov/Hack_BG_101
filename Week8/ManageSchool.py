import sqlite3

conn = sqlite3.connect("School.db")
cursor = conn.cursor()


def list_all_courses():
    try:
        output = cursor.execute("Select name from Courses").fetchall()
        for x in output:
            print(x[0])
        return True
    except Exception as e:
        print(e)
        return False

def list_all_students():
    try:
        output = cursor.execute("Select name, github from Students").fetchall()
        for x in output:
            print(x[0] + " - " + str(x[1]))
        return  True
    except Exception as e:
        print(e)
        return False

def list_students_courses():
    try:
        output = cursor.execute("Select Students.name, Courses.name From Students JOIN students_to_courses ON Students.id = students_to_courses.student_id JOIN Courses ON students_to_courses.course_id = Courses.id").fetchall()
        for x in output:
            print(x[0] + " - " + str(x[1]))
        return True
    except Exception as e:
        print(e)
        return False

print(list_students_courses())
