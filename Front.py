from configparser import ConfigParser
from Back import Backend


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
        # Global Variable
        self.back = Backend()
        # Import function
        data = self.back.init(self.type)
        

    def init_data(self):
        pass

    def get_input(self, box_id):
        # 当获取到输入触发此函数，然后在下拉框中显示匹配内容
        if box_id == 0: text = self.interface.lineSymptom.text()
        elif box_id == 1: text = self.interface.lineDisease.text()
        elif box_id == 2: text = self.interface.linePrescription.text()
        elif box_id == 3: text = self.interface.lineMedicine.text()
        else: text = ''
        if text:
            data = self.back.get_data(box_id, text)
        return 0

    def get_data(self, box_id=1, content=1):
        # 录入模式下，当添加按钮被触发时，将输入的内容添加到数据库
        # 如果当前位置不为空，还要添加关系
        return ['3', '2']

    @staticmethod
    def setTable(table, dataList):
        row = len(dataList)
        column = len(dataList[0])
        table.setRowCount(row)
        table.setColumnCount(column)
        for r in range(row):
            for c in range(column):
                table.setItem(r, c, QTableWidgetItem(dataList[r][c]))

