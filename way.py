import PyQt5.QtWidgets
from PyQt5 import QtWidgets
import UI
def SearchTable(cursor,id,mg):
    #try:
        cursor.execute("sql")
        #sql= " WHERE aid= '" + str(id) + "' "
        #data = cursor.fetchone()
        data1 = cursor.fetchall()
    #顺序
        #print(data)
        #print(data1)
        #print(len(data))
        #print(len(data1))

        row = len(data1)
        #col = len(data)
        mg.tableWidget_guanli.setRowCount(row)
        #print("检查")
        for rows in range(row):
            for columns in range(4):
                mg.tableWidget_guanli.setItem(rows,columns, QtWidgets.QTableWidgetItem(str(data1[rows][columns])))


def addTable(cursor,id,mg):
    #try:
        cursor.execute("sql")
        #sql= " WHERE aid= '" + str(id) + "' "
        #data = cursor.fetchone()
        data1 = cursor.fetchall()
    #测试
        #print(data)
        #print(data1)
        #print(len(data))
        #print(len(data1))

        row = len(data1)
        #col = len(data)
        mg.tableWidget_guanli.setRowCount(row)
        #print("检查")
        A = UI.lineSymptom.text()

        for rows in range(row):
            for columns in range(4):
                # mg.tablewidgetSymptom.setItem(rows,columns, QtWidgets.QTableWidgetItem(str(data1[rows][columns])))

                UI.tablewidgetSymptom.setItem(rows, 0, QtWidgets.QTableWidgetItem(A))


        basket = { A , 'orange', 'apple', 'pear', 'orange', 'banana'}
