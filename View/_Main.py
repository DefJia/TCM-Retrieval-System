from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from Interface import MainWindow
from Controller.Monitor import Monitor

class View:
    def __init__(self):
        app = QApplication(sys.argv)
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        Monitor(self.MainWindow)
        sys.exit(app.exec_())


if __name__ == '__main__':
    test = View()
