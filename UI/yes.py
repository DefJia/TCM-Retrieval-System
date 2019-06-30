# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yes.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Yes(object):
    def setupUi(self, Yes):
        Yes.setObjectName("Yes")
        Yes.resize(383, 197)
        self.centralwidget = QtWidgets.QWidget(Yes)
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
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.yesButton.setFont(font)
        self.yesButton.setObjectName("yesButton")
        self.gridLayout.addWidget(self.yesButton, 1, 0, 1, 1)
        Yes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Yes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 25))
        self.menubar.setObjectName("menubar")
        Yes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Yes)
        self.statusbar.setObjectName("statusbar")
        Yes.setStatusBar(self.statusbar)

        self.retranslateUi(Yes)
        QtCore.QMetaObject.connectSlotsByName(Yes)

    def retranslateUi(self, Yes):
        _translate = QtCore.QCoreApplication.translate
        Yes.setWindowTitle(_translate("Yes", "MainWindow"))
        self.label.setText(_translate("Yes", "      操作成功"))
        self.yesButton.setText(_translate("Yes", "确定"))
        self.yesButton.setShortcut(_translate("Yes", "Return"))

