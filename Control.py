from UI.UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Front import Frontend


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 修改界面
        super(Interface, self).__init__()
        self.setupUi(self)
        # 隐藏下拉框
        self.symptomOption.hide()
        self.diseaseOption.hide()
        self.prescriptionOption.hide()
        self.medicineOption.hide()

   
class Control:
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        self.interface.show()
        # Generate interface
        self.front = Frontend(self.interface)
        # Functions class
        # 模式按钮切换 以及四个功能按钮
        # 开方工作区操作
        self.line_text_changed()  # 输入框
        # self.button_clicked()  # 按钮
        self.option_clicked()  # 显示框选择
        # 下拉框选择
        # Add trigger
        sys.exit(app.exec_())

    def line_text_changed(self):
        # 可能今后会有bug，有点小冲突问题
        self.interface.lineSymptom.textChanged.connect(lambda: self.front.get_input(0))
        self.interface.lineDisease.textChanged.connect(lambda: self.front.get_input(1))
        self.interface.linePrescription.textChanged.connect(lambda: self.front.get_input(2))
        self.interface.lineMedicine.textChanged.connect(lambda: self.front.get_input(3))
        # self.interface.lineBook.textChanged.connect(lambda: self.front.get_input(4))
        # self.interface.lineSymptom.textChanged.connect(lambda: self.front.set_table(self.interface.symptomOption,self.front.data))  # 取数据还未完成
        # self.interface.lineDisease.textChanged.connect(lambda:self.front.set_table(self.interface.diseaseOption,self.front.data))
        # self.interface.linePrescription.textChanged.connect(lambda: self.front.set_table(self.interface.prescriptionOption,self.front.data))
        # self.interface.lineMedicine.textChanged.connect(lambda: self.front.set_table(self.interface.medicineOption,self.front.data))
        # self.interface.lineBook.textChanged.connect(lambda: self.front.set_table(self.interface.bookOption,self.front.data))
        self.interface.lineSymptom.textChanged.connect(lambda: self.interface.symptomOption.show())
        self.interface.lineDisease.textChanged.connect(lambda:self.interface.diseaseOption.show())
        self.interface.linePrescription.textChanged.connect(lambda:  self.interface.prescriptionOption.show())
        self.interface.lineMedicine.textChanged.connect(lambda: self.interface.medicineOption.show())
        pass

    def button_clicked(self):
        # 之后根据front再做变化
        # if self.interface.lineSymptom.text() != "" :
        self.interface.buttonSymptom.clicked.connect(lambda: self.front.save_data("symptom",self.interface.lineSymptom.text()))
        self.interface.buttonSymptom.clicked.connect(lambda: self.front.data.append(self.interface.lineSymptom.text()))#可合并再上个方法
        self.interface.buttonSymptom.clicked.connect(lambda: self.front.set_table(self.interface.symptomOption,self.front.data))#有错应该再back取数据
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

    def option_clicked(self):
        self.interface.symptomOption.clicked.connect(lambda:self.interface.lineSymptom.setText(self.interface.symptomOption.selectedItems.text()))
        self.interface.diseaseOption.clicked.connect(lambda:self.interface.lineDiseasesetText(self.interface.diseaseOption.selectedItems.text()))
        self.interface.prescriptionOption.clicked.connect(lambda:self.interface.linePrescription.setText(self.interface.prescriptionOption.selectedItems.text()))
        self.interface.medicineOption.clicked.connect(lambda:self.interface.lineMedicine.setText(self.interface.medicineOption.selectedItems.text()))
        
        self.interface.symptomOption.clicked.connect(lambda: self.interface.symptomOption.hide())
        self.interface.diseaseOption.clicked.connect(lambda: self.interface.diseaseOption.hide())
        self.interface.prescriptionOption.clicked.connect(lambda: self.interface.prescriptionOption.hide())
        self.interface.medicineOption.clicked.connect(lambda: self.interface.medicineOption.hide())
        pass


if __name__ == "__main__":
    test = Control()
