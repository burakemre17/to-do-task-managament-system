import uuid
from datetime import datetime, timedelta

def _now():
    """Return the current UTC timestamp in ISO format."""
    return datetime.utcnow().isoformat()

def create_task(tasks: list, task_data: dict) -> dict:
    """Create a new task and append it to the tasks list."""
    
    task = {
        "id": task_data.get("id", str(uuid.uuid4())),
        "title": task_data.get("title", "").strip(),
        "description": task_data.get("description", ""),
        "category": task_data.get("category", None),
        "priority": task_data.get("priority", "Medium"),
        "status": task_data.get("status", "pending"),
        "due_date": task_data.get("due_date", None),
        "created_at": _now(),
        "updated_at": _now(),
        "completed_at": None,
        "subtasks": []
    }
    tasks.append(task)
    return task

def update_task(tasks: list, task_id: str, updates: dict) -> dict:
    """Update fields of an existing task."""

    for task in tasks:
        if task["id"] == task_id:
            for key, value in updates.items():
                if key in task:
                    task[key] = value
            task["updated_at"] = _now()
            return task
    return None

def delete_task(tasks: list, task_id: str) -> bool:
    """Delete a task from the list by its ID."""

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False

def mark_task_status(tasks: list, task_id: str, status: str) -> dict:
    """Change the status of a task and update timestamps."""

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = _now()
            if status.lower() == "completed":
                task["completed_at"] = _now()
            return task
    return None

def add_subtask(tasks: list, task_id: str, subtask_data: dict) -> dict:
    """Add a subtask to a specific parent task."""

    for task in tasks:
        if task["id"] == task_id:
            subtask = {
                "id": str(uuid.uuid4()),
                "title": subtask_data.get("title", ""),
                "status": subtask_data.get("status", "pending"),
                "created_at": _now(),
                "completed_at": None
            }
            task["subtasks"].append(subtask)
            task["updated_at"] = _now()
            return task
    return None

def filter_tasks(tasks: list, *, status: str | None = None,
                 category: str | None = None,
                 due_before: str| None = None) -> list:
    """Filter tasks using optional parameters."""

    result = tasks

    if status is not None:
        result = [t for t in result if t["status"] == status]

    if category is not None:
        result = [t for t in result if t["category"] == category]

    if due_before is not None:
        result = [t for t in result if t["due_date"] and t["due_date"] <= due_before]

    return result

def search_tasks(tasks: list, query: str) -> list:
    """Search tasks by keyword in title or description."""

    query = query.lower()
    return [
        t for t in tasks
        if query in t["title"].lower() or query in t["description"].lower()
    ]

def summarize_by_category(tasks: list) -> dict:
    """Count tasks grouped by category."""

    summary = {}
    for task in tasks:
        cat = task["category"] or "Uncategorized"
        summary[cat] = summary.get(cat, 0) + 1
    return summary

def upcoming_tasks(tasks: list, within_days: int) -> list:
    """Return tasks with due dates within the next X days."""

    today = datetime.utcnow().date()
    limit = today + timedelta(days=within_days)

    upcoming = []
    for t in tasks:
        if not t["due_date"]:
            continue
        try:
            due = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
            if today <= due <= limit:
                upcoming.append(t)
        except:
            continue
    return upcoming