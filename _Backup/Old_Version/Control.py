from UI.UI import Ui_MainWindow
from UI.reminder import Ui_reminder
from UI.property import Ui_Property
from UI.information import Ui_Information
from UI.MessageBox import MessageBox
from UI.inquire import Ui_Inquire
from UI.wrong import Ui_Wrong
from UI.final import Ui_final
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Front import Frontend


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
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

class Final(QMainWindow, Ui_final):
    def __init__(self):
        # 修改界面
        super(Final, self).__init__()
        self.setupUi(self)


class Control:
    def __init__(self):
        app = QApplication(sys.argv)
        self.interface = Interface()
        # self.interface.show()
        self.information = Information()
        self.information.show()
        self.interface.show()
        self.reminder = Reminder()
        self.property = Property()
        self.inquire = Inquire()
        self.final = Final()
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

        self.id = 0
        # 定义组件组
        ''' 以下为信号操作 '''
        '''
        for option in self.group_options:  # 下拉框选择
            option.clicked.connect(lambda: self.option_clicked(option))
        for input_box in self.group_inputs:  # 输入框输入
            input_box.textChanged.connect(lambda: self.line_text_changed(input_box))
        '''
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
        # reminder 按钮点击
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
        self.information.IButtonInquire.clicked.connect(lambda: self.inquire.show())
        self.information.IButtonOut.clicked.connect(lambda: self.information.hide())
        # --- information 触发--- #
        self.information.lineSymptom.textChanged.connect(lambda: self.i_line_text_changed())
        self.information.option.hide()

        self.information.option.clicked.connect(lambda: self.i_option_clicked(self.information.option))

        # --- inquire按钮组 --- #
        #self.inquire.ButtonYes.clicked.connect(lambda: self.inquire.hide())
        # --- inquire 触发 --- #



        # --- interface按钮组 --- #
        self.interface.radioButton_2.toggled.connect(lambda: self.change_type())  # 切换模式
        self.interface.buttonInput.clicked.connect(lambda: self.buttonInput_clicked())  # 录入
        self.interface.buttonInitial.clicked.connect(lambda: self.initial_button_clicked())  # 初始化

        self.interface.buttonDelete.clicked.connect(lambda: self.buttonDelete_clicked())  # 删除
        self.interface.buttonDeleterelation.clicked.connect(lambda: self.buttonRelationDelete_clicked())# 删除关系
        self.interface.buttonOut.clicked.connect(lambda: self.interface.hide())  # 删除
        self.interface.buttonSave.clicked.connect(lambda: self.buttonSave_clicked())  # 最终保存
        # --- Inquire按钮组 --- #
        self.inquire.ButtonYes.clicked.connect(lambda: self.iq_buttonYes_clicked())  # 查询
        self.inquire.ButtonOut.clicked.connect(lambda: self.inquire.hide())
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
            self.front.type = 1
            self.interface.labelType.setText('开方模式')
            self.interface.groupboxSymptom.setGeometry(10, 70, 211, 411)
            self.interface.groupboxDisease.setGeometry(220, 70, 241, 411)
            for addition in self.group_additions:
                addition.hide()
        else:
            self.front.type = 0
            self.interface.labelType.setText('录入模式')

            self.interface.groupboxSymptom.setGeometry(220, 70, 241, 411)
            self.interface.groupboxDisease.setGeometry(10, 70, 211, 411)

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
        self.group_inputs[index].setText("")
        option.hide()
        mode = self.front.type
        self.front.optioned_data(index, text, mode)
        pass

    def i_option_clicked(self, option):
        # 检测到下拉框被点击
        text = str(option.selectedItems()[0].text())
        print(text)
        #print("1")
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
        if text != '':
            # self.reminder.show()
            result = self.show_reminder('', '添加成功')
            print(text)  # test
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
        pass


    def buttonSave_clicked(self):
        '''
        for i in 7:
            for j in 8:
                if self.interface.tablewidgetPrescribe(i, j) != "null":
                    self.prescription_area.append(self.interface.tablewidgetPrescribe(i, j))
        '''
        #print(id)
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
            if self.group_tables[i].selectedItems():
                text = self.group_tables[i].selectedItems()[0].text()
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
            medicines = self.front.search_area[3]
            if int(len(medicines))%4 == 0:
                row = int(len(medicines) / 4)
            else: row = int(len(medicines) / 4) + 1
            text_all = [list() for i in range(row)]
            n = 0
            for i in medicines:
                text_all[int(n/4)] += i
                n+=1
            self.front.set_table(self.group_tables[5], text_all)

        elif self.front.type == 0:
            for i in range(3):
                if len(self.front.search_area[i])!= 0 and len(self.front.search_area[i+1]) != 0:
                    for l in self.front.search_area[i]:
                        for m in self.front.search_area[i+1]:
                            self.front.back.save_relation(i,l[0],m[0])
            for list0 in self.front.search_area:
                list0.clear()
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
        self.information.lineGender.setText(gender)
        self.information.lineAge.setText(age)
        self.information.linePhone.setText(phone)
        self.information.lineIdentitynum.setText(idcard)
        self.information.lineAddress.setText(address)
        

#information 面板
    def i_buttonInput_clicked(self):
        name = self.information.lineName.text()
        gender = self.information.lineGender.text()
        age = self.information.lineAge.text()
        phone = self.information.linePhone.text()
        identitynum = self.information.lineIdentitynum.text()
        address = self.information.lineAddress.text()

        #inquirydate = line
        look = self.information.lineLook.text()
        listen = self.information.lineListen.text()
        question = self.information.lineQuestion.text()
        feel = self.information.lineFeel.text()
        menstruation = self.information.lineMenstruation.text()
        leucorrhoea = self.information.lineLeucorrhoea.text()
        #prescription = self.information.linePrescription.text()
        #mainsymptom = self.information.lineSymptom.text()
        mainsymptom = self.front.search_area[0]
        print (self.front.search_area[0])
        prescription= "null"

        print(name,gender,age,
        phone,identitynum,address,look,listen,question,feel,menstruation,leucorrhoea,prescription,mainsymptom)

        self.front.back.i_save_data(name,gender,age,
        phone,identitynum,address,look,listen,question,feel,menstruation,leucorrhoea,prescription,mainsymptom)
        self.interface.show()
        self.id =self.front.back.i_save_data(name,gender,age,
        phone,identitynum,address,look,listen,question,feel,menstruation,leucorrhoea,prescription,mainsymptom)
        print(id)
        self.information.hide()
        pass

#iinquire 面板
    def iq_buttonYes_clicked(self):
        name = self.inquire.lineName.text()
        phone = self.inquire.linePhone.text()
        idcard = self.inquire.lineIdcard.text()

        data = self.front.back.iq_inquire(name,phone,idcard)
        self.front.set_table(self.inquire.tableWidget, data)
        pass

if __name__ == "__main__":
    test = Control()