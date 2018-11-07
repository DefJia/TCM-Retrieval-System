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

class Control:
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        self.interface.show()
        # Generate interface
        self.front = Frontend()
        # Functions class
        self.line_text_changed()
        self.button_clicked()
        self.option_clicked()
        # Add trigger
        sys.exit(app.exec_())

    def line_text_changed(self):
        # self.interface.lineSymptom.textChanged.connect(lambda: self.front.)
        pass

    def button_clicked(self):
        self.interface.buttonSymptom.clicked.connect(lambda: self.test())

    def option_clicked(self):
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


if __name__ == "__main__":
    test = Control()
