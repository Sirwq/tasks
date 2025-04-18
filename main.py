import tasks
import database

database.initDb()

#Y-m-d H:M:S
task = tasks.Task("First task", "2025-12-31 23:47:59")
print(task)