import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

from src.UI.main_window import Ui_w_main_window

from TaskManager import TaskManager
from TableModel import TaskTableModel
from addtaskwindow import AddTask
from deletedialog import DeleteDialog

class MainWindow(qtw.QWidget, Ui_w_main_window):
    #addTask = qtc.Signal()
    taskManager = TaskManager("../../tasks.db")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Installing resize mode to stretch for Header
        self.w_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.w_table.horizontalHeader().setStretchLastSection(True)
        self.pb_add.clicked.connect(self.openAddTask)
        self.pb_remove.clicked.connect(self.removeSelectedTask)
        self.hasFocus()
        self.updateTaskTable()

    @qtc.Slot()
    def openAddTask(self):
        self.form = AddTask()
        self.form.task_submited.connect(self.addNewTask)
        self.form.exec()

    @qtc.Slot()
    def openEditTask(self):
        self.form = AddTask()
        self.form.groupBox.setTitle("Edit task")
        self.form.task_submited.connect(self.addNewTask)
        self.form.exec()

    @qtc.Slot()
    def addNewTask(self, title:str, deadline:str):
        new_task = self.taskManager.create_task(title, deadline)
        self.taskManager.add_task(new_task)
        self.updateTaskTable()

    @qtc.Slot()
    def removeSelectedTask(self):
        #add select later
        delete_dialog = DeleteDialog()
        result = delete_dialog.exec()

        if result:
            print("задача удалена")
            #self.taskManager.delete_task() # task id
            self.updateTaskTable()
        else:
            print("задача не изменена")

    def updateTaskTable(self):
        tasks = self.taskManager.get_all_tasks()
        self.model = TaskTableModel(tasks)
        self.w_table.setModel(self.model)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())