import sqlite3


conn = sqlite3.connect("Employees.db")
cursor = conn.cursor()


def print_commands():
    print("Available commands:\n -list\n -add\n -delete\n -monthly\n -exit")

def list_peopel_func():
    try:
        output = cursor.execute("SELECT id, name, position  FROM People").fetchall()
        for x in output:
            print(str(x[0]) + " - " + x[1] + " - " + x[2])
        return True
    except Exception as e:
        print(e)
        return False

def add_employee():
    try:
        name = input("  NAME-->")
        salary = input("  MONTHLY SALARY--> ")
        bonus = input("  YEARLY BONUS--> ")
        position = input("  POSITION --> ")
        person = (name, salary, bonus, position)
        person_in_db = cursor.execute("SELECT name, monthly_salary, yearly_bonus, position FROM People WHERE name = ? AND monthly_salary = ? AND yearly_bonus = ? AND position = ?", person).fetchone()
        if person_in_db is not None:
            return ("Person exists !")
        cursor.execute("INSERT INTO People(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)", person)
        conn.commit()
        return True
    except Exception as e:
        print(e)

def delete_user():
    try:
        list_peopel_func()
        emp_id = input("  ID To Delete-->")
        cursor.execute("DELETE FROM People WHERE id = ?", emp_id)
        conn.commit()
    except Exception as e:
        print(e)

def monthly_spending():
    try:
        salaries = (cursor.execute("SELECT monthly_salary FROM People")).fetchall()
        return sum([int(list(row)[0]) for row in salaries])
    except Exception as e:
        print(e)

print_commands()
while True:
    command = input("Enter command-> ")
    if command == "list":
        print(list_peopel_func())
    elif command == "exit":
        conn.close()
        break
    elif command == "add":
        print(add_employee())
    elif command == "delete":
        delete_user()
    elif command == "monthly":
        print(monthly_spending())
    else:
        print("Unknown command ({})".format(command))
