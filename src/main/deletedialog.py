import sys

from PySide6 import QtWidgets as qtw

from src.UI.delete_window import Ui_w_dialog

class DeleteDialog(qtw.QDialog, Ui_w_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_yes.clicked.connect(self.accept)
        self.pb_no.clicked.connect(self.reject)

if __name__ == "__main__":
    app = qtw.QApplication([])

    window = DeleteDialog()
    window.show()

    sys.exit(app.exec())