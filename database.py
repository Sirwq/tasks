import sqlite3

def initDb():
    db = sqlite3.connect("tasks.db")
    cursor = db.cursor() 
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP,
                    deadline DATETIME   
    )""")
    db.commit()
    db.close()