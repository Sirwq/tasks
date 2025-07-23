from PySide6 import QtCore
from datetime import datetime

class TaskTableModel(QtCore.QAbstractTableModel):
    def __init__(self, tasks):  # Принимаем список объектов Task
        super().__init__()
        self._data = tasks
        self._headers = ["", "Название", "Срок выполнения", "Осталось время"]  # Заголовки колонок

    def data(self, index, role):
        task = self._data[index.row()]
        column = index.column()

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and column == 0:
            return QtCore.Qt.CheckState.Checked if task.completed else QtCore.Qt.CheckState.Unchecked

        # Display columns
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if column == 0:
                return ""
            if column == 1:
                return task.title
            elif column == 2:
                if isinstance(task.deadline, datetime):
                    return task.deadline.strftime("%H:%M %d-%m-%Y")
                return str(task.deadline)
            elif column == 3:
                return task.timedeltaFormat()
            return None

        # Aligment flags
        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            if column == 3:
                return QtCore.Qt.AlignmentFlag.AlignRight
            return QtCore.Qt.AlignmentFlag.AlignCenter
        return None

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._headers)

    def headerData(self, section, orientation, role):
        # Метод для отображения заголовков колонок
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self._headers[section]
        return None

    def flags(self, index, /):
        defaultFlags = super().flags(index)

        if index.column() == 0:
            return defaultFlags | QtCore.Qt.ItemFlag.ItemIsUserCheckable
        return defaultFlags