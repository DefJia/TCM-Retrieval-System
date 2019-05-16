# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_final_2(object):
    def setupUi(self, final_2):
        final_2.setObjectName("final_2")
        final_2.resize(546, 347)
        self.centralwidget = QtWidgets.QWidget(final_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.buttonContinue = QtWidgets.QPushButton(self.centralwidget)
        self.buttonContinue.setGeometry(QtCore.QRect(80, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.buttonContinue.setFont(font)
        self.buttonContinue.setObjectName("buttonContinue")
        self.buttonOut = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOut.setGeometry(QtCore.QRect(310, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.buttonOut.setFont(font)
        self.buttonOut.setObjectName("buttonOut")
        final_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(final_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 25))
        self.menubar.setObjectName("menubar")
        final_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(final_2)
        self.statusbar.setObjectName("statusbar")
        final_2.setStatusBar(self.statusbar)

        self.retranslateUi(final_2)
        QtCore.QMetaObject.connectSlotsByName(final_2)

    def retranslateUi(self, final_2):
        _translate = QtCore.QCoreApplication.translate
        final_2.setWindowTitle(_translate("final_2", "MainWindow"))
        self.label.setText(_translate("final_2", "信息保存成功"))
        self.label_2.setText(_translate("final_2", "是否需要继续开方"))
        self.buttonContinue.setText(_translate("final_2", "继续开方"))
        self.buttonOut.setText(_translate("final_2", "退出系统"))

