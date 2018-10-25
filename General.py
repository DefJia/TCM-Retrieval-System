from UI.main import Ui_Main
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys


class M(QMainWindow, Ui_Main):
    def __init__(self):
        super(M, self).__init__()
        self.setupUi(self)

    def open(self):
        self.show()

    def close(self):
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = M()
    test.show()
