import sys
from PyQt5 import QtWidgets

from App.General import *
from App.Database import Database


class M_MainWindow:
    def __init__(self, window):
        self.view = window
        self.database = Database()
        # 当前参数
        self.data = dict()
        self.data['type'] = 1  # 当前模式
        self.data['tables'] = [list() for i in range(6)]  # 表格内容

    @staticmethod
    def clear(obj):
        if type(obj) == list:
            for elem in obj:
                elem.clear()
        else:
            obj.clear()

    def radiobox_changed(self):
        #  切换模式
        self.clear(self.view.group_inputs)
        self.clear(self.view.group_tables)
        self.data['table'] = [list() for i in range(6)]
        # 清空当前所有信息
        modes = ['录入模式', '开方模式']
        if self.view.interface.radioButton_2.isChecked():
            type = 1
            for addition in self.view.group_additions:
                addition.hide()
            self.view.interface.buttonDeleterelation.hide()
            # 隐藏加号按钮和删除关系
        else:
            type = 0
            for addition in self.view.group_additions:
                addition.show()
            self.view.interface.buttonDeleterelation.show()
        self.data['type'] = type
        record("当前处于%s" % modes[type])
        self.view.interface.labelType.setText(modes[type])

    def addition_clicked(self, id):
        # 点击加号
        print(id)
        
    def input_changed(self, id, text):
        if text:
            # 搜索然后出结果, 若没有结果则不出
            data = self.database.query_similar_data(id, text)
            option = self.view.group_options[id]
            option.show()
            self.set_table(option, data)

    def table_clicked(self, id):
        print(id)

    def option_clicked(self, id):
        option = self.view.group_options[id]
        table = self.view.group_tables[id]
        text = str(option.selectedItems()[0].text())
        data = self.database.find_relative_info(id, text)
        for index in data:
            table2 = self.view.group_tables[id]
            self.set_table(table2, data[index])
        self.set_table(table, [[text]])
        option.hide()  # 隐藏下拉框
        self.view.group_inputs[id].setText('')  # 清空输入框

    @staticmethod
    def set_table(table, data_list):
        # data_list: [[item, item], [item, item]]
        if data_list:
            print(data_list)
            row = len(data_list)
            column = len(data_list[0])
            print(row,column)
            table.setRowCount(row)
            table.setColumnCount(column)
            for r in range(row):
                columnCurrentRow = len(data_list[r])
                for c in range(columnCurrentRow):
                    t = (str(data_list[r][c]))
                    table.setItem(r, c, QtWidgets.QTableWidgetItem(t))
    
    def set_all_tables(self, data):
        cnt = 0
        for item in data:
            if type(item) == list and item:
                self.set_table(self.widgets[cnt], item)
            cnt += 1
        return 0

        
    '''
    def button_clicked(self, id):
        if id == 6:
            sys.exit()
        elif id == 5:
            res = MessageBox('a','b').status
    '''