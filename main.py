from sys import argv, exit


def add_task(task):
    with open("tasks.csv", "a") as file:
        file.write(f"{task},F\n")
        

def list_tasks():
    counter = 1
    with open("tasks.csv", "r") as file:
        line = file.readline().strip("\n")
        while line:
            items = line.split(",")
            if items[1] == "F":
                print(f"[ ] {counter} {items[0]}")
            else:
                print(f"[X] {counter} {items[0]}")

            line = file.readline().strip("\n")
            counter += 1
    

if argv[1] == "add":
    add_task(argv[2])

elif argv[1] == "list":
    list_tasks()

else:
    exit()
