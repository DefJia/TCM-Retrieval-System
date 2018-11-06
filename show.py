from UI.UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Front import Frontend


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 修改界面
        super(Interface, self).__init__()
        self.setupUi(self)
        self.symptomOption.hide()  # 隐藏下拉框

    # def open(self):
        # self.show()

    # def close(self):
        # self.hide()


class Control():
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        self.interface.show()
        self.interface.buttonSymptom.clicked.connect(lambda: self.test())
        self.interface.lineSymptom.textChanged.connect(lambda: self.test())
        # Generate interface
        self.front = Frontend()
        sys.exit(app.exec_())

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
