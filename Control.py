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
        self.button_clicked()  # 按钮
        self.option_clicked()  # 显示框选择
        # 下拉框选择
        # Add trigger
        sys.exit(app.exec_())

    def line_text_changed(self):
        self.interface.lineSymptom.textChanged.connect(lambda: self.front.get_input(0))
        pass

    def button_clicked(self):
        # self.interface.buttonSymptom.clicked.connect(lambda: self.front.())
        pass

    def option_clicked(self):
#<<<<<<< HEAD
        self.interface.symptomOption.clicked.connect(lambda: self.hhh())

    def hhh(self):
        data = self.interface.symptomOption.selectedItems()[0]

    def test(self):
        print(1)
        self.interface.symptomOption.show()
        data = self.front.get_data()
        self.setTable(self.interface.symptomOption, data)




    @staticmethod
    def setTable(table, dataList):
        row = len(dataList)
        column = len(dataList[0])
        table.setRowCount(row)
        table.setColumnCount(column)
        for r in range(row):
            for c in range(column):
                table.setItem(r, c, QTableWidgetItem(dataList[r][c]))
#=======
        # self.interface.symptomOption.clicked.connect(lambda: self.front.)
        pass
#>>>>>>> 1390aab1d4c3fc1a07f0b16843a8f77df16b7a11


if __name__ == "__main__":
    test = Control()