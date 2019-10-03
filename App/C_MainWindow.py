from App.M_MainWindow import M_MainWindow
from App.V_MainWindow import V_MainWindow
from App.General import *

from PyQt5.QtWidgets import QApplication
import sys


class C_MainWindow:
    def __init__(self):
        self.view = V_MainWindow()
        self.model = M_MainWindow(self.view)
        # init
        self.additions()
        self.inputs()
        self.tables()
        self.options()
        self.radioboxs()
        self.buttons()
        # show

    def additions(self):
        self.view.interface.buttonSymptom.clicked.connect(lambda: self.model.addition_clicked(0))
        self.view.interface.buttonDisease.clicked.connect(lambda: self.model.addition_clicked(1))
        self.view.interface.buttonPrescription.clicked.connect(lambda: self.model.addition_clicked(2))
        self.view.interface.buttonMedicine.clicked.connect(lambda: self.model.addition_clicked(3))

    def inputs(self):
        self.view.interface.lineSymptom.textChanged.connect(lambda: self.model.input_changed(0, self.view.interface.lineSymptom.text()))
        self.view.interface.lineDisease.textChanged.connect(lambda: self.model.input_changed(1, self.view.interface.lineDisease.text()))
        self.view.interface.linePrescription.textChanged.connect(lambda: self.model.input_changed(2, self.view.interface.Prescription.text()))
        self.view.interface.lineMedicine.textChanged.connect(lambda: self.model.input_changed(3, self.view.interface.lineMedicine.text()))
        
    def tables(self):
        self.view.interface.tablewidgetSymptom.clicked.connect(lambda: self.model.table_clicked(0))
        self.view.interface.tablewidgetDisease.clicked.connect(lambda: self.model.table_clicked(1))
        self.view.interface.tablewidgetPrescription.clicked.connect(lambda: self.model.table_clicked(2))
        self.view.interface.tablewidgetMedicine.clicked.connect(lambda: self.model.table_clicked(3))

    def options(self):
        self.view.interface.symptomOption.clicked.connect(lambda: self.model.option_clicked(0))
        self.view.interface.diseaseOption.clicked.connect(lambda: self.model.option_clicked(1))
        self.view.interface.prescriptionOption.clicked.connect(lambda: self.model.option_clicked(2))
        self.view.interface.medicineOption.clicked.connect(lambda: self.model.option_clicked(3))

    def radioboxs(self):
        self.view.interface.radioButton_2.toggled.connect(lambda: self.model.radiobox_changed())

    def buttons(self):
        self.view.interface.buttonDeleterelation.clicked.connect(lambda: self.model.button_clicked(0))  # 删除关系
        self.view.interface.buttonDelete.clicked.connect(lambda: self.model.button_clicked(1))  # 删除
        self.view.interface.buttonInitial.clicked.connect(lambda: self.model.button_clicked(2))  # 初始化
        self.view.interface.buttonInput.clicked.connect(lambda: self.model.button_clicked(3))  # 录入
        self.view.interface.buttonClean.clicked.connect(lambda: self.model.button_clicked(4))  # 清空
        self.view.interface.buttonSave.clicked.connect(lambda: self.model.button_clicked(5))  # 录入
        self.view.interface.buttonOut.clicked.connect(lambda: self.model.button_clicked(6))  # 退出

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = C_MainWindow()
    a.view.interface.show()
    sys.exit(app.exec_())
