import sys
from PySide6 import QtWidgets as qtw

from src.UI.main_window import Ui_w_main_window

from TaskManager import TaskManager
from TableModel import TaskTableModel


class MainWindow(qtw.QWidget, Ui_w_main_window):

    #addTask = qtc.Signal()
    taskManager = TaskManager("../../tasks.db")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Installing resize mode to stretch for Header
        self.w_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
        self.pb_remove.clicked.connect(self.close)

        self.updateTaskTable()

    def updateTaskTable(self):
        tasks = self.taskManager.get_all_tasks()
        self.model = TaskTableModel(tasks)
        self.w_table.setModel(self.model)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())