# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1_Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QAbstractItemView
from PyQt5 import QtCore, QtGui, QtWidgets

class Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1026, 512)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_out.setGeometry(QtCore.QRect(830, 410, 93, 28))
        self.pushButton_out.setObjectName("pushButton_out")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 311, 351))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_bingzheng = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_bingzheng.setGeometry(QtCore.QRect(20, 40, 113, 21))
        self.lineEdit_bingzheng.setObjectName("lineEdit_bingzheng")
        self.pushButton_bingzheng = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_bingzheng.setGeometry(QtCore.QRect(30, 80, 93, 28))
        self.pushButton_bingzheng.setObjectName("pushButton_bingzheng")

        self.tableWidget_yaofang = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_yaofang.setGeometry(QtCore.QRect(190, 40, 111, 281))
        self.tableWidget_yaofang.setObjectName("tableWidget_yaofang")
        self.tableWidget_yaofang.setColumnCount(1)
        self.tableWidget_yaofang.setRowCount(1)
        self.tableWidget_yaofang.setEditTriggers(QAbstractItemView.NoEditTriggers)
#        self.tableWidget_yaofang.setSelectionBehavior(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_yaofang.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_yaofang.verticalHeader().setVisible(False)
        self.tableWidget_yaofang.horizontalHeader().setVisible(False)


        self.pushButton_daoru = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_daoru.setGeometry(QtCore.QRect(40, 310, 93, 28))
        self.pushButton_daoru.setObjectName("pushButton_daoru")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 40, 561, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)


        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 501, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)


        self.pushButton_dayin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dayin.setGeometry(QtCore.QRect(700, 410, 93, 28))
        self.pushButton_dayin.setObjectName("pushButton_dayin")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 26))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.pushButton_out.setText(_translate("Main", "退出"))
        self.groupBox.setTitle(_translate("Main", "病症—药方检索"))
        self.pushButton_bingzheng.setText(_translate("Main", "搜索"))
        self.pushButton_daoru.setText(_translate("Main", "导入"))
        self.groupBox_2.setTitle(_translate("Main", "药名"))
        self.pushButton_dayin.setText(_translate("Main", "打印"))

class M(QMainWindow, Main):
    def __init__(self):
        super(M, self).__init__()
        self.setupUi(self)

    def open(self):
        self.show()

    def close(self):
        self.hide()
