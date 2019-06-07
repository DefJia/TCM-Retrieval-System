import sys
# --- 分割线 --- 
from View.V_MainWindow import V_MainWindow
from View.Interface import *
from View.General import *


class M_MainWindow:
    def __init__(self, obj):
        self.view = V_MainWindow(obj)
        # 当前参数
        self.type = 1  # 当前模式
        self.search_area = [list() for i in range(4)]  # 检索框内容

    def addition_clicked(self, id):
        # 点击加号
        print(id)
        
    def input_changed(self, id, text):
        if text:
            # 搜索然后出结果
            # 若没有结果则不出
        else:
            pass

    def table_clicked(self, id):
        print(id)

    def option_clicked(self, id):
        print(id)

    def radiobox_changed(self):
        # 点击单选框
        # 先初始化 清空所有信息
        text = '当前处于开方模式'
        output_log(text)
        print('-')

    def button_clicked(self, id):
        if id == 6:
            sys.exit()
        elif id == 5:
            res = MessageBox('a','b').status
        elif if == 2:
            # 初始化

