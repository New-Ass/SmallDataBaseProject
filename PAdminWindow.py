from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(735, 581)

        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 30, 521, 501))
        self.load()

        self.pushButton_4 = QPushButton(Dialog) # 删除
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(630, 410, 93, 28))
        self.pushButton_4.clicked.connect(self.delete)


        self.pushButton_5 = QPushButton(Dialog) # 添加
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(630, 360, 93, 28))
        self.pushButton_5.clicked.connect(self.add)


        self.pushButton_6 = QPushButton(Dialog) # 查询
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(630, 310, 93, 28))
        self.pushButton_6.clicked.connect(self.search)

        self.pushButton_7 = QPushButton(Dialog) # 查看日志
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(630, 460, 93, 28))
        self.pushButton_7.clicked.connect(self.log)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664\u4fe1\u606f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u4fe1\u606f", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u4fe1\u606f", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b\u65e5\u5fd7", None))
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

        sql = """
        SELECT
        emp.`name`,
        dep.`name`,
        dep.des,
        emp_detail.addr,
        emp_detail.email,
        emp_detail.time,
        project.`name`
        FROM
        emp
        INNER JOIN dep ON emp.dep_id = dep.id
        INNER JOIN emp2pro ON emp2pro.emp_id = emp.id
        INNER JOIN emp_detail ON emp.detail_id = emp_detail.id
        INNER JOIN project ON emp2pro.pro_id = project.id
        """

        cursor.execute(sql)
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

    def log(self):
        from PLogWindow import log_window
        self.window = log_window()
        self.window.show()

    def search(self):
        from PSearch import search_window
        self.window = search_window()
        self.window.show()

    def add(self):
        from PAdd import add_window
        self.window = add_window()
        self.window.show()

    def delete(self):
        from PDelete import delete_window
        self.window = delete_window()
        self.window.show()

class admin_window(QDialog, Ui_Dialog): # 打开普通用户登录后的页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)