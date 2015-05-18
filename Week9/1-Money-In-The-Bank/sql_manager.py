import sqlite3
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def get_all_usernames():
    query = "Select username from clients"
    all_users = cursor.execute(query).fetchall()
    output = []
    if isinstance(all_users, tuple):
        output.append(all_users[0])
    if isinstance(all_users, list):
        for user in all_users:
            output.append(user[0])
    return output


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user, ))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user, ))
    conn.commit()


def register(username, password):
    insert_sql = "insert into clients (username, password) values (?,?)"
    cursor.execute(insert_sql, (username, password, ))
    conn.commit()


def login(username, password):
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    cursor.execute(select_query, (username, password, ))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
