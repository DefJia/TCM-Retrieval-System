# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'property.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Property(object):
    def setupUi(self, Property):
        Property.setObjectName("Property")
        Property.resize(393, 293)
        self.centralwidget = QtWidgets.QWidget(Property)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 261, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        Property.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Property)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 25))
        self.menubar.setObjectName("menubar")
        Property.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Property)
        self.statusbar.setObjectName("statusbar")
        Property.setStatusBar(self.statusbar)

        self.retranslateUi(Property)
        QtCore.QMetaObject.connectSlotsByName(Property)

    def retranslateUi(self, Property):
        _translate = QtCore.QCoreApplication.translate
        Property.setWindowTitle(_translate("Property", "属性"))
        self.label.setText(_translate("Property", "请选择药材属性"))
        self.comboBox.setItemText(0, _translate("Property", "先煎"))
        self.comboBox.setItemText(1, _translate("Property", "后下"))
        self.comboBox.setItemText(2, _translate("Property", "包煎"))
        self.comboBox.setItemText(3, _translate("Property", "冲服"))
        self.comboBox.setItemText(4, _translate("Property", "烊化"))
        self.pushButton.setText(_translate("Property", "确定"))

