from tasks import create_task, filter_tasks

def test_create_task():
    tasks = []
    task = create_task(tasks, {"title": "Test Task"})

    assert len(tasks) == 1
    assert task["title"] == "Test Task"
    assert task["status"] == "pending"

def test_filter_tasks_by_status():
    tasks = []
    create_task(tasks, {"title": "Done", "status": "completed"})
    create_task(tasks, {"title": "Todo", "status": "pending"})

    completed = filter_tasks(tasks, status = "completed")

    assert len(completed) == 1
    assert completed[0]["title"] == "Done"