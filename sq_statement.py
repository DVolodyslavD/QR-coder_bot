import sqlite3 as sq


# List of all users
def get_users(db_file: str) -> tuple:
    connect = sq.connect(db_file)
    cur = connect.cursor()
    cur.execute("SELECT user_id FROM all_users")
    result = cur.fetchall()
    connect.close()
    return result


# User entry into the database
def set_user(db_file: str, user_id: int, first_name: str, username: str) -> None:
    connect = sq.connect(db_file)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO all_users (user_id, first_name, username) VALUES (?, ?, ?)", (user_id, first_name,
                                                                                              username))
    connect.commit()
    connect.close()
