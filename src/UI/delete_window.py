# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_w_dialog(object):
    def setupUi(self, w_dialog):
        if not w_dialog.objectName():
            w_dialog.setObjectName(u"w_dialog")
        w_dialog.resize(320, 103)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_dialog.sizePolicy().hasHeightForWidth())
        w_dialog.setSizePolicy(sizePolicy)
        w_dialog.setMinimumSize(QSize(300, 45))
        w_dialog.setMaximumSize(QSize(320, 103))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        w_dialog.setFont(font)
        self.gridLayout = QGridLayout(w_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.pb_yes = QPushButton(w_dialog)
        self.pb_yes.setObjectName(u"pb_yes")

        self.horizontalLayout.addWidget(self.pb_yes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_no = QPushButton(w_dialog)
        self.pb_no.setObjectName(u"pb_no")

        self.horizontalLayout.addWidget(self.pb_no)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.lb_text = QLabel(w_dialog)
        self.lb_text.setObjectName(u"lb_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(30)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_text.sizePolicy().hasHeightForWidth())
        self.lb_text.setSizePolicy(sizePolicy1)
        self.lb_text.setMinimumSize(QSize(300, 45))
        self.lb_text.setMaximumSize(QSize(300, 45))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.lb_text.setFont(font1)
        self.lb_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_text, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(w_dialog)

        QMetaObject.connectSlotsByName(w_dialog)
    # setupUi

    def retranslateUi(self, w_dialog):
        w_dialog.setWindowTitle(QCoreApplication.translate("w_dialog", u"delete task", None))
        self.pb_yes.setText(QCoreApplication.translate("w_dialog", u"Yes \u2705", None))
        self.pb_no.setText(QCoreApplication.translate("w_dialog", u"No \u274c", None))
        self.lb_text.setText(QCoreApplication.translate("w_dialog", u"Are you sure you want to delete this task ?", None))
    # retranslateUi

