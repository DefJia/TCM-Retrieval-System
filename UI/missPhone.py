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
        missPhone.resize(422, 273)
        self.centralwidget = QtWidgets.QWidget(missPhone)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(22)
        self.yesButton.setFont(font)
        self.yesButton.setObjectName("yesButton")
        self.gridLayout.addWidget(self.yesButton, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
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
        self.label_2.setText(_translate("missPhone", "     或身份证号"))
        self.yesButton.setText(_translate("missPhone", "确定"))
        self.yesButton.setShortcut(_translate("missPhone", "Return"))
        self.label.setText(_translate("missPhone", "   请输入手机号"))

