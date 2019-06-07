# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relationDelete.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_relationDelete(object):
    def setupUi(self, relationDelete):
        relationDelete.setObjectName("relationDelete")
        relationDelete.resize(430, 335)
        self.centralwidget = QtWidgets.QWidget(relationDelete)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.buttonYes = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.buttonYes.setFont(font)
        self.buttonYes.setObjectName("buttonYes")
        self.gridLayout.addWidget(self.buttonYes, 3, 0, 1, 1)
        self.buttonNo = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        self.buttonNo.setFont(font)
        self.buttonNo.setObjectName("buttonNo")
        self.gridLayout.addWidget(self.buttonNo, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        relationDelete.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(relationDelete)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 25))
        self.menubar.setObjectName("menubar")
        relationDelete.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(relationDelete)
        self.statusbar.setObjectName("statusbar")
        relationDelete.setStatusBar(self.statusbar)

        self.retranslateUi(relationDelete)
        QtCore.QMetaObject.connectSlotsByName(relationDelete)

    def retranslateUi(self, relationDelete):
        _translate = QtCore.QCoreApplication.translate
        relationDelete.setWindowTitle(_translate("relationDelete", "MainWindow"))
        self.label.setText(_translate("relationDelete", "      确定删除"))
        self.label_2.setText(_translate("relationDelete", "      的联系吗"))
        self.buttonYes.setText(_translate("relationDelete", "是的"))
        self.buttonNo.setText(_translate("relationDelete", "取消"))
        self.label_3.setText(_translate("relationDelete", "病症-病名-药方-药"))

