import uuid
from datetime import datetime

def _now():
    return datetime.utcnow().isoformat()

def create_task(tasks: list, task_data: dict) -> dict:
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
    for task in tasks:
        if task["id"] == task_id:
            for key, value in updates.items():
                if key in task:
                    task[key] = value
            task["updated_at"] = _now()
            return task
    return None

def delete_task(tasks: list, task_id: str) -> bool:
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False

def mark_task_status(tasks: list, task_id: str, status: str) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = _now()
            if status.lower() == "completed":
                task["completed_at"] = _now()
            return task
    return None

def add_subtask(tasks: list, task_id: str, subtask_data: dict) -> dict:
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
