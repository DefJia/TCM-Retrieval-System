from UI.UI import Ui_MainWindow
from UI.reminder import Ui_reminder
from UI.property import Ui_Property
from UI.information import Ui_Information
from UI.MessageBox import MessageBox
from UI.inquire import Ui_Inquire
from UI.wrong import Ui_Wrong
from UI.final import Ui_final_2
from UI.yes import Ui_Yes
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QFileDialog
import sys
from Front import Frontend
from UI.missPhone import Ui_missPhone
import time
from UI.quantity import Ui_quantity
from UI.result import Ui_result
from UI.relationDelete import Ui_relationDelete
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.login import Ui_LogIn
from UI.logwrong import Ui_LogWrong
import time
import getpass

class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 修改界面
        super(Interface, self).__init__()
        self.setupUi(self)

class Reminder(QMainWindow, Ui_reminder):
    def __init__(self):
        # 修改界面
        super(Reminder, self).__init__()
        self.setupUi(self)

class Information(QMainWindow, Ui_Information):
    def __init__(self):
        # 修改界面
        super(Information, self).__init__()
        self.setupUi(self)

class Wrong(QMainWindow, Ui_Wrong):
    def __init__(self):
        # 修改界面
        super(Wrong, self).__init__()
        self.setupUi(self)

'''
class ReminderAdvanced(QMainWindow, MessageBox, title, text):
    app = QApplication(sys.argv)
    main_window = MessageBox(title, text)
    main_window.show()
    sys.exit(app.exec_())
'''

class Property(QMainWindow, Ui_Property):
    def __init__(self):
        # 修改界面
        super(Property, self).__init__()
        self.setupUi(self)

class Inquire(QMainWindow, Ui_Inquire):
    def __init__(self):
        # 修改界面
        super(Inquire, self).__init__()
        self.setupUi(self)

class Final(QMainWindow, Ui_final_2):
    def __init__(self):
        # 修改界面
        super(Final, self).__init__()
        self.setupUi(self)

class Yes(QMainWindow, Ui_Yes):
    def __init__(self):
        # 修改界面
        super(Yes, self).__init__()
        self.setupUi(self)

class Quantity(QMainWindow, Ui_quantity):
    def __init__(self):
        # 修改界面
        super(Quantity, self).__init__()
        self.setupUi(self)

class Result(QMainWindow, Ui_result):
    def __init__(self):
        super(Result, self).__init__()
        self.setupUi(self)

class MissPhone(QMainWindow, Ui_missPhone):
    def __init__(self):
        super(MissPhone, self).__init__()
        self.setupUi(self)

class RelationDelete(QMainWindow, Ui_relationDelete):
    def __init__(self):
        super(RelationDelete, self).__init__()
        self.setupUi(self)

class LogIn(QMainWindow, Ui_LogIn):
    def __init__(self):
        super(LogIn, self).__init__()
        self.setupUi(self)

class LogWrong(QMainWindow, Ui_LogWrong):
    def __init__(self):
        super(LogWrong, self).__init__()
        self.setupUi(self)

class Control:
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        #self.interface.show()
        #self.inquire.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.quantity = Quantity()
        #self.quantity.show()
        self.information = Information()
        #self.information.show()
        #self.RelationDelete.show()
        self.interface.show()
        self.reminder = Reminder()
        self.property = Property()
        self.inquire = Inquire()
        self.final = Final()
        #self.final.show()
        self.yes = Yes()
        self.result = Result()
        self.missPhone = MissPhone()
        self.relationdelete = RelationDelete()
        self.login = LogIn()
        self.logwrong = LogWrong()
        self.login.show()
        #self.inquire.show()
        #self.missPhone.show()
        # 界面生成
        self.front = Frontend(self.interface, self.reminder, self.information, self.property)
        # 定义交互Class
        self.group_inputs = list()
        self.group_inputs.append(self.interface.lineSymptom)
        self.group_inputs.append(self.interface.lineDisease)
        self.group_inputs.append(self.interface.linePrescription)
        self.group_inputs.append(self.interface.lineMedicine)
        self.group_additions = list()
        self.group_additions.append(self.interface.buttonSymptom)
        self.group_additions.append(self.interface.buttonDisease)
        self.group_additions.append(self.interface.buttonPrescription)
        self.group_additions.append(self.interface.buttonMedicine)
        self.group_options = list()
        self.group_options.append(self.interface.symptomOption)
        self.group_options.append(self.interface.diseaseOption)
        self.group_options.append(self.interface.prescriptionOption)
        self.group_options.append(self.interface.medicineOption)
        self.group_tables = list()
        self.group_tables.append(self.interface.tablewidgetSymptom)
        self.group_tables.append(self.interface.tablewidgetDisease)
        self.group_tables.append(self.interface.tablewidgetPrescription)
        self.group_tables.append(self.interface.tablewidgetMedicine)
        self.group_tables.append(self.interface.tablewidgetBook)
        self.group_tables.append(self.interface.tablewidgetPrescribe)
        #self.front.back.final_save()


        # 定义组件组
        ''' 以下为信号操作 '''
        '''
        for option in self.group_options:  # 下拉框选择
            option.clicked.connect(lambda: self.option_clicked(option))
        for input_box in self.group_inputs:  # 输入框输入
            input_box.textChanged.connect(lambda: self.line_text_changed(input_box))
        '''
        # --- login按钮组 --- #
        self.login.yesButton.clicked.connect(lambda: self.start())
        self.login.noButton.clicked.connect(lambda: self.login.close())


        # --- interface按钮组 --- #
        self.interface.tablewidgetSymptom.clicked.connect(lambda: self.table_option_clicked(0))
        self.interface.tablewidgetDisease.clicked.connect(lambda: self.table_option_clicked(1))
        self.interface.tablewidgetPrescription.clicked.connect(lambda: self.table_option_clicked(2))
        self.interface.tablewidgetMedicine.clicked.connect(lambda: self.table_option_clicked(3))
        self.interface.symptomOption.clicked.connect(lambda: self.option_clicked(self.interface.symptomOption))
        self.interface.diseaseOption.clicked.connect(lambda: self.option_clicked(self.interface.diseaseOption))
        self.interface.prescriptionOption.clicked.connect(lambda: self.option_clicked(self.interface.prescriptionOption))
        self.interface.medicineOption.clicked.connect(lambda: self.option_clicked(self.interface.medicineOption))
        self.interface.lineSymptom.textChanged.connect(lambda: self.line_text_changed(self.interface.lineSymptom))
        self.interface.lineDisease.textChanged.connect(lambda: self.line_text_changed(self.interface.lineDisease))
        self.interface.linePrescription.textChanged.connect(lambda: self.line_text_changed(self.interface.linePrescription))
        self.interface.lineMedicine.textChanged.connect(lambda: self.line_text_changed(self.interface.lineMedicine))
        # 加号按钮
        self.interface.buttonSymptom.clicked.connect(lambda: self.button_clicked(self.interface.lineSymptom))
        self.interface.buttonDisease.clicked.connect(lambda: self.button_clicked(self.interface.lineDisease))
        self.interface.buttonPrescription.clicked.connect(lambda: self.button_clicked(self.interface.linePrescription))
        self.interface.buttonMedicine.clicked.connect(lambda: self.button_clicked(self.interface.lineMedicine))
        #  按钮隐藏
        self.interface.buttonDeleterelation.hide()
        # self.reminder.buttonYes.clicked.connect(lambda: self.button_yes_reminder())
        # self.reminder.buttonNo.clicked.connect(lambda: self.button_no_reminder())
        '''
        self.interface.buttonDisease.clicked.connect(lambda: self.button_clicked(self.interface.diseaseOption))
        self.interface.buttonPrescription.clicked.connect(lambda: self.button_clicked(self.interface.prescriptionOption))
        self.interface.buttonMedicine.clicked.connect(lambda: self.button_clicked(self.interface.medicineOption))
        '''
        # --- information按钮组 --- #
        self.information.IButtonYes.clicked.connect(lambda: self.i_buttonInput_clicked())
        #self.information.IButtonYes.clicked.connect(lambda: self.interface.show())
        self.information.IButtonGetinUI.clicked.connect(lambda: self.interface.show())
        self.information.IButtonInquire.clicked.connect(lambda: self.inquire.show())
        self.information.IButtonOut.clicked.connect(lambda: self.information.hide())
        # --- information 触发--- #
        self.information.lineSymptom.textChanged.connect(lambda: self.i_line_text_changed())
        self.information.option.hide()
        self.information.DBOutput.clicked.connect(lambda: self.output())
        self.information.DBInput.clicked.connect(lambda: self.input())
        self.information.option.clicked.connect(lambda: self.i_option_clicked(self.information.option))

        # --- inquire按钮组 --- #
        #self.inquire.ButtonYes.clicked.connect(lambda: self.inquire.hide())
        # --- inquire 触发 --- #

        # --- interface按钮组 --- #
        self.interface.radioButton_2.toggled.connect(lambda: self.change_type())  # 切换模式
        self.interface.buttonInput.clicked.connect(lambda: self.yes.show())  # 录入
        self.yes.yesButton.clicked.connect(lambda: self.buttonInput_clicked())
        self.interface.buttonInitial.clicked.connect(lambda: self.initial_button_clicked())  # 初始化
        self.interface.buttonClean.clicked.connect(lambda: self.buttonClean_clicked())

        self.interface.buttonDelete.clicked.connect(lambda: self.buttonDelete_clicked())  # 删除
        self.interface.buttonDeleterelation.clicked.connect(lambda: self.relationdelete.show())# 删除关系
        self.interface.buttonOut.clicked.connect(lambda: self.interface_out())  # 退出
        self.interface.buttonSave.clicked.connect(lambda: self.final.show())  # 最终保存

        # --- RelationDelete按钮组 --- #
        self.relationdelete.buttonYes.clicked.connect(lambda: self.buttonRelationDelete_clicked())
        self.relationdelete.buttonNo.clicked.connect(lambda: self.relationdelete.hide())

        # --- Inquire按钮组 --- #
        self.inquire.ButtonYes.clicked.connect(lambda: self.iq_buttonYes_clicked())  # 查询
        self.inquire.ButtonOut.clicked.connect(lambda: self.inquire_button_out())
        # --- Final按钮组 --- #
        #self.interface.buttonSave.clicked.connect(lambda: self.buttonSave_clicked())
        self.final.buttonContinue.clicked.connect(lambda: self.buttonContinue_click())
        self.final.buttonOut.clicked.connect(lambda: self.buttonOut_click())

        # --- quantity按钮组件 ---#
        self.quantity.pushButton.clicked.connect(lambda: self.quantity_button_clicked())

        # --- result按钮组件 ---#
        self.inquire.tableWidget.doubleClicked.connect(lambda: self.inquire_widget_double_clicked(self.inquire.tableWidget))
        self.result.ButtonOut.clicked.connect(lambda: self.buttonOut_clicked())
        self.result.tableWidget.doubleClicked.connect(lambda: self.result_widget_double_clicked(self.result.tableWidget))
        #self.interface.tablewidgetPrescription.clicked.connect(lambda: self.table_option_clicked(2))
        #self.inquire.show()
        #self.interface.tablewidgetSymptom.clicked.connect(lambda: self.table_option_clicked(0))

        # --- 缺失手机按钮组件 ---#
        self.missPhone.yesButton.clicked.connect(lambda: self.missPhone_clicked())
        self.logwrong.yesButton.clicked.connect(lambda: self.logwrong.close())

        #self.interface.show()
        ''' 以下为界面初始化处理 '''
        for i in range(8):
            # 设定药方区结构
            if i % 2 == 0:
                self.interface.tablewidgetPrescribe.setColumnWidth(i, 150)
            else:
                self.interface.tablewidgetPrescribe.setColumnWidth(i, 69)
        tmp = [90, 50, 50]
        for i in range(3):
            self.interface.tablewidgetMedicine.setColumnWidth(i, tmp[i])
        for addition in self.group_additions: addition.hide()  # 隐藏加号
        for table in self.group_tables: table.setShowGrid(False)  # 隐藏内边框
        for option in self.group_options: option.hide()  # 隐藏下拉框
        # self.front.set_table(self.interface.tablewidgetMedicine, data)
        # 测试代码
        sys.exit(app.exec_())

    def output(self):
        import shutil, datetime
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.copyfile('Data/Main.db', 'Data/%s.bak' % time)
        self.show_reminder('数据库导出', '导出成功：%s.bak' % time)

    def input(self):
        import shutil
        file = QFileDialog.getOpenFileName()
        self.show_reminder('数据库导入', '警告：原有数据库将被覆盖，继续？')
        self.output()
        shutil.copyfile(file[0], 'Data/Main.py')
        self.show_reminder('数据库导入', '导入成功')

    @staticmethod
    def show_reminder(title, text):
        # 显示弹框
        main_window = MessageBox(title, text)
        main_window.show()
        return main_window.status
        # 1 -> Yes, 0 -> No

    def change_type(self):
        #  切换模式
        for widget in self.group_tables[0:4]:
            widget.clear()
        for list0 in self.front.search_area:
            list0.clear()
        for line in self.group_inputs:
            line.clear()
        # 清空当前所有信息
        if self.interface.radioButton_2.isChecked():
            print("当前处于开方模式")
            self.interface.tablewidgetMedicine.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.front.type = 1
            self.interface.labelType.setText('开方模式')
            self.interface.groupboxSymptom.setGeometry(10, 70, 211, 411)
            self.interface.groupboxDisease.setGeometry(220, 70, 241, 411)
            self.interface.tablewidgetMedicine.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            for addition in self.group_additions:
                addition.hide()
            self.interface.buttonDeleterelation.hide()
        else:
            self.front.type = 0
            self.interface.labelType.setText('录入模式')
            self.interface.tablewidgetMedicine.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
            self.interface.groupboxSymptom.setGeometry(220, 70, 241, 411)
            self.interface.groupboxDisease.setGeometry(10, 70, 211, 411)
            self.interface.buttonDeleterelation.show()
            self.interface.tablewidgetMedicine.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            print("当前处于录入模式")
            for addition in self.group_additions:
                addition.show()
        pass

    def line_text_changed(self, input_box):
        # 检测到输入框有输入
        index = self.group_inputs.index(input_box)
        self.front.get_input(index, input_box, self.group_options[index])
        pass


    def i_line_text_changed(self):
        #information界面的方法
        self.front.get_input(0, self.information.lineSymptom, self.information.option)
        pass

    def option_clicked(self, option):
        # 检测到下拉框被点击
        index = self.group_options.index(option)
        text = str(option.selectedItems()[0].text())
        data = "0"
        self.group_inputs[index].setText("")
        #清空line里面的内容
        option.hide()
        mode = self.front.type
        self.front.optioned_data(index, text, mode, data)
        pass

    def i_option_clicked(self, option):
        # 检测到下拉框被点击
        text = str(option.selectedItems()[0].text())
        self.information.option.clear()
        option.hide()
        print("1")
        self.front.optioned_data(0, text, 0, 1)
        self.information.lineSymptom.clear()
        pass

    def table_option_clicked(self, table_id):
        # 检测到列表中的选项被选中
        table = self.group_tables[table_id]
        mode = self.front.type
        try:
            if table_id != 3 :
                text = str(table.selectedItems()[0].text())
                self.front.optioned_data(table_id, text, mode)
        except IndexError:
            pass

    def button_clicked(self, line):
        # 录入模式中，当+按钮被点击
        # self.interface.buttonSymptom.clicked.connect(lambda: self.front.save_data(0))
        text = line.text()
        index = self.group_inputs.index(line)
        if text != '':
            # self.reminder.show()
            result = self.show_reminder('', '是否添加')
            #print(text)  # test
            if result:
                # 点击yes
                listIndex = []
                for i in self.group_inputs:
                    if i.text():
                        index = self.group_inputs.index(i)
                        listIndex.append(index)
                for l in listIndex:
                    self.front.save_data(l, text)
                    if l == 3:
                        self.front.search_area[l].append([text," "])
                        print(self.front.search_area[l])
                    else:
                        self.front.search_area[l].append([text])
                    self.front.set_all_tables(self.front.search_area)
                    line.clear()
                    self.reminder.hide()
                print(1)
        '''
        if text != '' and index == 3:
            self.quantity.show()
            # self.reminder.show()
            result = self.show_reminder('', '添加成功')
            # print(text)  # test
            if result:
                # 点击yes
                listIndex = []
                for i in self.group_inputs:
                    if i.text():
                        index = self.group_inputs.index(i)
                        listIndex.append(index)
                for l in listIndex:
                    line = self.group_inputs[l]
                    text = line.text()
                    self.front.save_data(l, text)
                    self.front.search_area[l].append([text])
                    self.front.set_all_tables(self.front.search_area)
                    line.clear()
                    self.reminder.hide()
                print(1)
        
        #这个怎么搞？self.group_additions
        pass
        '''

    def quantity_button_clicked(self):
        text = self.quantity.lineQuantity.text()
        print(text)
        self.front.search_area[3].append([text])

        self.quantity.hide()

        pass

    def buttonSave_clicked(self):
        '''
        for i in 7:
            for j in 8:
                if self.interface.tablewidgetPrescribe(i, j) != "null":
                    self.prescription_area.append(self.interface.tablewidgetPrescribe(i, j))
        '''

        print("输出id" + self.front.id)

        #self.front.id = 0
        #待测试


        self.final.show()
        pass
    '''
    def button_yes_reminder(self):
        # self.front.save_data(self.interface.lineSymptom,'（需要变化）',box_id)
        """
        text = self.interface.lineSymptom.text()
        #print(text)
        index = self.group_inputs.index(self.interface.lineSymptom)
        #print(index)
        self.front.save_data(index,text)
        self.reminder.hide()
        self.front.search_area[index].append([text])
        self.front.set_all_tables(self.front.search_area)
        self.interface.lineSymptom.clear()
        """
        listIndex = []
        for i in self.group_inputs:
            if i.text():
                index = self.group_inputs.index(i)
                listIndex.append(index)
        
        for l in listIndex:
            line = self.group_inputs[l]
            text = line.text()
            self.front.save_data(l,text)
            self.front.search_area[l].append([text])
            self.front.set_all_tables(self.front.search_area)
            line.clear()
            self.reminder.hide()
        
        #print(text)
        
        #print(index)
    ''''''
    '''
    def buttonRelationDelete_clicked(self):
        for i in range(3):
            if len(self.front.search_area[i])!= 0 and len(self.front.search_area[i+1]) != 0:
                for l in self.front.search_area[i]:
                    for m in self.front.search_area[i+1]:
                        self.front.back.drop_relation(i, l[0], m[0])
        self.relationdelete.hide()
        print("###删除关系后")
        print(self.front.search_area[3])
        #self.initial_button_clicked()
        '''
        for i in self.front.search_area:
            i.clear()
        for widget in self.group_tables[0:5]:
            widget.clear()
        '''
        pass


    def buttonDelete_clicked(self):
        #index = self.table_option_clicked().index
        #text = self.table_option_clicked().text
        for i in range(4):
            if self.group_tables[i].selectedItems() and i != 3:
                text = self.group_tables[i].selectedItems()[0].text()
                print(text)
                self.front.search_area[i].remove([text])

            if self.group_tables[i].selectedItems() and i == 3:
                text1 = self.group_tables[i].selectedItems()[0].text()
                text2 = self.group_tables[i].selectedItems()[1].text()
                if text2:
                    print(self.front.search_area[i])
                    self.front.search_area[i].remove([text1,text2])
                else:
                    self.front.search_area[i].remove([text])

        for widget in self.group_tables[0:4]:
            widget.clear()
        self.front.set_all_tables(self.front.search_area)

    '''
        for widget in self.group_tables[0:5]:
            widget.clear()

        #self.front.back.deletedate(index,text)
        #for i in self.group_tables[0:5]:
            #if i clicked:
                #self.front.search_area[i].selected.clear
                #self.group_tables[i].selected.clear
    
        #self.front.back.deletedate(index,text)

   
    def button_no_reminder(self):
        self.reminder.hide()
        """
        self.interface.buttonSymptom.clicked.connect(lambda: self.front.save_data(0, self.interface.lineSymptom,self.reminder))
        self.interface.buttonDisease.clicked.connect(lambda: self.front.save_data(1, self.interface.lineDisease,self.reminder))
        self.interface.buttonPrescription.clicked.connect(lambda: self.front.save_data(2, self.interface.linePrescription,self.reminder))
        self.interface.buttonMedicine.clicked.connect(lambda: self.front.save_data(3, self.interface.lineMedicine,self.reminder))
        """
        pass
    '''

    def initial_button_clicked(self):
        # 初始化按钮
        for i in self.front.search_area:
            i.clear()
        for widget in self.group_tables[0:5]:
            widget.clear()
        '''
        for j in self.front.widgets:
            j.clear()
        for i in self.group_tables:
            i.clear
        '''
    def buttonInput_clicked(self):
        # 录入按钮
        if self.front.type == 1:
            # 开方模式
            medicines = self.front.search_area[3]
            print(medicines)
            list_1 =list()
            self.get_table_data(self.interface.tablewidgetPrescribe,list_1) #获取所有输入的药
            if list_1 == ['', '']:
                list_1 = []
            print("******")
            print(list_1) #每次都获取开方区里的所有数据
            list_2 =list() #改变list_1里面的结构
            list_3 =list() #改变medicines里面的结构
            print("***")
            print(self.front.result_list)

            for j in range(len(medicines)):
                list_3 += medicines[j]
                print(list_3)
                    #同理，改变结构
            list_1 = list_1 + list_3
            print(list_1)
                #把两个列表合成一个列表
            if list_1[0] == " ":
                del list_1[0]

            if int(len(list_1)) % 8 == 0:
                row = int(len(list_1) / 8)
            else:
                row = int(len(list_1) / 8) + 1
            print(row)
            list_4 = [list() for i in range(row)]
            n = 0
            for i in list_1:
                list_4[int(n / 8)].append(i)
                # self.group_tables[5][int(n / 4)].append('')
                n += 1
                print(list_4)
            self.front.set_table(self.group_tables[5], list_4)
            self.interface.tablewidgetMedicine.clear()
            self.front.search_area[3].clear()
            #self.front.result_list.clear()
            #self.front.set_table(self.group_tables[5], text_all)

            '''
            if int(len(list_1)) % 4 == 0:
                row = int(len(list_1) / 4)
            else:
                row = int(len(list_1) / 4) + 1
            text_all = [list() for i in range(row)]
            print(text_all)
            # 这句什么意思
            n = 0
            for i in list_1:
                text_all[int(n/4)] += i
                n+=1
                print(text_all)
            '''
            '''
            #加一个方法，让如果list里面有，则把text_all加载list后面，否则直接用
           
            if self.front.result_list:
                list1 = self.front.result_list[-1]
                if len(list1) <= 6:
                print(list1[-1])
                text_all_add = list()
                text_all_add = self.front.result_list + text_all
                self.front.set_table(self.group_tables[5], text_all_add)
            #下面的不应该用text_all应该用
            else:
                self.front.set_table(self.group_tables[5], text_all)
            self.front.result_list.clear()
            #print("测试" + self.group_table[5])
            '''
        elif self.front.type == 0:
            #录入模式
            print("###录入前")
            print(self.front.search_area[3])
            for i in range(3):
                if i < 2 and len(self.front.search_area[i])!= 0 and len(self.front.search_area[i+1]) != 0:
                    for l in self.front.search_area[i]:
                        for m in self.front.search_area[i+1]:
                            self.front.back.save_relation(i,l[0],m[0])

                if i == 2 and len(self.front.search_area[i])!= 0 and len(self.front.search_area[i+1]) != 0:
                    self.get_table_data(self.interface.tablewidgetMedicine, self.front.medicine_gram_list)

                    print("******")
                    #print(int(len(self.front.medicine_gram_list) / 2))

                    for i in range(int(len(self.front.medicine_gram_list) / 2)):
                        #print(self.front.medicine_gram_list[0])
                        meidi = self.front.medicine_gram_list[2 * i]
                        gram = self.front.medicine_gram_list[2 * i+1]
                        print(self.front.search_area[2][0])
                        for j in self.front.search_area[2]:
                            self.front.back.save_relation_gram(j[0],meidi,gram)

            for list0 in self.front.search_area:
                list0.clear()
        self.yes.hide()
        '''
        rows = self.interface.tablewidgetMedicine.rowCount()

        for rows_index in range(rows):
            # print items[item_index].text()
            print(self.interface.tablewidgetMedicine.item(rows_index, 0).text())
        print(rows)
        '''
        pass
    def get_history(self):
        if self.information.linePhone != "" :
            patientID = self.front.back.getPatientID('phone',self.information.linePhone.text())
            if len(patientID) == 0 :
                self.show_reminder("注意","查无此人！")
                return 0
        elif self.information.lineIdcard != "":
            patientID = self.front.back.getPatientID('identitynum',self.information.lineIdentitynum.text())
            if len(patientID) == 0 :
                self.show_reminder("注意","查无此人！")
                return 0
        else:
            self.show_reminder("注意","请输入手机或身份证！")

            
    def set_patient_info(self,patientID):
        name,gender,age,phone,identitynum,address = self.front.back.get_full_patient_info(patientID)
        self.information.lineName.setText(name)
        self.information.boxGender.setText(gender)
        self.information.lineAge.setText(age)
        self.information.linePhone.setText(phone)
        self.information.lineIdentitynum.setText(identitynum)
        self.information.lineAddress.setText(address)

    def buttonClean_clicked(self):
        self.group_tables[5].clear
        self.front.set_table(self.group_tables[5], " ")
        self.front.prescription_list.clear()

#information 病人信息录入面板
    def i_buttonInput_clicked(self):
        try:
            print(self.information.boxGender.currentText())
            name = self.information.lineName.text()
            gender = self.information.boxGender.currentText()
            age = self.information.lineAge.text()
            phone = self.information.linePhone.text()
            identitynum = self.information.lineIdentitynum.text()
            address = self.information.lineAddress.text()

            self.front.look = self.information.lineLook.text()
            self.front.listen = self.information.lineListen.text()
            self.front.question = self.information.lineQuestion.text()
            self.front.feel = self.information.lineFeel.text()
            self.front.menstruation = self.information.lineMenstruation.text()
            self.front.leucorrhoea = self.information.lineLeucorrhoea.text()
            #prescription = self.information.linePrescription.text()
            #mainsymptom = self.information.lineSymptom.text()
            self.front.mainsymptom = self.front.search_area[0]
            #print (self.front.search_area[0])
            prescription= "null"
            #print(name,gender,age,
            #phone,identitynum,address,look,listen,question,feel,menstruation,leucorrhoea,prescription,mainsymptom)
            print(phone)
            print(identitynum)
            while phone == "" and identitynum == "":
                #phone = self.information.linePhone.text()
                phone = 0
            else:
                if identitynum == "":
                    print(identitynum)
                    identitynum = "000000000000000000"
                    #这里有错
                    id = "000000000000000000" + phone

                else:
                    id = identitynum + phone
                    #inquirydate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    print(id)
            self.front.id = id
            #self.front.time = inquirydate
            signal = self.front.back.i_save_data(name,gender,age,phone,identitynum,address,id)
            if signal == 0:
                data = self.front.back.iq_inquire(name, phone , identitynum)
                if data != 0:
                    self.front.set_table(self.inquire.tableWidget, data)
                    self.inquire.show()
            else:
                self.interface.show()
            self.information.hide()

            #清除所有的空
            self.information.lineName.clear()
            #self.information.boxGender.clear()
            self.information.lineAge.clear()
            self.information.linePhone.clear()
            self.information.lineIdentitynum.clear()
            self.information.lineAddress.clear()

            # inquirydate = line
            self.information.lineLook.clear()
            self.information.lineListen.clear()
            self.information.lineQuestion.clear()
            self.information.lineFeel.clear()
            self.information.lineMenstruation.clear()
            self.information.lineLeucorrhoea.clear()
            # prescription = self.information.linePrescription.text()
            # mainsymptom = self.information.lineSymptom.text()
            self.front.mainsymptom = self.front.search_area[0]
        except Exception as e:
            print(e)
        pass

#iinquire 面板
    def iq_buttonYes_clicked(self):
        name = self.inquire.lineName.text()
        phone = self.inquire.linePhone.text()
        idcard = self.inquire.lineIdcard.text()

        data = self.front.back.iq_inquire(name,phone,idcard)
        print(data)
        self.front.set_table(self.inquire.tableWidget, data)
        pass

#final面板
    def get_table_data(self,table,list):
        row = table.rowCount()
        column = table.columnCount()
        print(column)
        for i in range(row):
            for j in range(column):
                try:
                    print(table.item(i, j))
                    print(table.item(i, j).text())
                except Exception as e:
                    print(e)
                if table.item(i, j) is not None and table.item(i, j).text() != "NULL" :#********可能有问题
                    list.append(table.item(i, j).text())
                    print(list)

    def interface_out(self):
        self.interface.hide()
        self.front.result_list.clear()
        self.information.show()

    def buttonOut_click(self):
        self.final.hide()
        self.information.hide()
        self.interface.hide()
        self.get_table_data(self.interface.tablewidgetPrescribe, self.front.prescription_list)
        print(self.front.prescription_list)
        self.front.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.front.final_save(self.front.prescription_list, self.front.id, self.front.time)
        self.front.id = 0
        self.front.time = 0
        self.initial_button_clicked()
        self.front.prescription_list.clear()
        self.information.tablewidgetMainSymptom.clear()
        self.front.result_list.clear()
        self.interface.tablewidgetPrescribe.clear()


    def buttonContinue_click(self):
        self.interface.hide()
        self.information.show()
        self.final.hide()
        self.get_table_data(self.interface.tablewidgetPrescribe, self.front.prescription_list)
        print(self.front.prescription_list)
        self.front.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.front.final_save(self.front.prescription_list, self.front.id, self.front.time)
        self.front.id = 0
        self.front.time = 0
        self.initial_button_clicked()
        self.information.tablewidgetMainSymptom.clear()
        self.front.result_list.clear()
        #print(self.front.prescription_list)
        print("====")
        self.front.prescription_list.clear()
        self.initial_button_clicked()
        print("====清空后")
        print(self.front.prescription_list)
        self.interface.tablewidgetPrescribe.clear()
        #data = 遍历开方区里面的内容
        #self.front.back.final_save(self.front.id,data)

    def inquire_widget_double_clicked(self,table):
        #text = str(table.selectedIteams().text())
        try:
            id = str(table.selectedItems()[6].text())
            self.front.id = id
            print(id)
            if id:
                data = self.front.back.get_click_result(id)
                print(data)
                self.front.set_table(self.result.tableWidget,data)
                self.result.show()
        except Exception as e:
            print(e)

    def buttonOut_clicked(self):
        self.result.hide()
        self.initial_button_clicked()

    def inquire_button_out(self):
        self.inquire.hide()
        self.inquire.lineName.clear()
        self.inquire.lineIdcard.clear()
        self.inquire.linePhone.clear()
        self.inquire.tableWidget.clear()

    def result_widget_double_clicked(self,table):
        time = str(table.selectedItems()[0].text())
        data = self.front.back.result_UI_show(time) #得到之前的开方
        self.interface.show()
        print(data)
        data = data[0][0][2: -2].split("', '")
        print(data)
        if int(len(data)) % 8 == 0:
            row = int(len(data) / 8)
        else:
            row = int(len(data) / 8) + 1
        self.front.result_list = [list() for i in range(row)]
        n = 0
        for i in data:
            self.front.result_list[int(n / 8)].append(i) #往result_list里面添加数据
            #self.group_tables[5][int(n / 4)].append('')
            n += 1
            #print(self.front.result_list)
            try:
                self.front.set_table(self.interface.tablewidgetPrescribe, self.front.result_list)
            except Exception as e:
                print(e)
        print(self.front.result_list)

    def missPhone_clicked(self):
        self.missPhone.hide()

    def start(self):
        user = self.login.lineUser.text()
        pasw = self.login.linePassword.text()
        if user == 'abc123' and pasw == '123':
            self.login.close()
            self.information.show()
        else:
            self.logwrong.show()
            self.login.linePassword.clear()


if __name__ == "__main__":
    test = Control()