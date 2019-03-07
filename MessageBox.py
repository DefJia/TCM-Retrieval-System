# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:04:54 2018

@author: yang
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

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
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.buttonReply = QMessageBox.question(self, self.content, self.question, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #Cancel Open Discard Reset No RestoreDefaults Ignore
        #Ok Save Close Yes NoToAll Abort
        #Help SaveAll Apply YesToAll NoButton Retry
        '''
        if self.buttonReply == QtWidgets.QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')
        '''
        #buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to save?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        #print(int(buttonReply))
        #if buttonReply == QMessageBox.Yes:
        #    print('Yes clicked.')
        #if buttonReply == QMessageBox.No:
        #    print('No clicked.')
        #if buttonReply == QMessageBox.Cancel:
        #    print('Cancel')
     
    def getReply(self):
        if self.buttonReply == QtWidgets.QMessageBox.Yes:
            return "yes"
        else:
            return "no"
        
    #def setTitle(self,title):
     #   self.title = title
    
    #def setContent(self,content):
     #   self.content = content
    
    #def setQuestion(self,question):
     #   self.question = question
    
    def showWindow(self):
        self.show()

if __name__ == "__main__":
    test = MessageBox("你好吗","还行")