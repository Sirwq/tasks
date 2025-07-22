import datetime
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from src.UI.add_task_window import Ui_d_createTask

class AddTask(qtw.QDialog, Ui_d_createTask):

    task_submited = qtc.Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.groupBox.setTitle("Add Task")
        self.dte_deadline.clear()
        self.pb_close.clicked.connect(self.reject)
        self.pb_submit.clicked.connect(self.process_entry)

    @qtc.Slot()
    def process_entry(self):
        title = self.le_title.text().strip()
        deadline = self.dte_deadline.dateTime()
        stringDate = deadline.toString("yyyy-MM-dd hh:mm:ss")

        if not title:
            self.lb_message.setText("Please, enter task title")
            self.le_title.setFocus()
            return

        if not deadline or deadline < datetime.datetime.now():
            self.lb_message.setText("Please, enter valid date")
            self.le_title.setFocus()
            return

        self.task_submited.emit(title, stringDate)
        self.lb_message.setText("New task added.")
        self.le_title.clear()
        self.le_title.setFocus()
        self.accept()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = AddTask()
    form.open()

    sys.exit(app.exec())