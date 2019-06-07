# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reminder.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reminder(object):
    def setupUi(self, reminder):
        reminder.setObjectName("reminder")
        reminder.resize(397, 247)
        self.centralwidget = QtWidgets.QWidget(reminder)
        self.centralwidget.setObjectName("centralwidget")
        self.labelType = QtWidgets.QLabel(self.centralwidget)
        self.labelType.setGeometry(QtCore.QRect(30, 20, 351, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.labelType.setFont(font)
        self.labelType.setToolTip("")
        self.labelType.setObjectName("labelType")
        self.buttonYes = QtWidgets.QPushButton(self.centralwidget)
        self.buttonYes.setGeometry(QtCore.QRect(80, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(11)
        self.buttonYes.setFont(font)
        self.buttonYes.setObjectName("buttonYes")
        self.buttonNo = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNo.setGeometry(QtCore.QRect(220, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(11)
        self.buttonNo.setFont(font)
        self.buttonNo.setObjectName("buttonNo")
        reminder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(reminder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 25))
        self.menubar.setObjectName("menubar")
        reminder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(reminder)
        self.statusbar.setObjectName("statusbar")
        reminder.setStatusBar(self.statusbar)

        self.retranslateUi(reminder)
        QtCore.QMetaObject.connectSlotsByName(reminder)

    def retranslateUi(self, reminder):
        _translate = QtCore.QCoreApplication.translate
        reminder.setWindowTitle(_translate("reminder", "提示"))
        self.labelType.setText(_translate("reminder", "是否确定加入数据库"))
        self.buttonYes.setText(_translate("reminder", "确定"))
        self.buttonNo.setText(_translate("reminder", "取消"))

