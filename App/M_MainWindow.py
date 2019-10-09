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
        self.modes = ['录入模式', '开方模式']
        self.log = list()

    def radiobox_changed(self):
        #  切换模式
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
            # 显示加号按钮和删除关系
        self.data['type'] = type    
        self.view.interface.labelType.setText(self.modes[type])
        self.button_clicked(2)  # 初始化
        
    def input_changed(self, id, text):
        option = self.view.group_options[id]
        if text:
            data = self.database.query_similar_data(id, text)
            if data:
                # 搜索然后出结果, 若没有结果则不出
                option.show()
                self.set_table(option, data)
                self.record('搜索关键词：' + text)
            else:
                option.hide()
        else:
                option.hide()

    def option_clicked(self, id):
        # 下拉框
        if self.data['type'] == 1:
            for i in range(4): 
                self.data['tables'][i] = list()
                self.clear(self.view.group_tables[:4])
            # 清空
        option = self.view.group_options[id]
        table = self.view.group_tables[id]
        text = str(option.selectedItems()[0].text())
        data = self.database.find_relative_info(id, text)
        flag = 0
        for index in data:
            if self.data['type'] == 1 or flag != 0:
                table2 = self.view.group_tables[index]
                self.set_table(table2, data[index])
            flag = 1
        self.set_table(table, [[text]])
        option.hide()  # 隐藏下拉框
        self.view.group_inputs[id].setText('')  # 清空输入框
        self.record('点击关键词：' + text)

    def table_clicked(self, id, text=''):
        if self.data['type'] == 1:
            for i in range(4): self.data['tables'][i] = list()
            table = self.view.group_tables[id]
            if text == '':
                text = str(table.selectedItems()[0].text())
            data = self.database.find_relative_info(id, text)
            for index in data:
                table2 = self.view.group_tables[index]
                self.set_table(table2, data[index])
            self.set_table(table, [[text]])
            self.record('点击关键词：' + text)

    def addition_clicked(self, id):
        # 仅限录入模式，点击加号，回车
        # 若没有则直接加入，有不加入，但都将这个放入table
        text = self.view.group_inputs[id].text()
        data = self.database.query_similar_data(id, text)
        if data:
            for i in range(4): self.data['tables'][i] = list()
            self.set_table(self.view.group_tables[id], data)
        else:
            message = format('是否确认添加%s？' % text)
            response = self.view.show_reminder(message)
            if response == 0:
                # 确认添加
                result = self.database.save_single_item(id, text)
                if result == 0:
                    # 添加成功
                    '''
                    for i in range(4):
                        data = self.database.query_similar_data(i, '')
                        self.set_table(self.view.group_tables[i], data)
                        '''
                    table = self.view.group_tables[id]
                    self.data['tables'][id].append([text])
                    self.set_table(table, self.data['tables'][id])
                    self.clear(self.view.group_inputs[id])
                    self.record('添加%s成功' % text)
                else:
                    message = '添加失败，请检查数据库或重新尝试！'
                    self.view.show_reminder(message)

    def button_clicked(self, id):
        # 按钮合集
        if id == 0:
            # 删除关系
            if self.data['type'] == 0:
                for i in range(3):
                    if self.data['tables'][i] and self.data['tables'][i+1]:
                        for ii in self.data['tables'][i]:
                            for iii in self.data['tables'][i+1]:
                                res = self.database.drop_relation(i, ii[0], iii[0])
                                if res == 1:
                                    self.view.show_reminder('存在关联的数据，不可删除！')
                                else:
                                    self.view.show_reminder('删除关系成功！')
        elif id == 1:
            # 删除
            if self.data['type'] == 0:
                for i in range(4):
                    if self.view.group_tables[i].selectedItems():
                        text = self.view.group_tables[i].selectedItems()[0].text()
                        res = self.database.delete_single_item(i, text)
                        # 删除数据
                        if res == 1:
                            self.view.show_reminder('存在关联的数据，不可删除！')
                        else:
                            self.view.show_reminder('删除%s成功！' % text)
                            self.record(('删除%s成功！' % text))
                        # self.data['tables'][i].remove([text])
                        # self.set_all_tables()
                        break
        elif id == 2:
            # 初始化
            # 开方模式初始化，清空一切数据
            # 录入模式，显示所有
            self.clear(self.view.group_inputs)
            self.clear(self.view.group_tables)
            self.data['tables'] = [list() for i in range(6)]
            '''
            if self.data['type'] == 0:
                for i in range(4):
                    data = self.database.query_similar_data(i, '')
                    self.set_table(self.view.group_tables[i], data)
            '''
            self.record('执行初始化操作')
        elif id == 3:
            if self.data['type'] == 1:
                # 保存
                for elem in self.data['tables'][3]:
                    flag = 0
                    for i in self.data['tables'][4]:
                        if i[0] == elem[0]:
                            i[1] = str(int(i[1]) + int(elem[1]))
                            flag = 1
                            break
                    if flag == 0: self.data['tables'][4].append(elem[:-1])
                # 合并两个列表
                tmp = list()
                for i in self.data['tables'][4]:
                    tmp.append(i[0])
                    tmp.append(i[1] + '克')
                if int(len(tmp)) % 6 == 0:
                    row = int(len(tmp) / 6)
                else:
                    row = int(len(tmp) / 6) + 1
                list_4 = [list() for i in range(row)]
                n = 0
                for i in tmp:
                    list_4[int(n / 6)].append(i)
                    n += 1
                self.set_table(self.view.group_tables[4], list_4)
                self.record('写入开方区：'+str(self.data['tables'][3])+str(self.data['tables'][4]))
            else:
                # 录入模式 添加关系
                for i in range(3):
                    if self.data['tables'][i] and self.data['tables'][i+1]:
                        for ii in self.data['tables'][i]:
                            for iii in self.data['tables'][i+1]:
                                self.database.save_relation(i, ii[0], iii[0])
                                self.record('%s-%s的关系写入成功！' % (ii[0], iii[0]))
                                self.view.show_reminder('%s-%s的关系写入成功！' % (ii[0], iii[0]))
        elif id == 4:
            # 清空开方
            self.data['tables'][4] = list()
            self.clear(self.view.group_tables[4])
            self.record('清空开方')
        elif id == 5:
            # res = MessageBox('a','b').status
            pass
        elif id == 6:
            sys.exit()

    def set_table(self, table, data_list):
        # data_list: [[item, item], [item, item]]
        if table in self.view.group_tables:
            id = self.view.group_tables.index(table)
            self.data['tables'][id] = data_list
            if id == 4:
                header = [['药名', '克数', '药名', '克数', '药名', '克数']]
                data_list = header + data_list 
        # table.clear()
        if data_list:
            row = len(data_list)
            column = len(data_list[0])
            table.setRowCount(row)
            table.setColumnCount(column)
            for r in range(row):
                columnCurrentRow = len(data_list[r])
                for c in range(columnCurrentRow):
                    t = (str(data_list[r][c]))
                    table.setItem(r, c, QtWidgets.QTableWidgetItem(t))
    
    def set_all_tables(self, data=None):
        data = self.data['tables']
        for i in range(len(data)):
            self.set_table(self.view.group_tables[i], data[i])

    def clear(self, obj):
        if type(obj) == list:
            for elem in obj:
                elem.clear()
        else:
            obj.clear()  

    def record(self, text=''):
        content = format('%s, %s' % (self.modes[self.data['type']], text))
        print(content)
        self.log.append([content])
        self.set_table(self.view.interface.tablewidgetBook, self.log)
