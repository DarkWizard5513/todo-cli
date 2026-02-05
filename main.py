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
    print("Task added.")


def list_tasks(cursor):
    cursor.execute("SELECT * FROM tasks")
    results = cursor.fetchall()
    for counter, result in enumerate(results):
        if result[2] == 0:
            print(f"[ ] {counter+1}. {result[1]}")
        else:
            print(f"[X] {counter+1}. {result[1]}")


def mark_complete(conn, cursor, task_number):
    task_id = -1
    cursor.execute("SELECT id FROM tasks")
    results = cursor.fetchall()
    for counter, result in enumerate(results):
        if counter + 1 == int(task_number):
            task_id = result[0]
            break

    if task_id == -1:
        print(f"Task with number {task_number} not found in database.")
    else:
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
        print("Task completed.")


def delete_task(conn, cursor, task_number):
    task_id = -1
    cursor.execute("SELECT id FROM tasks")
    results = cursor.fetchall()
    for counter, result in enumerate(results):
        if counter + 1 == int(task_number):
            task_id = result[0]
            break

    if task_id == -1:
        print(f"Task with number {task_number} not found in database.")
    else:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        print("Task deleted.")


def edit_task(conn, cursor, task_number, new_description):
    task_id = -1
    cursor.execute("SELECT id FROM tasks")
    results = cursor.fetchall()
    for counter, result in enumerate(results):
        if counter + 1 == int(task_number):
            task_id = result[0]
            break

    if task_id == -1:
        print(f"Task with number {task_number} not found in database.")
    else:
        cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id))
        conn.commit()
        print("Task edited.")


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

elif argv[1] == "done":
    mark_complete(conn, cursor, argv[2])

elif argv[1] == "delete":
    delete_task(conn, cursor, argv[2])

elif argv[1] == "edit":
    edit_task(conn, cursor, argv[2], argv[3])

else:
    conn.close()
    exit()
