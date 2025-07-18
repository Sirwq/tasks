from PySide6 import QtCore
from datetime import datetime

class TaskTableModel(QtCore.QAbstractTableModel):
    def __init__(self, tasks):  # Принимаем список объектов Task
        super().__init__()
        self._data = tasks
        self._headers = ["Статус", "Название", "Срок выполнения", "Осталось время"]  # Заголовки колонок

    def data(self, index, role):
        column = index.column()
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            task = self._data[index.row()]


            if column == 0:
                return "✅ Выполнено" if task.completed else "In Progress"
            elif column == 1:
                return task.title
            elif column == 2:
                if isinstance(task.deadline, datetime):
                    return task.deadline.strftime("%H:%M %d-%m-%Y")
                return str(task.deadline)
            elif column == 3:
                return task.timedeltaFormat()

        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            if column == 2:
                return QtCore.Qt.AlignmentFlag.AlignRight
            else:
                return QtCore.Qt.AlignmentFlag.AlignCenter



    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._headers)

    def headerData(self, section, orientation, role):
        # Метод для отображения заголовков колонок
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self._headers[section]
        return None