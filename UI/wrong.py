# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wrong.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wrong(object):
    def setupUi(self, Wrong):
        Wrong.setObjectName("Wrong")
        Wrong.resize(310, 143)
        self.centralwidget = QtWidgets.QWidget(Wrong)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 72, 15))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        Wrong.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Wrong)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 25))
        self.menubar.setObjectName("menubar")
        Wrong.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Wrong)
        self.statusbar.setObjectName("statusbar")
        Wrong.setStatusBar(self.statusbar)

        self.retranslateUi(Wrong)
        QtCore.QMetaObject.connectSlotsByName(Wrong)

    def retranslateUi(self, Wrong):
        _translate = QtCore.QCoreApplication.translate
        Wrong.setWindowTitle(_translate("Wrong", "MainWindow"))
        self.label.setText(_translate("Wrong", "密码错误"))
        self.pushButton.setText(_translate("Wrong", "确定"))
        self.pushButton.setShortcut(_translate("Wrong", "Return"))

