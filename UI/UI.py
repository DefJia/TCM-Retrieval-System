# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1314, 846)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 9999999))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1301, 781))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonClean = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonClean.setFont(font)
        self.buttonClean.setObjectName("buttonClean")
        self.gridLayout.addWidget(self.buttonClean, 8, 8, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 22, 1, 1)
        self.tablewidgetPrescribe = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tablewidgetPrescribe.setObjectName("tablewidgetPrescribe")
        self.tablewidgetPrescribe.setColumnCount(8)
        self.tablewidgetPrescribe.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescribe.setItem(3, 0, item)
        self.tablewidgetPrescribe.verticalHeader().setVisible(False)
        self.tablewidgetPrescribe.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.tablewidgetPrescribe, 5, 0, 1, 24)
        spacerItem1 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 10, 1, 1)
        self.tablewidgetBook = QtWidgets.QTableWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tablewidgetBook.setFont(font)
        self.tablewidgetBook.setObjectName("tablewidgetBook")
        self.tablewidgetBook.setColumnCount(0)
        self.tablewidgetBook.setRowCount(0)
        self.gridLayout.addWidget(self.tablewidgetBook, 2, 24, 4, 1)
        self.buttonDelete = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonDelete.setFont(font)
        self.buttonDelete.setObjectName("buttonDelete")
        self.gridLayout.addWidget(self.buttonDelete, 4, 2, 1, 1)
        self.buttonInitial = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonInitial.setFont(font)
        self.buttonInitial.setObjectName("buttonInitial")
        self.gridLayout.addWidget(self.buttonInitial, 4, 8, 1, 1)
        self.buttonInput = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonInput.setFont(font)
        self.buttonInput.setObjectName("buttonInput")
        self.gridLayout.addWidget(self.buttonInput, 4, 14, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 16, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 15, 1, 1)
        self.labelPosition_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.labelPosition_2.setFont(font)
        self.labelPosition_2.setObjectName("labelPosition_2")
        self.gridLayout.addWidget(self.labelPosition_2, 0, 24, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 19, 1, 1)
        self.buttonDeleterelation = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonDeleterelation.setFont(font)
        self.buttonDeleterelation.setObjectName("buttonDeleterelation")
        self.gridLayout.addWidget(self.buttonDeleterelation, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 17, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 20, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 14, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 18, 1, 1)
        self.lineBook = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(24)
        self.lineBook.setFont(font)
        self.lineBook.setObjectName("lineBook")
        self.gridLayout.addWidget(self.lineBook, 1, 24, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 13, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 21, 1, 1)
        self.buttonOut = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buttonOut.setFont(font)
        self.buttonOut.setObjectName("buttonOut")
        self.gridLayout.addWidget(self.buttonOut, 8, 24, 1, 1)
        self.labelType = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(28)
        self.labelType.setFont(font)
        self.labelType.setObjectName("labelType")
        self.gridLayout.addWidget(self.labelType, 0, 2, 1, 1)
        self.buttonSave = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")
        self.gridLayout.addWidget(self.buttonSave, 8, 14, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 11, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 0, 9, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 0, 12, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 8, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 21, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 3, 22, 1, 1)
        self.groupboxSymptom = QtWidgets.QGroupBox(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupboxSymptom.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.groupboxSymptom.setFont(font)
        self.groupboxSymptom.setObjectName("groupboxSymptom")
        self.lineSymptom = QtWidgets.QLineEdit(self.groupboxSymptom)
        self.lineSymptom.setGeometry(QtCore.QRect(10, 40, 161, 41))
        self.lineSymptom.setObjectName("lineSymptom")
        self.tablewidgetSymptom = QtWidgets.QTableWidget(self.groupboxSymptom)
        self.tablewidgetSymptom.setGeometry(QtCore.QRect(10, 90, 161, 321))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tablewidgetSymptom.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tablewidgetSymptom.setFont(font)
        self.tablewidgetSymptom.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidgetSymptom.setObjectName("tablewidgetSymptom")
        self.tablewidgetSymptom.setColumnCount(0)
        self.tablewidgetSymptom.setRowCount(0)
        self.tablewidgetSymptom.horizontalHeader().setVisible(False)
        self.tablewidgetSymptom.horizontalHeader().setDefaultSectionSize(161)
        self.tablewidgetSymptom.verticalHeader().setVisible(False)
        self.buttonSymptom = QtWidgets.QPushButton(self.groupboxSymptom)
        self.buttonSymptom.setGeometry(QtCore.QRect(170, 40, 41, 41))
        self.buttonSymptom.setObjectName("buttonSymptom")
        self.symptomOption = QtWidgets.QTableWidget(self.groupboxSymptom)
        self.symptomOption.setGeometry(QtCore.QRect(10, 80, 161, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.symptomOption.setFont(font)
        self.symptomOption.setAutoFillBackground(False)
        self.symptomOption.setFrameShape(QtWidgets.QFrame.Box)
        self.symptomOption.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.symptomOption.setMidLineWidth(0)
        self.symptomOption.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.symptomOption.setObjectName("symptomOption")
        self.symptomOption.setColumnCount(0)
        self.symptomOption.setRowCount(0)
        self.symptomOption.horizontalHeader().setVisible(False)
        self.symptomOption.horizontalHeader().setDefaultSectionSize(161)
        self.symptomOption.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.groupboxSymptom, 1, 0, 3, 1)
        self.groupboxDisease = QtWidgets.QGroupBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.groupboxDisease.setFont(font)
        self.groupboxDisease.setObjectName("groupboxDisease")
        self.lineDisease = QtWidgets.QLineEdit(self.groupboxDisease)
        self.lineDisease.setGeometry(QtCore.QRect(10, 40, 161, 41))
        self.lineDisease.setObjectName("lineDisease")
        self.tablewidgetDisease = QtWidgets.QTableWidget(self.groupboxDisease)
        self.tablewidgetDisease.setGeometry(QtCore.QRect(10, 90, 161, 321))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(204, 255, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 255, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tablewidgetDisease.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tablewidgetDisease.setFont(font)
        self.tablewidgetDisease.setAutoFillBackground(True)
        self.tablewidgetDisease.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidgetDisease.setObjectName("tablewidgetDisease")
        self.tablewidgetDisease.setColumnCount(0)
        self.tablewidgetDisease.setRowCount(0)
        self.tablewidgetDisease.horizontalHeader().setVisible(False)
        self.tablewidgetDisease.horizontalHeader().setDefaultSectionSize(191)
        self.tablewidgetDisease.verticalHeader().setVisible(False)
        self.buttonDisease = QtWidgets.QPushButton(self.groupboxDisease)
        self.buttonDisease.setGeometry(QtCore.QRect(170, 40, 41, 41))
        self.buttonDisease.setObjectName("buttonDisease")
        self.diseaseOption = QtWidgets.QTableWidget(self.groupboxDisease)
        self.diseaseOption.setGeometry(QtCore.QRect(10, 80, 161, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.diseaseOption.setFont(font)
        self.diseaseOption.setFrameShape(QtWidgets.QFrame.Box)
        self.diseaseOption.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.diseaseOption.setObjectName("diseaseOption")
        self.diseaseOption.setColumnCount(0)
        self.diseaseOption.setRowCount(0)
        self.diseaseOption.horizontalHeader().setVisible(False)
        self.diseaseOption.horizontalHeader().setDefaultSectionSize(191)
        self.diseaseOption.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.groupboxDisease, 1, 2, 3, 5)
        self.groupboxPrescription = QtWidgets.QGroupBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.groupboxPrescription.setFont(font)
        self.groupboxPrescription.setObjectName("groupboxPrescription")
        self.linePrescription = QtWidgets.QLineEdit(self.groupboxPrescription)
        self.linePrescription.setGeometry(QtCore.QRect(10, 40, 191, 41))
        self.linePrescription.setObjectName("linePrescription")
        self.tablewidgetPrescription = QtWidgets.QTableWidget(self.groupboxPrescription)
        self.tablewidgetPrescription.setGeometry(QtCore.QRect(10, 90, 191, 321))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(204, 255, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 255, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tablewidgetPrescription.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tablewidgetPrescription.setFont(font)
        self.tablewidgetPrescription.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidgetPrescription.setObjectName("tablewidgetPrescription")
        self.tablewidgetPrescription.setColumnCount(2)
        self.tablewidgetPrescription.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescription.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescription.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescription.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescription.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetPrescription.setItem(0, 1, item)
        self.tablewidgetPrescription.horizontalHeader().setVisible(False)
        self.tablewidgetPrescription.horizontalHeader().setDefaultSectionSize(191)
        self.tablewidgetPrescription.verticalHeader().setVisible(False)
        self.buttonPrescription = QtWidgets.QPushButton(self.groupboxPrescription)
        self.buttonPrescription.setGeometry(QtCore.QRect(200, 40, 41, 41))
        self.buttonPrescription.setObjectName("buttonPrescription")
        self.prescriptionOption = QtWidgets.QTableWidget(self.groupboxPrescription)
        self.prescriptionOption.setGeometry(QtCore.QRect(10, 80, 191, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prescriptionOption.setFont(font)
        self.prescriptionOption.setFrameShape(QtWidgets.QFrame.Box)
        self.prescriptionOption.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.prescriptionOption.setObjectName("prescriptionOption")
        self.prescriptionOption.setColumnCount(0)
        self.prescriptionOption.setRowCount(0)
        self.prescriptionOption.horizontalHeader().setVisible(False)
        self.prescriptionOption.horizontalHeader().setDefaultSectionSize(191)
        self.prescriptionOption.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.groupboxPrescription, 1, 8, 3, 6)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 2, 22, 1, 1)
        self.groupboxMedicine = QtWidgets.QGroupBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.groupboxMedicine.setFont(font)
        self.groupboxMedicine.setObjectName("groupboxMedicine")
        self.lineMedicine = QtWidgets.QLineEdit(self.groupboxMedicine)
        self.lineMedicine.setGeometry(QtCore.QRect(10, 40, 191, 41))
        self.lineMedicine.setObjectName("lineMedicine")
        self.tablewidgetMedicine = QtWidgets.QTableWidget(self.groupboxMedicine)
        self.tablewidgetMedicine.setGeometry(QtCore.QRect(10, 90, 191, 321))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(204, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tablewidgetMedicine.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tablewidgetMedicine.setFont(font)
        self.tablewidgetMedicine.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidgetMedicine.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidgetMedicine.setObjectName("tablewidgetMedicine")
        self.tablewidgetMedicine.setColumnCount(2)
        self.tablewidgetMedicine.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetMedicine.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetMedicine.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetMedicine.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablewidgetMedicine.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetMedicine.setItem(0, 1, item)
        self.tablewidgetMedicine.horizontalHeader().setVisible(False)
        self.tablewidgetMedicine.horizontalHeader().setCascadingSectionResizes(False)
        self.tablewidgetMedicine.horizontalHeader().setDefaultSectionSize(93)
        self.tablewidgetMedicine.horizontalHeader().setSortIndicatorShown(False)
        self.tablewidgetMedicine.verticalHeader().setVisible(False)
        self.tablewidgetMedicine.verticalHeader().setCascadingSectionResizes(False)
        self.buttonMedicine = QtWidgets.QPushButton(self.groupboxMedicine)
        self.buttonMedicine.setGeometry(QtCore.QRect(200, 40, 41, 41))
        self.buttonMedicine.setObjectName("buttonMedicine")
        self.medicineOption = QtWidgets.QTableWidget(self.groupboxMedicine)
        self.medicineOption.setGeometry(QtCore.QRect(10, 80, 191, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.medicineOption.setFont(font)
        self.medicineOption.setFrameShape(QtWidgets.QFrame.Box)
        self.medicineOption.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.medicineOption.setObjectName("medicineOption")
        self.medicineOption.setColumnCount(0)
        self.medicineOption.setRowCount(0)
        self.medicineOption.horizontalHeader().setVisible(False)
        self.medicineOption.horizontalHeader().setDefaultSectionSize(191)
        self.medicineOption.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.groupboxMedicine, 1, 14, 3, 8)
        self.gridLayout.setRowStretch(0, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1314, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能中医开放检索系统"))
        self.buttonClean.setText(_translate("MainWindow", "清空"))
        self.tablewidgetPrescribe.setSortingEnabled(False)
        item = self.tablewidgetPrescribe.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescribe.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescribe.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescribe.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescribe.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescribe.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescribe.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "药"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "克数"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "药"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "克数"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "药"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "克数"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "药"))
        item = self.tablewidgetPrescribe.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "克数"))
        __sortingEnabled = self.tablewidgetPrescribe.isSortingEnabled()
        self.tablewidgetPrescribe.setSortingEnabled(False)
        self.tablewidgetPrescribe.setSortingEnabled(__sortingEnabled)
        self.buttonDelete.setText(_translate("MainWindow", "删除"))
        self.buttonInitial.setText(_translate("MainWindow", "初始化"))
        self.buttonInput.setText(_translate("MainWindow", "录入"))
        self.labelPosition_2.setText(_translate("MainWindow", "典籍"))
        self.buttonDeleterelation.setText(_translate("MainWindow", "删除关系"))
        self.radioButton_2.setText(_translate("MainWindow", "开方模式"))
        self.label_4.setText(_translate("MainWindow", "       "))
        self.label_5.setText(_translate("MainWindow", "     "))
        self.buttonOut.setText(_translate("MainWindow", "退出"))
        self.labelType.setText(_translate("MainWindow", "开方模式"))
        self.buttonSave.setText(_translate("MainWindow", "保存"))
        self.label.setText(_translate("MainWindow", "当前位置："))
        self.radioButton.setText(_translate("MainWindow", "录入模式"))
        self.groupboxSymptom.setTitle(_translate("MainWindow", "病症"))
        self.buttonSymptom.setText(_translate("MainWindow", "+"))
        self.groupboxDisease.setTitle(_translate("MainWindow", "病名"))
        self.buttonDisease.setText(_translate("MainWindow", "+"))
        self.groupboxPrescription.setTitle(_translate("MainWindow", "药方"))
        item = self.tablewidgetPrescription.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetPrescription.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tablewidgetPrescription.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.tablewidgetPrescription.isSortingEnabled()
        self.tablewidgetPrescription.setSortingEnabled(False)
        self.tablewidgetPrescription.setSortingEnabled(__sortingEnabled)
        self.buttonPrescription.setText(_translate("MainWindow", "+"))
        self.groupboxMedicine.setTitle(_translate("MainWindow", "药"))
        item = self.tablewidgetMedicine.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tablewidgetMedicine.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tablewidgetMedicine.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.tablewidgetMedicine.isSortingEnabled()
        self.tablewidgetMedicine.setSortingEnabled(False)
        self.tablewidgetMedicine.setSortingEnabled(__sortingEnabled)
        self.buttonMedicine.setText(_translate("MainWindow", "+"))

