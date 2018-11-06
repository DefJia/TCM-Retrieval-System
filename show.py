from UI.UI import MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Front import Frontend


class Interface(QMainWindow, MainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi(self)

    def open(self):
        self.show()

    def close(self):
        self.hide()


class Control():
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        self.interface.show()
        self.interface.buttonSymptom.clicked.connect(lambda: self.test())

        # Generate interface
        self.front = Frontend()
        sys.exit(app.exec_())

    def test(self):
        print(1)
        data = self.front.get_data()
        self.setTable(self.interface.tablewidgetSymptom, data)

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
