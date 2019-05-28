# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'missPhone.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_missPhone(object):
    def setupUi(self, missPhone):
        missPhone.setObjectName("missPhone")
        missPhone.resize(422, 238)
        self.centralwidget = QtWidgets.QWidget(missPhone)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesButton.setGeometry(QtCore.QRect(160, 110, 93, 28))
        self.yesButton.setObjectName("yesButton")
        missPhone.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(missPhone)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 25))
        self.menubar.setObjectName("menubar")
        missPhone.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(missPhone)
        self.statusbar.setObjectName("statusbar")
        missPhone.setStatusBar(self.statusbar)

        self.retranslateUi(missPhone)
        QtCore.QMetaObject.connectSlotsByName(missPhone)

    def retranslateUi(self, missPhone):
        _translate = QtCore.QCoreApplication.translate
        missPhone.setWindowTitle(_translate("missPhone", "MainWindow"))
        self.label.setText(_translate("missPhone", "请输入手机号"))
        self.yesButton.setText(_translate("missPhone", "确定"))

