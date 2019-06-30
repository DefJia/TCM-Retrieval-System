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
        LogIn.resize(390, 263)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineUser = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(18)
        self.lineUser.setFont(font)
        self.lineUser.setObjectName("lineUser")
        self.gridLayout.addWidget(self.lineUser, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(18)
        self.linePassword.setFont(font)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setObjectName("linePassword")
        self.gridLayout.addWidget(self.linePassword, 1, 1, 1, 2)
        self.noButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(18)
        self.noButton.setFont(font)
        self.noButton.setObjectName("noButton")
        self.gridLayout.addWidget(self.noButton, 2, 2, 1, 1)
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(18)
        self.yesButton.setFont(font)
        self.yesButton.setObjectName("yesButton")
        self.gridLayout.addWidget(self.yesButton, 2, 1, 1, 1)
        LogIn.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogIn)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 25))
        self.menubar.setObjectName("menubar")
        LogIn.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogIn)
        self.statusbar.setObjectName("statusbar")
        LogIn.setStatusBar(self.statusbar)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "登录界面"))
        self.label.setText(_translate("LogIn", "用户名"))
        self.label_2.setText(_translate("LogIn", "密码"))
        self.noButton.setText(_translate("LogIn", "取消"))
        self.noButton.setShortcut(_translate("LogIn", "Esc"))
        self.yesButton.setText(_translate("LogIn", "确定"))
        self.yesButton.setShortcut(_translate("LogIn", "Return"))

