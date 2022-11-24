from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(741, 561)

        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 30, 571, 501))
        self.load()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

    def connect_database(self): # 连接数据库
        import pymysql
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password=" ",
            database="classDesign",
            charset="utf8",  # 编码千万不要加 -
            autocommit=True
        )  # 连接数据库

        cursor = conn.cursor()  # 产生一个游标对象（cmd 的 光标）,帮助执行命令

        return cursor

    def load(self):
        cursor = self.connect_database()

        cursor.execute('select * from log')
        rows = cursor.fetchall()
        row = cursor.rowcount  # 取得记录个数，用于设置表格的行数
        # print(rows[0].keys())

        col = len(rows[0])  # 取得字段数，用于设置表格的列数

        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)

        # print(rows)

        for i in range(row):
            for j in range(col):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                # data = data.setGeometry(QRect(70, 30, 661, 501))
                self.tableWidget.setItem(i, j, data)

class log_window(QDialog, Ui_Dialog):  # 打开普通用户登录后的页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)

