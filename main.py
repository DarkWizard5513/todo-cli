from sys import argv, exit
import sqlite3


def create_table(conn, cursor):
    cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    completed INTEGER NOT NULL
);
    """)
    conn.commit()
    

def add_task(conn, cursor, task):
    cursor.execute("INSERT INTO tasks(description, completed) VALUES(?, ?)", (task, 0))
    conn.commit()


def list_tasks(cursor):
    cursor.execute("SELECT * FROM tasks")
    results = cursor.fetchall()
    for result in results:
        if result[2] == 0:
            print(f"[ ] {result[0]} {result[1]}")
        else:
            print(f"[X] {result[0]} {result[1]}")

try:
    conn = sqlite3.connect("list.db")
except:
    print("Error connecting to database.")
    exit()
else:
    cursor = conn.cursor()
    create_table(conn, cursor)


if argv[1] == "add":
    add_task(conn, cursor, argv[2])

elif argv[1] == "list":
    list_tasks(cursor)

else:
    conn.close()
    exit()
