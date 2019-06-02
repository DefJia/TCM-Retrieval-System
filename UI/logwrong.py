# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logwrong.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LogWrong(object):
    def setupUi(self, LogWrong):
        LogWrong.setObjectName("LogWrong")
        LogWrong.resize(422, 238)
        self.centralwidget = QtWidgets.QWidget(LogWrong)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesButton.setGeometry(QtCore.QRect(160, 130, 93, 28))
        self.yesButton.setObjectName("yesButton")
        LogWrong.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogWrong)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 25))
        self.menubar.setObjectName("menubar")
        LogWrong.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogWrong)
        self.statusbar.setObjectName("statusbar")
        LogWrong.setStatusBar(self.statusbar)

        self.retranslateUi(LogWrong)
        QtCore.QMetaObject.connectSlotsByName(LogWrong)

    def retranslateUi(self, LogWrong):
        _translate = QtCore.QCoreApplication.translate
        LogWrong.setWindowTitle(_translate("LogWrong", "MainWindow"))
        self.label.setText(_translate("LogWrong", "账号或密码错误"))
        self.yesButton.setText(_translate("LogWrong", "确定"))

