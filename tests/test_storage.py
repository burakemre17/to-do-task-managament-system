import os
from storage import save_state, load_state

def test_save_and_load_state(tmp_path):
    base_dir = tmp_path / "data"

    tasks = [{"id": "1", "title": "Test", "status": "pending"}]
    categories = []
    activity = []

    save_state(str(base_dir), tasks, categories, activity)
    loaded_tasks, loaded_categories, loaded_activity = load_state(str(base_dir))

    assert loaded_tasks == tasks
    assert loaded_categories == categories