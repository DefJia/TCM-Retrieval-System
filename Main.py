from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys

from App.C_MainWindow import C_MainWindow


class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        self.MainWindow = C_MainWindow()
        self.MainWindow.view.interface.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    test = Main()
