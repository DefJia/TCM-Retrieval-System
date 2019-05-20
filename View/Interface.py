from PyQt5.QtWidgets import QMainWindow
from View.UI.UI import Ui_MainWindow
from View.UI.information import Ui_Information
from View.UI.inquire import Ui_Inquire


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


class InformationWindow(QMainWindow, Ui_Information):
    def __init__(self):
        super(InformationWindow, self).__init__()
        self.setupUi(self)


class InquireWindow(QMainWindow, Ui_Inquire):
    def __init__(self):
        super(InquireWindow, self).__init__()
        self.setupUi(self)
