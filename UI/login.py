# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(432, 317)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUser.setGeometry(QtCore.QRect(200, 60, 161, 41))
        self.lineUser.setObjectName("lineUser")
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(200, 170, 161, 41))
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setObjectName("linePassword")
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesButton.setGeometry(QtCore.QRect(50, 240, 93, 28))
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(self.centralwidget)
        self.noButton.setGeometry(QtCore.QRect(240, 240, 93, 28))
        self.noButton.setObjectName("noButton")
        LogIn.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogIn)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 25))
        self.menubar.setObjectName("menubar")
        LogIn.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogIn)
        self.statusbar.setObjectName("statusbar")
        LogIn.setStatusBar(self.statusbar)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "MainWindow"))
        self.label.setText(_translate("LogIn", "用户名"))
        self.label_2.setText(_translate("LogIn", "密码"))
        self.yesButton.setText(_translate("LogIn", "确定"))
        self.noButton.setText(_translate("LogIn", "取消"))

