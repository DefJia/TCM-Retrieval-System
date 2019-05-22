class V_MainWindow:
    def __init__(self, obj):
        self.interface = obj
        self.group_inputs = list()
        self.group_additions = list()
        self.group_options = list()
        self.group_tables = list()
        self.fill_lists()
        # --- 设定部分区域结构 ---
        # 设定药方区结构
        for i in range(8):
            width = 69 if i % 2 != 0 else 150
            self.interface.tablewidgetPrescribe.setColumnWidth(i, width)
        # 设定药名区结构
        tmp = [90, 50]
        for i in range(len(tmp)):
            self.interface.tablewidgetMedicine.setColumnWidth(i, tmp[i])
        # --- 隐藏部分组件 --- 
        for addition in self.group_additions: addition.hide()  # 隐藏加号
        for table in self.group_tables: table.setShowGrid(False)  # 隐藏内边框
        for option in self.group_options: option.hide()  # 隐藏下拉框

    def fill_lists(self):
        # 输入框
        self.group_inputs.append(self.interface.lineSymptom)
        self.group_inputs.append(self.interface.lineDisease)
        self.group_inputs.append(self.interface.linePrescription)
        self.group_inputs.append(self.interface.lineMedicine)
        # 添加按钮
        self.group_additions.append(self.interface.buttonSymptom)
        self.group_additions.append(self.interface.buttonDisease)
        self.group_additions.append(self.interface.buttonPrescription)
        self.group_additions.append(self.interface.buttonMedicine)
        # 下拉框
        self.group_options.append(self.interface.symptomOption)
        self.group_options.append(self.interface.diseaseOption)
        self.group_options.append(self.interface.prescriptionOption)
        self.group_options.append(self.interface.medicineOption)
        # 显示框
        self.group_tables.append(self.interface.tablewidgetSymptom)
        self.group_tables.append(self.interface.tablewidgetDisease)
        self.group_tables.append(self.interface.tablewidgetPrescription)
        self.group_tables.append(self.interface.tablewidgetMedicine)
        self.group_tables.append(self.interface.tablewidgetBook)
        self.group_tables.append(self.interface.tablewidgetPrescribe)

