from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MessageBox(QtWidgets.QWidget):
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
        self.buttonReply = QMessageBox.question(self, self.content, self.question, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if self.buttonReply == QtWidgets.QMessageBox.Yes:
            print('Yes clicked.')
            return 1
        else:
            print('No clicked.')
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MessageBox("你好吗","还行")
    main_window.show()
    sys.exit(app.exec_())
