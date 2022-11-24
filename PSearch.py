from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget


class Ui_Dialog(object):
        def setupUi(self, Dialog):
            if not Dialog.objectName():
                Dialog.setObjectName(u"Dialog")
            Dialog.resize(741, 740)

            self.lineEdit = QLineEdit(Dialog)
            self.lineEdit.setObjectName(u"lineEdit")
            self.lineEdit.setGeometry(QRect(290, 80, 281, 81))

            self.label = QLabel(Dialog)
            self.label.setObjectName(u"label")
            self.label.setGeometry(QRect(130, 110, 141, 21))

            self.pushButton = QPushButton(Dialog) # 职工姓名查询
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setGeometry(QRect(130, 250, 111, 41))
            self.pushButton.clicked.connect(self.name)

            self.pushButton_2 = QPushButton(Dialog) # 部门查询
            self.pushButton_2.setObjectName(u"pushButton_2")
            self.pushButton_2.setGeometry(QRect(330, 250, 111, 41))
            self.pushButton_2.clicked.connect(self.dep)

            self.pushButton_3 = QPushButton(Dialog) # 项目查询
            self.pushButton_3.setObjectName(u"pushButton_3")
            self.pushButton_3.setGeometry(QRect(520, 250, 111, 41))
            self.pushButton_3.clicked.connect(self.project)

            self.tableWidget = QTableWidget(Dialog)
            self.tableWidget.setObjectName(u"tableView")
            self.tableWidget.setGeometry(QRect(130, 320, 511, 371))

            self.retranslateUi(Dialog)

            QMetaObject.connectSlotsByName(Dialog)

        # setupUi

        def retranslateUi(self, Dialog):
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
            self.label.setText(
                QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u67e5\u8be2\u7684\u5185\u5bb9", None))
            self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u804c\u5de5\u59d3\u540d\u67e5\u8be2", None))
            self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u90e8\u95e8\u67e5\u8be2", None))
            self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u67e5\u8be2", None))
        # retranslateUi

        def connect_database(self): # 连接数据库
            import pymysql
            conn = pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="",
                database="classDesign",
                charset="utf8",  # 编码千万不要加 -
                autocommit=True
            )  # 连接数据库

            cursor = conn.cursor()  # 产生一个游标对象（cmd 的 光标）,帮助执行命令

            return cursor

        def name(self):
            cursor = self.connect_database()

            name = self.lineEdit.text()
            # print(name)

            sql = """
            SELECT
            emp.`name`,
            emp_detail.addr,
            emp_detail.email,
            emp_detail.time,
            dep.`name`,
            dep.des
            FROM
            emp
            INNER JOIN emp_detail ON emp.detail_id = emp_detail.id
            INNER JOIN dep ON emp.dep_id = dep.id
            WHERE
            emp.name = %s
            """

            res = cursor.execute(sql, (name,))

            if res != 0:
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

                self.log("query", name)
            else:
                self.log("query", name)
                # print("没有该条信息")
                from search_err import err_window
                self.window = err_window()
                self.window.show()

        def log(self, action, name):
            sql = "insert into log(action, msg) values(%s, %s)"
            cursor = self.connect_database()
            cursor.execute(sql, (action, name))

        def dep(self):
            cursor = self.connect_database()

            name = self.lineEdit.text()

            sql = """
            SELECT
            dep.`name`,
            emp.`name`,
            emp_detail.addr,
            emp_detail.email,
            emp_detail.time
            FROM
            dep
            INNER JOIN emp ON emp.dep_id = dep.id
            INNER JOIN emp_detail ON emp.detail_id = emp_detail.id
            WHERE
            dep.name = %s
            """

            res = cursor.execute(sql, (name,))

            if res != 0:
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

                self.log("query", name)
            else:
                self.log("query", name)
                # print("没有该条信息")
                from search_err import err_window
                self.window = err_window()
                self.window.show()

        def project(self):
            cursor = self.connect_database()

            name = self.lineEdit.text()

            sql = """
            SELECT
            project.`name`,
            emp.`name`,
            emp_detail.addr,
            emp_detail.email,
            emp_detail.time,
            dep.`name`,
            dep.des
            FROM
            project
            INNER JOIN emp2pro ON emp2pro.pro_id = project.id
            INNER JOIN emp ON emp2pro.emp_id = emp.id
            INNER JOIN emp_detail ON emp.detail_id = emp_detail.id
            INNER JOIN dep ON emp.dep_id = dep.id
            WHERE
            project.name = %s
            """

            res = cursor.execute(sql, (name,))

            if res != 0:
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

                self.log("query", name)
            else:
                self.log("query", name)
                # print("没有该条信息")
                from search_err import err_window
                self.window = err_window()
                self.window.show()

class search_window(QDialog, Ui_Dialog): # 打开查询的页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)