from tasks import (
    create_task,
    update_task,
    delete_task,
    mark_task_status,
    add_subtask,
    filter_tasks,
    search_tasks,
    summarize_by_category,
    upcoming_tasks
)
from views import list_tasks, print_tasks, print_category_summary

tasks = []

def main():
    """Run the interactive terminal menu."""
    
    while True:
        print("1) Add task")
        print("2) View tasks")
        print("3) Update task")
        print("4) Delete task")
        print("5) Mark status")
        print("6) Add subtask")
        print("7) Filter tasks")
        print("8) Search tasks")
        print("9) Category summary")
        print("10) Upcoming tasks ")
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

        elif choice == "7":
            status = input("Status (or leave empty): ") or None
            category = input("Category (or leave empty): ") or None
            due = input("Due before (YYYY-MM-DD or empty): ") or None
            result = filter_tasks(tasks, status=status, category=category, due_before=due)
            print_tasks(result)

        elif choice == "8":
            q = input("Search query: ")
            result = search_tasks(tasks, q)
            print_tasks(result)

        elif choice == "9":
            summary = summarize_by_category(tasks)
            print_category_summary(summary)

        elif choice == "10":
            d = int(input("Days ahead: "))
            result = upcoming_tasks(tasks, d)
            print_tasks(result)

        elif choice == "0":
            break

if __name__ == "__main__":
    main()