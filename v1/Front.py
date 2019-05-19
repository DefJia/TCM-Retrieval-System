from configparser import ConfigParser
from Back import Backend
from PyQt5.QtWidgets import QTableWidgetItem


class Frontend:
    def __init__(self, interface, reminder=None, information = None,property=None) :
        config = ConfigParser()
        config.read('.config.ini')
        self.index = config.get('Setting', 'index').split(',')
        # 读取配置文件
        self.interface = interface
        self.reminder = reminder
        self.information = information
        self.property = property
        self.row = 0
        self.column = 0
        self.id = 0
        self.time = 0
        self.type = 1  # 模式
        self.location = tuple()  # 当前位置
        self.search_area = [list(), list(), list(), list()]  # 检索区
        # self.search_area_symptom = list()
        self.prescription_list =list()
        self.mainSymptom = list()
        self.work_area = dict()  # 药方工作区
        self.prescription_list = list() 
        self.widgets = list(range(4))
        self.widgets[0] = self.interface.tablewidgetSymptom
        self.widgets[1] = self.interface.tablewidgetDisease
        self.widgets[2] = self.interface.tablewidgetPrescription
        self.widgets[3] = self.interface.tablewidgetMedicine
        self.viceSymptoms = list(range(6))
        self.viceSymptoms[0] =self.information.lineLook 
        self.viceSymptoms[1] =self.information.lineListen
        self.viceSymptoms[2] =self.information.lineQuestion  
        self.viceSymptoms[3] =self.information.lineFeel 
        self.viceSymptoms[4] =self.information.lineMenstruation  
        self.viceSymptoms[5] =self.information.lineLeucorrhoea
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
        # 当获取到输入，触发此函数，然后在下拉框中显示匹配内容
        text = input_box.text()
        if text:
            data = self.back.query_similar_data(box_id, text)
            if data:
                #print("测试1")
                option_box.show()
                self.set_table(option_box, data)

            else:
                option_box.hide()
                #print("测试")
        else:
            option_box.hide()
        return 0

    def optioned_data(self, box_id, text, mode=0, aaa=0):
        # 任意模式下，当option被选中时，显示相关数据
        # mode为0时只显示右边
        #self.search_area = [list() for i in range(4)]

        '''
        for widget in self.widgets:
            widget.clear()
        '''

        # 初始化 
        if aaa ==0:
            target_indexs = list()
            if [text] not in self.search_area[box_id]:
                self.search_area[box_id].append([text])
            if mode == 1 and box_id != 3:
                target_indexs.append(box_id + 1)

                pass
            '''
            elif mode == 0:
                right = box_id + 1
                if 0 <= right <= 3:
                    target_indexs.append(right)
                 #不需要关系
                pass
            '''
            for index in target_indexs:
                if box_id != 0:
                    sub_data = self.back.union_query(box_id, index, text)
                    if sub_data:
                        self.search_area[index] = sub_data
                else:
                    self.back.search_disease(self.search_area[0])
                    #获取serach_area[0]里面的每一个元素，并启动查询方法传入（search_area[0]），查询里面每一个数
                    #在back里面写方法  Select 病名 from 表 where 病症名 = line.text1 or 病症名 = line.text2 order by xxx
                    #settable()
                    pass
            self.set_all_tables(self.search_area)
            # print(self.search_area)
            return 0
        '''
        elif aaa == 1:
            target_indexs = list()
            if [text] not in self.search_area[box_id]:
                self.search_area[box_id].append([text])
            if mode == 1 and box_id != 3:
                target_indexs.append(box_id + 1)
                pass
            for index in target_indexs:
                sub_data = self.back.union_query(box_id, index, text)
                if sub_data:
                    self.search_area[index] = sub_data
            self.set_all_tables(self.search_area)

            #target_indexs = list()
            if [text] not in self.mainSymptom:
                self.mainSymptom.append([text])

            print(self.mainSymptom)
            self.set_table(self.information.tablewidgetMainSymptom,self.mainSymptom)
            # self.mainSymptom.clear()
            return 0
        '''
    def get_data(self, box_id=1, content=1):
        # 录入模式下，当添加按钮被触发时，将输入的内容添加到数据库
        # 如果当前位置不为空，还要添加关系
        return ['3', '2']

    def save_data(self,index,text):
        # 如何获取点击按钮
        #index = self.group_inputs.index(input_box)
        if index == 0:
            name = "symptom"  #是不是直接这个
        elif index == 1:
            name = "disease"
        elif index == 2:
            name = "prescription"
        elif index == 3:
            name = "medicine"

        if text:
            res = self.back.save_data(name, text)
            if res:
                print('该名称已存在')
            else:
                print('录入成功')
    

    # 新加方法
    def add_item(self, box_id, text):
        check_id = 0
        for value in self.search_area[box_id]:
            if text == value:
                check_id = check_id + 1
        if check_id == 0:
            self.search_area[box_id].append(text)
            # print(text)
            if self.type == 0:
                self.save_data(box_id, text)


    @staticmethod
    def set_table(table, data_list):
        # data_list: [[item, item], [item, item]]
        if data_list:
            print(data_list)

            '''
            for elem in data_list:
                elem.append('克')
            '''
            row = len(data_list)
            column = len(data_list[0])
            print(row,column)
            table.setRowCount(row)
            table.setColumnCount(column)
            for r in range(row):
                columnCurrentRow = len(data_list[r])
                for c in range(columnCurrentRow):
                    table.setItem(r, c, QTableWidgetItem(data_list[r][c]))

        #如果table是开方区的则

    def set_all_tables(self, data):
        cnt = 0
        for item in data:
            if type(item) == list and item:
                self.set_table(self.widgets[cnt], item)
            cnt += 1
        return 0

    def deletedata(self,text,index):
        self.back.deletedate(text,index)
        pass
    
    def final_save(self,table,data):

        self.back.final_save()
        pass
        

if __name__ == '__main__':
    pass