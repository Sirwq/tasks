import pytest
from src.main.Task import Task
from datetime import datetime, timedelta

def test_task_creation():
    # Create a task with a specific due date
    due_date = datetime.now() + timedelta(days=5)
    task = Task(title="Test Task", description="This is a test task.", due_date=due_date)

    # Check if the task is created with the correct attributes
    assert task.title == "Test Task"
    assert task.description == "This is a test task."
    assert task.due_date == due_date

    for py in pytest:
        py.add_task(task)