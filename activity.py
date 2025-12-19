from datetime import datetime
import os

def log_activity(log_path: str, event: dict) -> None:
    """Append a task-related activity event to the log file."""

    event["timestamp"] = datetime.utcnow().isoformat()

    with open(log_path, "a", encoding="utf-8") as file:
        file.write(str(event) + "\n")

def load_activity(log_path: str) -> list:
    """Load all activity events from the log file."""

    if not os.path.exists(log_path):
        return[]

    with open(log_path, "r", encoding="utf-8") as file:
        return file.readlines()
    
def productivity_stats(tasks: list, activity_log: list) -> dict:
    """Generate basic productivity statistics."""

    total = len(tasks)
    completed = len([t for t in tasks if t["status"] == "completed"])

    return {
    "total_tasks": total,
    "completed_tasks": completed
}

def export_report(report: dict, filename: str) -> str:
    """Export a productivity report to a text file."""

    with open(filename, "w", encoding="utf-8") as file:
        for key, value in report.items():
            file.write(f"{key}: {value}\n")
    
    return filename