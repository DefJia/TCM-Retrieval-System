import sys, os
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir)

from Controller.Method import test
from Model.test import L


class Monitor:
    def __init__(self, obj):
        obj.buttonInput.clicked.connect(lambda:test())
        # 输入框
        self.group_inputs = list()
        self.group_inputs.append(obj.lineSymptom)
        self.group_inputs.append(obj.lineDisease)
        self.group_inputs.append(obj.linePrescription)
        self.group_inputs.append(obj.lineMedicine)
        # 添加按钮
        self.group_additions = list()
        self.group_additions.append(obj.buttonSymptom)
        self.group_additions.append(obj.buttonDisease)
        self.group_additions.append(obj.buttonPrescription)
        self.group_additions.append(obj.buttonMedicine)
        # 下拉框
        self.group_options = list()
        self.group_options.append(obj.symptomOption)
        self.group_options.append(obj.diseaseOption)
        self.group_options.append(obj.prescriptionOption)
        self.group_options.append(obj.medicineOption)
        # 显示框
        self.group_tables = list()
        self.group_tables.append(obj.tablewidgetSymptom)
        self.group_tables.append(obj.tablewidgetDisease)
        self.group_tables.append(obj.tablewidgetPrescription)
        self.group_tables.append(obj.tablewidgetMedicine)
        self.group_tables.append(obj.tablewidgetBook)
        self.group_tables.append(obj.tablewidgetPrescribe)
        # init
        self.tables()

    def tables(self):
        n = 0
        for table in self.group_additions:
            table.clicked.connect(L(n))
            n += 1
