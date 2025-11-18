def list_tasks(tasks: list) -> None:
    for task in tasks:
        print(f"{task['id']} | {task['title']} | {task['status']} | due: {task['due_date']}")
