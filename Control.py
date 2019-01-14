from UI.UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Front import Frontend


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 修改界面
        super(Interface, self).__init__()
        self.setupUi(self)

   
class Control:
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        self.interface.show()
        # 界面生成
        self.front = Frontend(self.interface)
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
        self.interface.symptomOption.clicked.connect(lambda: self.option_clicked(self.interface.symptomOption))
        self.interface.diseaseOption.clicked.connect(lambda: self.option_clicked(self.interface.diseaseOption))
        self.interface.prescriptionOption.clicked.connect(lambda: self.option_clicked(self.interface.prescriptionOption))
        self.interface.medicineOption.clicked.connect(lambda: self.option_clicked(self.interface.medicineOption))
        self.interface.lineSymptom.textChanged.connect(lambda: self.line_text_changed(self.interface.lineSymptom))
        self.interface.lineDisease.textChanged.connect(lambda: self.line_text_changed(self.interface.lineDisease))
        self.interface.linePrescription.textChanged.connect(lambda: self.line_text_changed(self.interface.linePrescription))
        self.interface.lineMedicine.textChanged.connect(lambda: self.line_text_changed(self.interface.lineMedicine))
        self.button_clicked()  # 按钮点击
        self.interface.radioButton_2.toggled.connect(lambda: self.change_type())  # 切换模式
        ''' 以下为界面初始化处理 '''
        for addition in self.group_additions: addition.hide()  # 隐藏加号
        for table in self.group_tables: table.setShowGrid(False)  # 隐藏内边框
        for option in self.group_options: option.hide()  # 隐藏下拉框
        sys.exit(app.exec_())

    def change_type(self):
        #  切换模式
        if self.interface.radioButton_2.isChecked():
            self.front.type = 1
            for addition in self.group_additions:
                print("开方")
                addition.hide()
        else:
            self.front.type = 0
            for addition in self.group_additions:
                addition.show()
                print("录入")
        #self.front.init_data()
        pass

    def line_text_changed(self, input_box):
        # 原有代码已精简
        index = self.group_inputs.index(input_box)
        self.front.get_input(index, input_box, self.group_options[index])
        pass

    def option_clicked(self, option):
        index = self.group_options.index(option)
        text = str(option.selectedItems()[0].text())
        #self.group_inputs[index].setText(text)
        self.group_inputs[index].setText("")
        option.hide()
        #option.clicked.connect(lambda: self.front.optioned_data(index, text))
        self.front.optioned_data(index, text)
        #option.clicked.connect(lambda: self.front.add_item(index, text))
        
        pass

    def button_clicked(self):
        # 之后根据front再做变化
        self.interface.buttonSymptom.clicked.connect(lambda: self.front.save_data(0))
        # 此处代码已合并至Front的save_data
         #if self.interface.lineDisease.text() != "" :
        self.interface.buttonDisease.clicked.connect(lambda: self.front.save_data("disease",self.interface.lineDisease.text()))
        self.interface.buttonDisease.clicked.connect(lambda: self.front.data.append(self.interface.lineDisease.text()))
        self.interface.buttonDisease.clicked.connect(lambda: self.front.set_table(self.interface.diseaseOption,self.front.data))

         #if self.interface.linePrescription.text() != "" :
        self.interface.buttonPrescription.clicked.connect(lambda: self.front.save_data("symptom",self.interface.linePrescription.text()))
        self.interface.buttonPrescription.clicked.connect(lambda: self.front.data.append(self.interface.linePrescription.text()))
        self.interface.buttonPrescription.clicked.connect(lambda: self.front.set_table(self.interface.prescriptionOption,self.front.data))
        
        # if self.interface.lineSymptom.text() != "" :
        self.interface.buttonMedicine.clicked.connect(lambda: self.front.save_data("symptom",self.interface.lineMedicine.text()))
        self.interface.buttonMedicine.clicked.connect(lambda: self.front.data.append(self.interface.lineMedicine.text()))
        self.interface.buttonMedicine.clicked.connect(lambda: self.front.set_table(self.interface.medicineOption,self.front.data))
        pass


if __name__ == "__main__":
    test = Control()
