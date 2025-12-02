def list_tasks(tasks: list) -> None:
    """Print all tasks in a simple formatted list."""
    
    for task in tasks:
        print(f"{task['id']} | {task['title']} | {task['status']} | due: {task['due_date']}")

def print_tasks(tasks: list):
    """Display a formatted list of tasks."""

    for t in tasks:
        print(f"{t['id']} | {t['title']} | {t['status']} | {t['due_date']}")

def print_category_summary(summary: dict):
    """Print category summary information. """

    for cat, count in summary.items():
        print(f"{cat}: {count} tasks")