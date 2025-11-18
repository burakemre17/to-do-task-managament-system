from tasks import (
    create_task,
    update_task,
    delete_task,
    mark_task_status,
    add_subtask
)
from views import list_tasks

tasks = []

def main():
    while True:
        print("1) Add task")
        print("2) View tasks")
        print("3) Update task")
        print("4) Delete task")
        print("5) Mark status")
        print("6) Add subtask")
        print("0) Exit")

        choice = input("Select: ")

        if choice == "1":
            title = input("Title: ")
            due = input("Due date (YYYY-MM-DD): ")
            create_task(tasks, {"title": title, "due_date": due})

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            tid = input("Task ID: ")
            field = input("Field: ")
            value = input("Value: ")
            update_task(tasks, tid, {field: value})

        elif choice == "4":
            tid = input("Task ID: ")
            delete_task(tasks, tid)

        elif choice == "5":
            tid = input("Task ID: ")
            status = input("Status: ")
            mark_task_status(tasks, tid, status)

        elif choice == "6":
            tid = input("Task ID: ")
            title = input("Subtask title: ")
            add_subtask(tasks, tid, {"title": title})

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
