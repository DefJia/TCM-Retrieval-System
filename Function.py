
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
#import MessageBox

def bing_add(cursor,log,A):
    if A.lineEdit_yaofang.text() == "":
        try:
            cursor.execute("INSERT INTO bing (id_bing,name) \
                VALUES ( '"+str(A.lineEdit_id.text())+"' ,'"+str(A.lineEdit_bingming.text())+"')")
            log.commit()
            #massageBox = MessageBox.MessageBox("导入成功")      ?????
            print("导入病成功")
        except Exception as e:
            print(e)
            print("导入错误")

    elif A.lineEdit_bingming.text() == "":
        try:
            cursor.execute("INSERT INTO yaofang (id_bing,yaofang) \
                VALUES ( '"+str(A.lineEdit_id.text())+"' ,'"+str(A.lineEdit_yaofang.text())+"')")
            log.commit()
            #massageBox = MessageBox.MessageBox("导入成功")      ?????
            print("导入药方成功")
        except Exception as e:
            print(e)
            print("导入错误")

    elif A.lineEdit_1.text() == "":
        try:
            cursor.execute("INSERT INTO yaofang (id_bing,yaofang) \
                VALUES ( '"+str(A.lineEdit_id.text())+"' ,'"+str(A.lineEdit_yaofang.text())+"')")
            log.commit()

            cursor.execute("INSERT INTO bing (id_bing,name) \
                            VALUES ( '" + str(A.lineEdit_id.text()) + "' ,'" + str(A.lineEdit_bingming.text()) + "')")
            log.commit()

            print("导入病和药方成功")
        except Exception as e:
            print(e)
            print("导入错误")
    else :
        try:
            cursor.execute("INSERT INTO yaofang (id_bing,yaofang) \
                            VALUES ( '" + str(A.lineEdit_id.text()) + "' ,'" + str(A.lineEdit_yaofang.text()) + "')")
            log.commit()


            cursor.execute("INSERT INTO bing (id_bing,name) \
                                        VALUES ( '" + str(A.lineEdit_id.text()) + "' ,'" + str(
                A.lineEdit_bingming.text()) + "')")
            log.commit()


            cursor.execute("INSERT INTO yao (id_bing,yao) \
                VALUES ( '" + str(A.lineEdit_id.text()) + "' ,'" + str(A.lineEdit_1.text()) + "')")
            log.commit()
            print("导入病，药方，药成功")
        except Exception as e:
            print(e)
            print("导入错误")

def setTable1(cursor,id,mg):
    #try:
        #sql = " WHERE bingzheng= '" + str(id) + "' "
        cursor.execute("SELECT *  FROM bing_bingzheng WHERE bingzheng = '" + str(id) + "'")
        #data = cursor.fetchone()
        data1 = cursor.fetchall()

        row = len(data1)
        #col = len(data)
        print(data1)
        mg.tableWidget_yaofang.setRowCount(row)
        mg.tableWidget_yaofang.setColumnCount(1)

        for rows in range(row):
            print(rows)
            print(str(data1[0][1]))
            mg.tableWidget_yaofang.setItem(0,0, QtWidgets.QTableWidgetItem(str(data1[0][1])))



def settable(cursor,window):
    print("\n")

    try:
        # cursor.execute("SELECT aid ,type, level, time FROM vio WHERE aid= "+str(id)+" ")
        cursor.execute("SELECT * FROM bing WHERE aid= '" + str(id) + "' ")
        print("查询成功")
        nn = cursor.fetchone()
        nnn = cursor.fetchall()

        x =len(nn)
        y =len(nnn)
        print(len(nn))
        print(len(nnn))
        window.tableWidget_yaofang.setColumnCount(x)
        window.tableWidget_yaofang.setRowCount(y)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))

        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            # problems

    except Exception as e:
        print(e)


def chaxun(cursor,id):
    try:
        cursor.execute("SELECT * FROM bing WHERE name = '"+str(id)+"' ")
        data = cursor.fetchone()
        print(data[1])
            #捕捉输入框的输入进行检索？？？
        #data[1] == password:
           # information=self.cursor.fetchall()
            #return information   #????
    except Exception as e:
        print(e)