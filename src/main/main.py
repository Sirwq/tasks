from src.main.TaskManager import TaskManager

tm = TaskManager("../../tasks.db")
tm.init_db()

#Y-m-d H:M:S
task = tm.create_task("Test Task213", "2029-10-31 23:59:59")
x = tm.add_task(task)
print(f"Task added with ID: {x}")

tasks = tm.get_all_tasks()
for task in tasks:
    print(task.id, task.title, task.created, task.deadline, task.completed)
