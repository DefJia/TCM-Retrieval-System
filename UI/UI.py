# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1383, 888)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupboxSymptom = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxSymptom.setGeometry(QtCore.QRect(10, 80, 241, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxSymptom.setFont(font)
        self.groupboxSymptom.setObjectName("groupboxSymptom")
        self.lineSymptom = QtWidgets.QLineEdit(self.groupboxSymptom)
        self.lineSymptom.setGeometry(QtCore.QRect(20, 30, 161, 41))
        self.lineSymptom.setObjectName("lineSymptom")
        self.tablewidgetSymptom = QtWidgets.QTableWidget(self.groupboxSymptom)
        self.tablewidgetSymptom.setGeometry(QtCore.QRect(20, 80, 161, 321))
        self.tablewidgetSymptom.setObjectName("tablewidgetSymptom")
        self.tablewidgetSymptom.setColumnCount(0)
        self.tablewidgetSymptom.setRowCount(0)
        self.buttonSymptom = QtWidgets.QPushButton(self.groupboxSymptom)
        self.buttonSymptom.setGeometry(QtCore.QRect(180, 30, 41, 41))
        self.buttonSymptom.setObjectName("buttonSymptom")
        self.symptomOption = QtWidgets.QTableWidget(self.groupboxSymptom)
        self.symptomOption.setGeometry(QtCore.QRect(20, 70, 161, 271))
        self.symptomOption.setAutoFillBackground(False)
        self.symptomOption.setFrameShape(QtWidgets.QFrame.Box)
        self.symptomOption.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.symptomOption.setMidLineWidth(0)
        self.symptomOption.setObjectName("symptomOption")
        self.symptomOption.setColumnCount(0)
        self.symptomOption.setRowCount(0)
        self.symptomOption.horizontalHeader().setVisible(False)
        self.symptomOption.verticalHeader().setVisible(False)
        self.tablewidgetPrescribe = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidgetPrescribe.setGeometry(QtCore.QRect(30, 550, 881, 171))
        self.tablewidgetPrescribe.setObjectName("tablewidgetPrescribe")
        self.tablewidgetPrescribe.setColumnCount(0)
        self.tablewidgetPrescribe.setRowCount(0)
        self.tablewidgetBook = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidgetBook.setGeometry(QtCore.QRect(990, 100, 361, 741))
        self.tablewidgetBook.setObjectName("tablewidgetBook")
        self.tablewidgetBook.setColumnCount(0)
        self.tablewidgetBook.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, -10, 191, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupboxDisease = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxDisease.setGeometry(QtCore.QRect(220, 80, 251, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxDisease.setFont(font)
        self.groupboxDisease.setObjectName("groupboxDisease")
        self.lineDisease = QtWidgets.QLineEdit(self.groupboxDisease)
        self.lineDisease.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.lineDisease.setObjectName("lineDisease")
        self.tablewidgetDisease = QtWidgets.QTableWidget(self.groupboxDisease)
        self.tablewidgetDisease.setGeometry(QtCore.QRect(20, 80, 191, 321))
        self.tablewidgetDisease.setObjectName("tablewidgetDisease")
        self.tablewidgetDisease.setColumnCount(0)
        self.tablewidgetDisease.setRowCount(0)
        self.buttonDisease = QtWidgets.QPushButton(self.groupboxDisease)
        self.buttonDisease.setGeometry(QtCore.QRect(210, 30, 41, 41))
        self.buttonDisease.setObjectName("buttonDisease")
        self.diseaseOption = QtWidgets.QTableWidget(self.groupboxDisease)
        self.diseaseOption.setGeometry(QtCore.QRect(20, 70, 191, 271))
        self.diseaseOption.setFrameShape(QtWidgets.QFrame.Box)
        self.diseaseOption.setObjectName("diseaseOption")
        self.diseaseOption.setColumnCount(0)
        self.diseaseOption.setRowCount(0)
        self.groupboxPrescription = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxPrescription.setGeometry(QtCore.QRect(460, 80, 251, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxPrescription.setFont(font)
        self.groupboxPrescription.setObjectName("groupboxPrescription")
        self.linePrescription = QtWidgets.QLineEdit(self.groupboxPrescription)
        self.linePrescription.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.linePrescription.setObjectName("linePrescription")
        self.tablewidgetPrescription = QtWidgets.QTableWidget(self.groupboxPrescription)
        self.tablewidgetPrescription.setGeometry(QtCore.QRect(20, 80, 191, 321))
        self.tablewidgetPrescription.setObjectName("tablewidgetPrescription")
        self.tablewidgetPrescription.setColumnCount(0)
        self.tablewidgetPrescription.setRowCount(0)
        self.buttonPrescription = QtWidgets.QPushButton(self.groupboxPrescription)
        self.buttonPrescription.setGeometry(QtCore.QRect(210, 30, 41, 41))
        self.buttonPrescription.setObjectName("buttonPrescription")
        self.prescriptionOption = QtWidgets.QTableWidget(self.groupboxPrescription)
        self.prescriptionOption.setGeometry(QtCore.QRect(20, 70, 191, 271))
        self.prescriptionOption.setFrameShape(QtWidgets.QFrame.Box)
        self.prescriptionOption.setObjectName("prescriptionOption")
        self.prescriptionOption.setColumnCount(0)
        self.prescriptionOption.setRowCount(0)
        self.groupboxMedicine = QtWidgets.QGroupBox(self.centralwidget)
        self.groupboxMedicine.setGeometry(QtCore.QRect(700, 80, 271, 411))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.groupboxMedicine.setFont(font)
        self.groupboxMedicine.setObjectName("groupboxMedicine")
        self.lineMedicine = QtWidgets.QLineEdit(self.groupboxMedicine)
        self.lineMedicine.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.lineMedicine.setObjectName("lineMedicine")
        self.tablewidgetMedicine = QtWidgets.QTableWidget(self.groupboxMedicine)
        self.tablewidgetMedicine.setGeometry(QtCore.QRect(20, 80, 191, 321))
        self.tablewidgetMedicine.setObjectName("tablewidgetMedicine")
        self.tablewidgetMedicine.setColumnCount(0)
        self.tablewidgetMedicine.setRowCount(0)
        self.buttonMedicine = QtWidgets.QPushButton(self.groupboxMedicine)
        self.buttonMedicine.setGeometry(QtCore.QRect(210, 30, 41, 41))
        self.buttonMedicine.setObjectName("buttonMedicine")
        self.medicineOption = QtWidgets.QTableWidget(self.groupboxMedicine)
        self.medicineOption.setGeometry(QtCore.QRect(20, 70, 191, 271))
        self.medicineOption.setFrameShape(QtWidgets.QFrame.Box)
        self.medicineOption.setObjectName("medicineOption")
        self.medicineOption.setColumnCount(0)
        self.medicineOption.setRowCount(0)
        self.buttonInitial = QtWidgets.QPushButton(self.centralwidget)
        self.buttonInitial.setGeometry(QtCore.QRect(570, 490, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonInitial.setFont(font)
        self.buttonInitial.setObjectName("buttonInitial")
        self.buttonInput = QtWidgets.QPushButton(self.centralwidget)
        self.buttonInput.setGeometry(QtCore.QRect(750, 490, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonInput.setFont(font)
        self.buttonInput.setObjectName("buttonInput")
        self.buttonClean = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClean.setGeometry(QtCore.QRect(570, 730, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonClean.setFont(font)
        self.buttonClean.setObjectName("buttonClean")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(750, 850, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")
        self.lineBook = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBook.setGeometry(QtCore.QRect(1110, 40, 191, 41))
        self.lineBook.setObjectName("lineBook")
        self.labelPosition_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelPosition_2.setGeometry(QtCore.QRect(1000, 10, 191, 91))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.labelPosition_2.setFont(font)
        self.labelPosition_2.setObjectName("labelPosition_2")
        self.buttonClean_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClean_2.setGeometry(QtCore.QRect(750, 730, 161, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonClean_2.setFont(font)
        self.buttonClean_2.setObjectName("buttonClean_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(480, 40, 96, 24))
        font = QtGui.QFont()
        font.setFamily("Noto Serif CJK SC")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(590, 40, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Noto Serif CJK SC")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1383, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupboxSymptom.setTitle(_translate("MainWindow", "病症"))
        self.buttonSymptom.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "当前位置："))
        self.groupboxDisease.setTitle(_translate("MainWindow", "病名"))
        self.buttonDisease.setText(_translate("MainWindow", "+"))
        self.groupboxPrescription.setTitle(_translate("MainWindow", "药方"))
        self.buttonPrescription.setText(_translate("MainWindow", "+"))
        self.groupboxMedicine.setTitle(_translate("MainWindow", "药"))
        self.buttonMedicine.setText(_translate("MainWindow", "+"))
        self.buttonInitial.setText(_translate("MainWindow", "初始化"))
        self.buttonInput.setText(_translate("MainWindow", "录入"))
        self.buttonClean.setText(_translate("MainWindow", "清空"))
        self.buttonSave.setText(_translate("MainWindow", "保存"))
        self.labelPosition_2.setText(_translate("MainWindow", "典籍"))
        self.buttonClean_2.setText(_translate("MainWindow", "保存"))
        self.radioButton.setText(_translate("MainWindow", "录入模式"))
        self.radioButton_2.setText(_translate("MainWindow", "开方模式"))
        self.menu.setTitle(_translate("MainWindow", "智能中医开方检索系统"))

