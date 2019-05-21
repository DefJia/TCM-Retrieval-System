import sys, os
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir)

# from Controller.Method import test
# from Model.test import L
from Model.Interface import *


class Monitor:
    def __init__(self, obj):
        self.interface = obj
        # init
        self.additions()
        self.inputs()
        self.tables()
        self.options()
        self.radioboxs()
        self.buttons()

    def additions(self):
        self.interface.buttonSymptom.clicked.connect(lambda: addition_clicked(0))
        self.interface.buttonDisease.clicked.connect(lambda: addition_clicked(1))
        self.interface.buttonPrescription.clicked.connect(lambda: addition_clicked(2))
        self.interface.buttonMedicine.clicked.connect(lambda: addition_clicked(3))

    def inputs(self):
        self.interface.lineSymptom.textChanged.connect(lambda: input_changed(0, self.interface.lineSymptom.text()))
        self.interface.lineDisease.textChanged.connect(lambda: input_changed(1, self.interface.lineDisease.text()))
        self.interface.linePrescription.textChanged.connect(lambda: input_changed(2, self.interface.Prescription.text()))
        self.interface.lineMedicine.textChanged.connect(lambda: input_changed(3, self.interface.lineMedicine.text()))
        
    def tables(self):
        self.interface.tablewidgetSymptom.clicked.connect(lambda: table_clicked(0))
        self.interface.tablewidgetDisease.clicked.connect(lambda: table_clicked(1))
        self.interface.tablewidgetPrescription.clicked.connect(lambda: table_clicked(2))
        self.interface.tablewidgetMedicine.clicked.connect(lambda: table_clicked(3))

    def options(self):
        self.interface.symptomOption.clicked.connect(lambda: option_clicked(0))
        self.interface.diseaseOption.clicked.connect(lambda: option_clicked(1))
        self.interface.prescriptionOption.clicked.connect(lambda: option_clicked(2))
        self.interface.medicineOption.clicked.connect(lambda: option_clicked(3))

    def radioboxs(self):
        self.interface.radioButton_2.toggled.connect(lambda: radiobox_changed())

    def buttons(self):
        self.interface.buttonDeleterelation.clicked.connect()  # 删除关系
        self.interface.buttonDelete.clicked.connect()  # 删除
        self.interface.buttonInput.clicked.connect()  # 录入
        self.interface.buttonClean.clicked.connect()
        self.interface.buttonInitial

'''
# --- information按钮组 --- #
        self.information.IButtonYes.clicked.connect(lambda: self.i_buttonInput_clicked())
        #self.information.IButtonYes.clicked.connect(lambda: self.interface.show())
        self.information.IButtonInquire.clicked.connect(lambda: self.inquire.show())
        self.information.IButtonOut.clicked.connect(lambda: self.information.hide())
        # --- information 触发--- #
        self.information.lineSymptom.textChanged.connect(lambda: self.i_line_text_changed())
        self.information.option.hide()

        self.information.option.clicked.connect(lambda: self.i_option_clicked(self.information.option))

        # --- inquire按钮组 --- #
        #self.inquire.ButtonYes.clicked.connect(lambda: self.inquire.hide())
        # --- inquire 触发 --- #



        # --- interface按钮组 --- #
        self.interface.buttonInput.clicked.connect(lambda: self.yes.show())  # 录入
        self.yes.yesButton.clicked.connect(lambda: self.buttonInput_clicked())
        self.interface.buttonInitial.clicked.connect(lambda: self.initial_button_clicked())  # 初始化
        self.interface.buttonClean.clicked.connect(lambda: self.buttonClean_clicked())

        self.interface.buttonDelete.clicked.connect(lambda: self.buttonDelete_clicked())  # 删除
        self.interface.buttonDeleterelation.clicked.connect(lambda: self.buttonRelationDelete_clicked())# 删除关系
        self.interface.buttonOut.clicked.connect(lambda: self.interface.hide())  # 退出
        self.interface.buttonSave.clicked.connect(lambda: self.final.show())  # 最终保存


        # --- Inquire按钮组 --- #
        self.inquire.ButtonYes.clicked.connect(lambda: self.iq_buttonYes_clicked())  # 查询
        self.inquire.ButtonOut.clicked.connect(lambda: self.inquire.hide())
        # --- Final按钮组 --- #
        #self.interface.buttonSave.clicked.connect(lambda: self.buttonSave_clicked())
        self.final.buttonContinue.clicked.connect(lambda: self.buttonContinue_click())
        self.final.buttonOut.clicked.connect(lambda: self.buttonOut_click())

        # --- quantity按钮组件 ---#
        self.quantity.pushButton.clicked.connect(lambda: self.quantity_button_clicked())

        # --- result按钮组件 ---#
        self.inquire.tableWidget.doubleClicked.connect(lambda: self.inquire_widget_double_clicked(self.inquire.tableWidget))
        self.result.ButtonOut.clicked.connect(lambda: self.buttonOut_clicked())
        self.result.tableWidget.doubleClicked.connect(lambda: self.result_widget_double_clicked(self.result.tableWidget))
'''