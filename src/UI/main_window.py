# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
from res import Icons_rc

class Ui_w_main_window(object):
    def setupUi(self, w_main_window):
        if not w_main_window.objectName():
            w_main_window.setObjectName(u"w_main_window")
        w_main_window.resize(710, 471)
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        w_main_window.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/good-morning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_main_window.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_main_window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(w_main_window)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_table = QTableView(self.groupBox)
        self.w_table.setObjectName(u"w_table")

        self.verticalLayout.addWidget(self.w_table)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.pb_remove = QPushButton(w_main_window)
        self.pb_remove.setObjectName(u"pb_remove")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_remove.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_remove, 2, 1, 1, 1)

        self.pb_add = QPushButton(w_main_window)
        self.pb_add.setObjectName(u"pb_add")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/add-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_add, 2, 0, 1, 1)

        QWidget.setTabOrder(self.pb_add, self.pb_remove)

        self.retranslateUi(w_main_window)

        QMetaObject.connectSlotsByName(w_main_window)
    # setupUi

    def retranslateUi(self, w_main_window):
        w_main_window.setWindowTitle(QCoreApplication.translate("w_main_window", u"time manager", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_main_window", u"Hello :)", None))
        self.pb_remove.setText(QCoreApplication.translate("w_main_window", u"REMOVE", None))
        self.pb_add.setText(QCoreApplication.translate("w_main_window", u"ADD", None))
    # retranslateUi

