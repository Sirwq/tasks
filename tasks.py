from datetime import datetime

# id, title, created date, finish date
class Task:
<<<<<<< HEAD
    def __init__(self, id, title, deadline):
        self.id = None
=======
    def __init__(self, title, deadline: datetime):
>>>>>>> 4f73b2575169acffb4132ff5a1ea27966e15fab1
        self.title = title
        self.deadline = deadline
        self.createdDate = datetime.now()

    def __str__(self):
        return f"{self.title} | created: {self.createdDate} | finish untill: {self.deadline}"
    
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
<<<<<<< HEAD
            raise ValueError(f"Invalid deadline format: {e}")

    def addTask(self, title, finishDate):
        pass

    def renameTask(self):
        pass
=======
            raise ValueError(f"Invalid deadline format: {e}")
>>>>>>> 4f73b2575169acffb4132ff5a1ea27966e15fab1
