import sys, os
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir)


from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from View.Interface import MainWindow
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
