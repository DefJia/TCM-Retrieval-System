from UI.UI import Ui_MainWindow
from UI.reminder import Ui_reminder
from UI.property import Ui_Property
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Front import Frontend



class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 修改界面
        super(Interface, self).__init__()
        self.setupUi(self)


class Reminder(QMainWindow, Ui_reminder):
    def __init__(self):
        # 修改界面
        super(Reminder, self).__init__()
        self.setupUi(self)


class Property(QMainWindow, Ui_Property):
    def __init__(self):
        # 修改界面
        super(Property, self).__init__()
        self.setupUi(self)


class Control:
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        self.interface.show()
        self.reminder = Reminder()
        self.property = Property()
        # 界面生成
        self.front = Frontend(self.interface, self.reminder, self.property)
        # 定义交互Class
        self.group_inputs = list()
        self.group_inputs.append(self.interface.lineSymptom)
        self.group_inputs.append(self.interface.lineDisease)
        self.group_inputs.append(self.interface.linePrescription)
        self.group_inputs.append(self.interface.lineMedicine)
        self.group_additions = list()
        self.group_additions.append(self.interface.buttonSymptom)
        self.group_additions.append(self.interface.buttonDisease)
        self.group_additions.append(self.interface.buttonPrescription)
        self.group_additions.append(self.interface.buttonMedicine)
        self.group_options = list()
        self.group_options.append(self.interface.symptomOption)
        self.group_options.append(self.interface.diseaseOption)
        self.group_options.append(self.interface.prescriptionOption)
        self.group_options.append(self.interface.medicineOption)
        self.group_tables = list()
        self.group_tables.append(self.interface.tablewidgetSymptom)
        self.group_tables.append(self.interface.tablewidgetDisease)
        self.group_tables.append(self.interface.tablewidgetPrescription)
        self.group_tables.append(self.interface.tablewidgetMedicine)
        self.group_tables.append(self.interface.tablewidgetBook)
        self.group_tables.append(self.interface.tablewidgetPrescribe)
        # 定义组件组
        ''' 以下为信号操作 '''
        '''
        for option in self.group_options:  # 下拉框选择
            option.clicked.connect(lambda: self.option_clicked(option))
        for input_box in self.group_inputs:  # 输入框输入
            input_box.textChanged.connect(lambda: self.line_text_changed(input_box))
        '''
        #self.interface.tablewidgetSymptom.clicked.connect(lambda: self.table_option_clicked(0))
        self.interface.tablewidgetDisease.clicked.connect(lambda: self.table_option_clicked(1))
        self.interface.tablewidgetPrescription.clicked.connect(lambda: self.table_option_clicked(2))
        self.interface.tablewidgetMedicine.clicked.connect(lambda: self.table_option_clicked(3))
        self.interface.symptomOption.clicked.connect(lambda: self.option_clicked(self.interface.symptomOption))
        self.interface.diseaseOption.clicked.connect(lambda: self.option_clicked(self.interface.diseaseOption))
        self.interface.prescriptionOption.clicked.connect(lambda: self.option_clicked(self.interface.prescriptionOption))
        self.interface.medicineOption.clicked.connect(lambda: self.option_clicked(self.interface.medicineOption))
        self.interface.lineSymptom.textChanged.connect(lambda: self.line_text_changed(self.interface.lineSymptom))
        self.interface.lineDisease.textChanged.connect(lambda: self.line_text_changed(self.interface.lineDisease))
        self.interface.linePrescription.textChanged.connect(lambda: self.line_text_changed(self.interface.linePrescription))
        self.interface.lineMedicine.textChanged.connect(lambda: self.line_text_changed(self.interface.lineMedicine))


        # 按钮点击
        self.interface.buttonSymptom.clicked.connect(lambda: self.button_clicked())
        self.reminder.buttonYes.clicked.connect(lambda: self.buttonyes_reminder())
        self.reminder.buttonNo.clicked.connect(lambda: self.buttonno_reminder())
        '''
        self.interface.buttonDisease.clicked.connect(lambda: self.button_clicked(self.interface.diseaseOption))
        self.interface.buttonPrescription.clicked.connect(lambda: self.button_clicked(self.interface.prescriptionOption))
        self.interface.buttonMedicine.clicked.connect(lambda: self.button_clicked(self.interface.medicineOption))
        '''
        self.interface.radioButton_2.toggled.connect(lambda: self.change_type())  # 切换模式

        self.interface.buttonInput.clicked.connect(lambda: self.buttonInput_clicked())

        #self.reminder.show()


        ''' 以下为界面初始化处理 '''
        for i in range(8):
            # 设定药方区结构
            if i % 2 == 0:
                self.interface.tablewidgetPrescribe.setColumnWidth(i, 150)
            else:
                self.interface.tablewidgetPrescribe.setColumnWidth(i, 69)
        tmp = [90, 50, 50]
        for i in range(3):
            self.interface.tablewidgetMedicine.setColumnWidth(i, tmp[i])
        for addition in self.group_additions: addition.hide()  # 隐藏加号
        for table in self.group_tables: table.setShowGrid(False)  # 隐藏内边框
        for option in self.group_options: option.hide()  # 隐藏下拉框
        # data = [('小sss汤', '3', '克'), ('哈哈', '2', '克' )]
        # self.front.set_table(self.interface.tablewidgetMedicine, data)
        # 测试代码
        sys.exit(app.exec_())

    def change_type(self):
        #  切换模式
        for widget in self.group_tables[0:3]:
            widget.clear()

        for line in self.group_inputs:
            line.clear()


        if self.interface.radioButton_2.isChecked():
            print("当前处于开方模式")
            self.front.type = 1
            self.interface.labelType.setText('开方模式')
            for addition in self.group_additions:
                addition.hide()
        else:
            self.front.type = 0
            self.interface.labelType.setText('录入模式')
            print("当前处于录入模式")
            for addition in self.group_additions:
                addition.show()
        pass

    def line_text_changed(self, input_box):
        # 原有代码已精简
        index = self.group_inputs.index(input_box)
        self.front.get_input(index, input_box, self.group_options[index])
        pass

    def option_clicked(self, option):
        index = self.group_options.index(option)
        text = str(option.selectedItems()[0].text())
        # self.group_inputs[index].setText(text)
        self.group_inputs[index].setText("")
        option.hide()
        self.front.optioned_data(index, text)
        pass

    def table_option_clicked(self, table_id):
        table = self.group_tables[table_id]
        try:
            if table_id != 3:
                text = str(table.selectedItems()[0].text())
                self.front.optioned_data(table_id, text, 1)
        except IndexError:
            pass

    def button_clicked(self):
        # 之后根据front再做变化
        # self.interface.buttonSymptom.clicked.connect(lambda: self.front.save_data(0))
        # 此处代码已合并至Front的save_data
        self.reminder.show()


    def buttonyes_reminder(self):
        self.front.save_data(self.interface.lineSymptom,'（需要变化）', 0,'（需要变化）')

    def buttonno_reminder(self):
        self.reminder.hide()

        '''
        self.interface.buttonSymptom.clicked.connect(lambda: self.front.save_data(0, self.interface.lineSymptom,self.reminder))
        self.interface.buttonDisease.clicked.connect(lambda: self.front.save_data(1, self.interface.lineDisease,self.reminder))
        self.interface.buttonPrescription.clicked.connect(lambda: self.front.save_data(2, self.interface.linePrescription,self.reminder))
        self.interface.buttonMedicine.clicked.connect(lambda: self.front.save_data(3, self.interface.lineMedicine,self.reminder))
        '''
        pass

    def buttonInput_clicked(self):
        medicines = self.front.search_area[3]
        if int(len(medicines))%4 == 0:
            row = int(len(medicines) / 4)
        else: row = int(len(medicines) / 4) + 1
        text_all = [list() for i in range(row)]
        n = 0
        for i in medicines:
            text_all[int(n/4)] += i
            n+=1
        self.front.set_table(self.group_tables[5], text_all)


        '''
        rows = self.interface.tablewidgetMedicine.rowCount()

        for rows_index in range(rows):
            # print items[item_index].text()
            print(self.interface.tablewidgetMedicine.item(rows_index, 0).text())

        print(rows)
        '''
        #没写完
        pass


if __name__ == "__main__":
    test = Control()