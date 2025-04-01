from datetime import datetime

# id, title, created date, finish date
class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.createdDate = datetime.now()

    def __str__(self):
        return f"{self.title} | created: {self.createdDate.strftime("%Y-%m-%d %H:%M:%S")} | finish untill: {self.deadline}"
    
    @property
    def title(self):
        return self._title
    
    @property
    def deadline(self):
        return self._deadline
    
    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Missing title")
        self._title = title

    @deadline.setter
    def deadline(self, deadline):
        if not deadline:
            raise ValueError("Missing deadline")
        try:
            self._deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            raise ValueError(f"Invalid deadline format: {e}")

def getCurrentTime():
    return datetime.now()

def addTask(self, title, finishDate):
    pass

def renameTask(self):
    pass