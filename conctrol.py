from a_Main import M
from b_Add import A
import a_way
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
#数据库开启————————————————————————————————
import pymysql
try:
    log = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='ok120110', db='medical')
    print("数据库连接成功")
except Exception as e:
    print(e)
    print("数据库连接失败")
cursor = log.cursor()

#__________________________________

if __name__=="__main__":
    app=QApplication(sys.argv)
    M = M()
    A = A()

#显示——————————————————————
    M.show()    # 显示log


#操作——————————————————————
   # M.pushButton_bingzheng.clicked.connect(lambda: a_way.chaxun(cursor, mw.lineEdit.text(), Mw2))
    M.pushButton_out.clicked.connect(lambda: M.hide())
    A.pushButton_out.clicked.connect(lambda: A.hide())
    M.pushButton_daoru.clicked.connect(lambda: A.show())
    A.pushButton_tianjia.clicked.connect(lambda: a_way.bing_add(cursor,log,A))
    M.pushButton_bingzheng.clicked.connect(lambda: a_way.chaxun(cursor,M.lineEdit_bingzheng.text()))

    sys.exit(app.exec_())
    close
