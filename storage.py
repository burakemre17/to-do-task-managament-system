import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
CATEGORIES_FILE = "categories.json"
ACTIVITY_FILE = "activity.log"

def _ensure_dir(path: str):
    """
    Ensure that a directory exists.
    If the directory does not exist, it is created.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def load_state(base_dir: str) -> tuple[list, list, list]:
    """Load tasks, categories, and activity log from disk."""

    _ensure_dir(base_dir)
    
    tasks_path = os.path.join(base_dir, TASKS_FILE)
    categories_path = os.path.join(base_dir, CATEGORIES_FILE)
    activity_path = os.path.join(base_dir, ACTIVITY_FILE)

    tasks = []
    categories = []
    activity_log = []

    try:
        if os.path.exists(tasks_path):
            with open(tasks_path, "r", encoding="utf-8") as f:
                tasks = json.load(f)

        if os.path.exists(categories_path):
            with open(categories_path, "r", encoding="utf-8") as f:
                categories = json.load(f)

        if os.path.exists(activity_path):
            with open(activity_path, "r", encoding="utf-8") as f:
                activity_log = f.readlines()

    except Exception:
        return [], [], []
    
    return tasks, categories, activity_log

def save_state(base_dir: str, tasks: list, categories: list, activity_log: list):
    """Save tasks, categories, and activity log to disk."""

    _ensure_dir(base_dir)

    with open(os.path.join(base_dir, TASKS_FILE), "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

    with open(os.path.join(base_dir, CATEGORIES_FILE), "w", encoding="utf-8") as f:
        json.dump(categories, f, indent=2)
    
    with open(os.path.join(base_dir, ACTIVITY_FILE), "w", encoding="utf-8") as f:
        for line in activity_log:
            f.write(line)

def backup_state(base_dir: str, backup_dir: str) -> list[str]:
    """Create a timestamped backup of all state files."""

    _ensure_dir(backup_dir)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    _ensure_dir(backup_path)

    copied = []

    for filename in [TASKS_FILE, CATEGORIES_FILE, ACTIVITY_FILE]:
        src = os.path.join(base_dir, filename)
        if os.path.exists(src):
            dst = os.path.join(backup_path, filename)
            with open(src, "rb") as f_src, open(dst, "wb") as f_dst:
                f_dst.write(f_src.read())
            copied.append(dst)

    return copied

def validate_task_schema(tasks: list) -> bool:
    """Validate that each task contains all required fields."""
    
    required_keys = {
        "id", "title", "description", "category",
        "priority", "status", "due_date",
        "created_at", "updated_at",
        "completed_at", "subtasks"
    }

    for task in tasks:
        if not isinstance(task, dict):
            return False
        if not required_keys.issubset(task.keys()):
            return False

    return True