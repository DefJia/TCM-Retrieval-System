from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox

from View.UI.UI import Ui_MainWindow
from View.UI.information import Ui_Information
from View.UI.inquire import Ui_Inquire


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()


class InformationWindow(QMainWindow, Ui_Information):
    def __init__(self):
        super(InformationWindow, self).__init__()
        self.setupUi(self)


class InquireWindow(QMainWindow, Ui_Inquire):
    def __init__(self):
        super(InquireWindow, self).__init__()
        self.setupUi(self)

class MessageBox(QWidget):
    def __init__(self,content,question):
        super().__init__()
        self.title = "message"
        self.left = 570
        self.top = 290
        self.width = 320
        self.height = 200
        self.content = content
        self.question = question
        self.status = self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.buttonReply = QMessageBox.question(self, self.content, self.question, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if self.buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            return 1
        else:
            print('No clicked.')
            return 0
