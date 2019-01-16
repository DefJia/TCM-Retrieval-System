from configparser import ConfigParser
from Back import Backend
from PyQt5.QtWidgets import QTableWidgetItem


class Frontend:
    def __init__(self, interface):
        config = ConfigParser()
        config.read('.config.ini')
        self.index = config.get('Setting', 'index').split(',')
        # 读取配置文件
        self.interface = interface
        self.type = 1  # 模式
        self.location = tuple()  # 当前位置
        self.search_area = [list(), list(), list(), list()]  # 检索区
        self.work_area = dict()  # 药方工作区
        self.widgets = list(range(4))
        self.widgets[0] = self.interface.tablewidgetSymptom
        self.widgets[1] = self.interface.tablewidgetDisease
        self.widgets[2] = self.interface.tablewidgetPrescription
        self.widgets[3] = self.interface.tablewidgetMedicine
        # Global Variable
        self.back = Backend()
        # Import function
        # self.init_data() # 不用一开始显示,而且显示会崩溃，原因未查
        # Init data

    def init_data(self):
        data = self.back.init(self.type)
        self.set_all_tables(data)
        return 0

    def get_input(self, box_id, input_box, option_box):
        # 当获取到输入触发此函数，然后在下拉框中显示匹配内容
        text = input_box.text()
        if text:
            data = self.back.query_similar_data(box_id, text)
            if data:
                option_box.show()
                self.set_table(option_box, data)
            else:
                option_box.hide()
        else:
            option_box.hide()
        return 0

    def optioned_data(self, box_id, text):
        # 任意模式下，当option被选中时，显示相关数据
        self.search_area = [list(), list(), list(), list()]
        for widget in self.widgets:
            widget.clear()
        # 初始化
        target_indexs = list()
        self.search_area[box_id].append(text)
        if box_id == 0:
            # 选中的是子类（症状 or 药）
            target_indexs.append(box_id + 1)
        elif box_id == 3:
            target_indexs.append(box_id - 1)
        else:
            target_indexs.append(box_id - 1)
            target_indexs.append(box_id + 1)
        for index in target_indexs:
            sub_data = self.back.union_query(box_id, index, text)
            self.search_area[index] = sub_data
        self.set_all_tables(self.search_area)
        print(self.search_area)
        return 0

    def get_data(self, box_id=1, content=1):
        # 录入模式下，当添加按钮被触发时，将输入的内容添加到数据库
        # 如果当前位置不为空，还要添加关系
        return ['3', '2']

    def save_data(self, box_id,text):
        # if not self.location:
            # text = self.interface.
        return 0

    @staticmethod
    def set_table(table, data_list):
        if data_list:
            row = len(data_list)
            column = len(data_list[0])
            table.setRowCount(row)
            table.setColumnCount(column)
            for r in range(row):
                for c in range(column):
                    table.setItem(r, c, QTableWidgetItem(data_list[r][c]))

    def set_all_tables(self, data):
        cnt = 0
        for item in data:
            if type(item) == list and item:
                # ensure_tuple = (item,)  # 防止每个字单独1列
                ensure_tuple = list()
                for elem in item:
                    ensure_tuple.append((elem, ))
                self.set_table(self.widgets[cnt], ensure_tuple)
            cnt += 1
        return 0


    # 新加方法
    def add_item(self,box_id,text):
        check_id = 0
        for value in self.search_area[box_id]:
            if text == value:
                check_id = check_id + 1
        
        if check_id == 0:
            self.search_area[box_id].append(text)
            print(text)
            if self.type == 0 :
                self.save_data(box_id,text)
   