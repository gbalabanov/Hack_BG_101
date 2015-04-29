import sqlite3


conn = sqlite3.connect("Employees.db")
cursor = conn.cursor()


def list_peopel_func():
    output = cursor.execute("SELECT id, name, position  FROM People").fetchall()
    for x in output:
        print(str(x[0]) + " - " + x[1] + " - " + x[2])

def add_employee():
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

def delete_user():
    emp_id = input("  ID-->")
    cursor.execute("DELETE FROM People WHERE id = ?", emp_id)
    #TODO

def monthly_spending():
    salaries = (cursor.execute("SELECT monthly_salary FROM People")).fetchall()
    return sum([int(list(row)[0]) for row in salaries])


while True:
    command = input("Enter command-> ")
    if command == "list":
        print(list_peopel_func())
    if command == "exit":
        conn.close()
        break
    if command == "add":
        print(add_employee())
    if command == "delete":
        delete_user()
    if command == "monthly":
        print(monthly_spending())
