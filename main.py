from sys import argv, exit

def add_task(tasks, task):
    tasks.append((task, False))

def list_tasks(tasks):
    for index, task in enumerate(tasks):
        if task[1]:
            print(f"[X] {index+1} {task[0]}")
        else:
            print(f"[ ] {index+1} {task[0]}")

def mark_completed(tasks, task_index):
    tasks[task_index][1] = not tasks[task_index][1]
    

tasks = []

if argv[1] == "add":
    add_task(tasks, argv[2])

elif argv[1] == "list":
    list_tasks(tasks)

elif argv[1] == "done":
    index = argv[2]
    mark_completed(tasks, index-1)

else:
    exit()
