# Task Management System

## Project Overview
This project is a terminal-based Task Management System developed in Python. 
It is designed to help individuals and teams organize daily workflows, track task progress, and manage categories in an offline environment.

The system supports task creation, categorization, priority leveling, status updates, activity logging, and data persistence using JSON files.

---

## Features

### Task & Category Management
- Create and update tasks with details such as title, description, due date, and priority
- Manage and assign tasks to specific categories
- Persist task and category data using JSON files

### Workflow & Tracking
- Update task status (To Do, In Progress, Done) to monitor progress
- Filter and focus on tasks based on priority levels (High, Medium, Low)
- Automatic due-date tracking for better deadline management

### Activity Logging & UI
- Log application activities for history and auditing
- Structured terminal views for clear data presentation
- Real-time activity updates within the system

### Persistence & Backup
- Save system state using JSON files
- Create backups to ensure data safety
- Validate task and category data integrity

### Testing
- Automated tests for:
  - Task logic and state transitions
  - Storage reliability and JSON handling
  - Data integrity and persistence

---

## Project Structure
```text
project/
├── main.py              # Application entry point
├── tasks.py             # Core task management logic
├── activity.py          # Activity tracking and logging
├── storage.py           # Data persistence and JSON handler
├── views.py             # Terminal UI and display logic
├── backups/             # Directory for data backups
│   └── .gitkeep         # Ensures directory tracking
├── data/                # Data storage layer
│   ├── tasks.json       # Main task records
│   ├── categories.json  # Category records
│   └── activity.log     # System logs
├── tests/               # Automated test suite
│   ├── test_tasks.py    # Unit tests for tasks
│   └── test_storage.py  # Unit tests for storage
└── README.md            # Project documentation
```


---
## How to Run the Application

1. Ensure Python 3.9+ is installed
2. Navigate to the project directory
3. Run the main application:

```bash
python main.py
```
