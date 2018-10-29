from UI.main import Main
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys


class Interface(QMainWindow, Main):
    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi(self)

    def open(self):
        self.show()

    def close(self):
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Interface()
    test.show()
    sys.exit(app.exec_())
