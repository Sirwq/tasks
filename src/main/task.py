from datetime import datetime

# id, title, created date, finish date
class Task:
    def __init__(self, title, deadline: datetime, id=None, created=None, completed=None):
        if id is not None:
            self.id = id
        else:
            self.id = None

        if created is not None:
            self.created = created
        else:
            self.created = datetime.now()

        if completed is not None:
            self.completed = completed
        else:
            self.completed = False
            
        self.title = title
        self.deadline = deadline
        self.completed = False

    def __str__(self):
        return f"{self.title} | created: {self.created.strftime('%Y-%m-%d %H:%M:%S')} | finish untill: {self.deadline}"
    
    @property
    def title(self):
        return self._title
    
    @property
    def deadline(self):
        return self._deadline
    
    @property
    def completed(self):
        return self._completed
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @completed.setter
    def completed(self, completed):
        if not isinstance(completed, bool):
            raise ValueError("Completed must be a boolean value")
        self._completed = completed
    
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
            if self._deadline < datetime.now():
                raise ValueError("Deadline must be in the future")
        except ValueError as e:
            raise ValueError(f"Invalid deadline format: {e}")

    def renameTask(self):
        self.title = input("Enter new title: ")
        print(f"Task renamed to {self.title}")