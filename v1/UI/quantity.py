# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quantity.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_quantity(object):
    def setupUi(self, quantity):
        quantity.setObjectName("quantity")
        quantity.resize(429, 201)
        self.centralwidget = QtWidgets.QWidget(quantity)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineQuantity = QtWidgets.QLineEdit(self.centralwidget)
        self.lineQuantity.setGeometry(QtCore.QRect(210, 40, 171, 41))
        self.lineQuantity.setObjectName("lineQuantity")
        quantity.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(quantity)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 25))
        self.menubar.setObjectName("menubar")
        quantity.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(quantity)
        self.statusbar.setObjectName("statusbar")
        quantity.setStatusBar(self.statusbar)

        self.retranslateUi(quantity)
        QtCore.QMetaObject.connectSlotsByName(quantity)

    def retranslateUi(self, quantity):
        _translate = QtCore.QCoreApplication.translate
        quantity.setWindowTitle(_translate("quantity", "MainWindow"))
        self.pushButton.setText(_translate("quantity", "确定"))
        self.label.setText(_translate("quantity", "克数"))

