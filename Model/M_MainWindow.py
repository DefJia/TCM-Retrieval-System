import sys
from View.V_MainWindow import V_MainWindow
from View.Interface import *


class M_MainWindow:
    def __init__(self, obj):
        self.view = V_MainWindow(obj)

    def addition_clicked(self, id):
        print(id)
        
    def input_changed(self, id, text):
        print(id, text)

    def table_clicked(self, id):
        print(id)

    def option_clicked(self, id):
        print(id)

    def radiobox_changed(self):
        print('-')

    def button_clicked(self, id):
        if id == 6:
            sys.exit()
        elif id == 5:
            res = MessageBox('a','b').status
