import sqlite3 as sq


# List of all users
def select_users(db_file):
    connect = sq.connect(db_file)
    cur = connect.cursor()
    cur.execute("SELECT user_id FROM all_users")
    result = cur.fetchall()
    connect.close()
    print(result)
    return result


# User entry into the database
def write_user(db_file, user_id, first_name, username):
    connect = sq.connect(db_file)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO all_users (user_id, first_name, username) VALUES (?, ?, ?)", (user_id, first_name,
                                                                                              username))
    connect.commit()
    connect.close()