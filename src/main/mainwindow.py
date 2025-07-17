import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from src.main.UI.main_window import Ui_w_main_window

from TaskManager import TaskManager


class MainWindow(qtw.QWidget, Ui_w_main_window):

    #addTask = qtc.Signal()
    taskManager = TaskManager("../../tasks.db")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_remove.clicked.connect(self.close)
        self.updateTaskTable()

    def updateTaskTable(self):
        self.w_table.setRowCount(0)
        tasks = self.taskManager.get_all_tasks()
        for task in tasks:
            row_position = self.w_table.rowCount()
            self.w_table.insertRow(row_position)

            self.w_table.setItem(row_position, 0, qtw.QTableWidgetItem(task.completed))
            self.w_table.setItem(row_position, 1, qtw.QTableWidgetItem(task.title))
            self.w_table.setItem(row_position, 2, qtw.QTableWidgetItem(str(task.deadline)))




if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())