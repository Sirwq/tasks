import sqlite3
from task import Task


class TaskManager:
    def __init__(self, db_path="../tasks.db"):
        self.db_path = db_path
        self.init_db()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self._get_connection() as db:
            cursor = db.cursor() 
            cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                created DATETIME DEFAULT CURRENT_TIMESTAMP,
                deadline DATETIME,
                completed INTEGER DEFAULT 0
                ) 
            """)
            db.commit()

    def create_task(self, title: str, deadline: str):
        task = Task(title, deadline)
        return task

    def add_task(self, task: Task):
        with self._get_connection() as db:
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO tasks (title, created, deadline, completed)
                VALUES (?, ?, ?, ?)
                """, (task.title, task.created, task.deadline, task.completed))
            db.commit()
            task.id = cursor.lastrowid
        return task.id

    def get_all_tasks(self):
        with self._get_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT id, title, created, deadline, completed FROM tasks")
            rows = cursor.fetchall()

        tasks = [
            Task(
                id=row[0],
                title=row[1],
                created=row[2],
                deadline=row[3],
                completed=bool(row[4])
            )
            for row in rows
        ]
        return tasks

    def mark_completed(self, task_id):
        with self._get_connection() as db:
            cursor = db.cursor()
            cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id))
            db.commit()
            print(f"Task {task_id} marked as completed.")

    def delete_task(self, task_id):
        with self._get_connection() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id))
            db.commit()
            print(f"Task {task_id} deleted.")
