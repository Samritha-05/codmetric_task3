TASK_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASK_FILE, "r",encoding="utf-8") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, "w",encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(task):
    tasks.append(f"[ ] {task}")
    save_tasks(tasks)
    print("Task added successfully.")

def display_tasks():
    print("\n===TASK LIST===")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    print()


def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task Deleted: {removed}")
    except IndexError:
        print("Invalid task number!!!")


def complete_task(index):
    try:
        if tasks[index - 1].startswith("[ ]"):
            tasks[index - 1] = tasks[index - 1].replace("[ ]", "[✓]", 1)
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Task is already completed.")
    except IndexError:
        print("Invalid task number!!!")


tasks = load_tasks()

while True:
    print("\nOPTIONS: \n 1.Add TASK\n 2.Delete TASK\n 3.Complete TASK\n 4.Show LIST\n 5.Exit TASK")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter the task: ")
        add_task(task)
    elif choice == 2:
        display_tasks()
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    elif choice == 3:
        display_tasks()
        num = int(input("Enter task number to mark as completed: "))
        complete_task(num)
    elif choice == 4:
        display_tasks()
    elif choice == 5:
        print("Exiting Task Manager")
        break
    else:
        print("Invalid option.")
