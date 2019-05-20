# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_final(object):
    def setupUi(self, final):
        final.setObjectName("final")
        final.resize(546, 347)
        self.centralwidget = QtWidgets.QWidget(final)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        final.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(final)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 25))
        self.menubar.setObjectName("menubar")
        final.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(final)
        self.statusbar.setObjectName("statusbar")
        final.setStatusBar(self.statusbar)

        self.retranslateUi(final)
        QtCore.QMetaObject.connectSlotsByName(final)

    def retranslateUi(self, final):
        _translate = QtCore.QCoreApplication.translate
        final.setWindowTitle(_translate("final", "MainWindow"))
        self.label.setText(_translate("final", "信息保存成功"))
        self.label_2.setText(_translate("final", "是否需要继续开方"))
        self.pushButton.setText(_translate("final", "继续开方"))
        self.pushButton_2.setText(_translate("final", "退出系统"))

