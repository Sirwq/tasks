from src.main.task_manager import TaskManager

task_manager = TaskManager("../../tasks.db")
task_manager.init_db()

#Y-m-d H:M:S
task = task_manager.create_task("Test Task213", "2029-10-31 23:59:59")
x = task_manager.add_task(task)
print(f"Task added with ID: {x}")

tasks = task_manager.get_all_tasks()
for task in tasks:
    print(task.id, task.title, task.created, task.deadline, task.completed)
