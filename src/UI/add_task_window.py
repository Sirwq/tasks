# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_task_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
from res import Icons_rc

class Ui_d_createTask(object):
    def setupUi(self, d_createTask):
        if not d_createTask.objectName():
            d_createTask.setObjectName(u"d_createTask")
        d_createTask.setWindowModality(Qt.WindowModality.ApplicationModal)
        d_createTask.resize(368, 190)
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        d_createTask.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/good-morning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        d_createTask.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_createTask)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_message = QLabel(d_createTask)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 3, 0, 1, 2)

        self.groupBox = QGroupBox(d_createTask)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QSize(350, 103))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.le_title = QLineEdit(self.groupBox)
        self.le_title.setObjectName(u"le_title")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_title)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.dte_deadline = QDateTimeEdit(self.groupBox)
        self.dte_deadline.setObjectName(u"dte_deadline")
        self.dte_deadline.setWrapping(False)
        self.dte_deadline.setDateTime(QDateTime(QDate(2025, 10, 14), QTime(0, 0, 0)))
        self.dte_deadline.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dte_deadline)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.pb_submit = QPushButton(d_createTask)
        self.pb_submit.setObjectName(u"pb_submit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/add-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_submit.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_submit, 2, 0, 1, 1)

        self.pb_close = QPushButton(d_createTask)
        self.pb_close.setObjectName(u"pb_close")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_close.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_close, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        QWidget.setTabOrder(self.le_title, self.dte_deadline)
        QWidget.setTabOrder(self.dte_deadline, self.pb_submit)
        QWidget.setTabOrder(self.pb_submit, self.pb_close)

        self.retranslateUi(d_createTask)

        QMetaObject.connectSlotsByName(d_createTask)
    # setupUi

    def retranslateUi(self, d_createTask):
        d_createTask.setWindowTitle(QCoreApplication.translate("d_createTask", u"add task", None))
        self.lb_message.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("d_createTask", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("d_createTask", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("d_createTask", u"Deadline", None))
        self.dte_deadline.setDisplayFormat(QCoreApplication.translate("d_createTask", u"d/M/yyyy hh:mm", None))
        self.pb_submit.setText(QCoreApplication.translate("d_createTask", u"SUBMIT", None))
        self.pb_close.setText(QCoreApplication.translate("d_createTask", u"CLOSE", None))
    # retranslateUi

