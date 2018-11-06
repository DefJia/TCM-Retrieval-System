class Frontend:
    def __init__(self):
        self.type = 2  # 模式
        self.location = tuple()  # 当前位置
        self.search_area = [list(), list(), list(), list()]  # 检索区
        self.work_area = dict()  # 药方工作区

    def get_input(self):
        # 当获取到输入触发此函数，然后在下拉框中显示匹配内容
        pass

    def get_data(self, box_id=1, content=1):
        # 录入模式下，当添加按钮被触发时，将输入的内容添加到数据库
        # 如果当前位置不为空，还要添加关系
        return ['3', '2']

