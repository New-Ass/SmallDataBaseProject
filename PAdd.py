from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(880, 459)

        self.lineEdit = QLineEdit(Dialog) # 姓名
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(220, 80, 211, 41))

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 90, 141, 21))

        self.lineEdit_2 = QLineEdit(Dialog) # add
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 150, 211, 41))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 160, 141, 21))

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 230, 141, 21))
        self.lineEdit_3 = QLineEdit(Dialog) # email
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(220, 220, 211, 41))

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 120, 141, 21))
        self.lineEdit_4 = QLineEdit(Dialog) # 部门姓名
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(600, 110, 211, 41))

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(490, 190, 141, 21))
        self.lineEdit_5 = QLineEdit(Dialog) # 项目
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(600, 180, 211, 41))

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 330, 171, 61))
        self.pushButton.clicked.connect(self.submit)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u804c\u5458\u59d3\u540d", None))
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u804c\u5458\u5730\u5740", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u804c\u5458\u90ae\u7bb1", None))
        self.lineEdit_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6240\u5c5e\u90e8\u95e8", None))
        self.lineEdit_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u52a0\u5165\u9879\u76ee", None))
        self.lineEdit_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u6570\u636e", None))
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

    def submit(self):
        emp_name = self.lineEdit.text()

        emp_add = self.lineEdit_2.text()
        emp_email = self.lineEdit_3.text()

        # 部门
        dep = self.lineEdit_4.text()
        dep_id = None

        # 项目
        pro = self.lineEdit_5.text()
        pro_id = None

        # print(emp_name,emp_add,emp_email, dep, pro)

        cursor = self.connect_database()

        # 判断部门是否存在，如果不存在，添加并且返回 部门的 id 值
        if len(dep) != 0:
            sql_dep = "select id from dep where name = %s"
            res = cursor.execute(sql_dep, dep)

            if res == 0: # 不存在该部门
                sql_insert_dep = "insert into dep(name) values ('%s')" % (dep)
                cursor.execute(sql_insert_dep)

            cursor.execute(sql_dep, dep)
            dep_id = cursor.fetchall()[0][0]
            # print(dep_id)

            self.log("add", dep)

        # 判断 项目 是否存在，如果不存在，添加并且返回 项目的 id 值
        if len(pro) != 0:
            sql_pro = "select id from project where name = %s"
            res = cursor.execute(sql_pro, pro)

            if res == 0:  # 不存在该项目
                sql_insert_pro = "insert into project(name) values ('%s')" % (pro)
                cursor.execute(sql_insert_pro)

            cursor.execute(sql_pro, pro)
            pro_id = cursor.fetchall()[0][0]
            # print(pro_id)

            self.log("add", pro)

        if len(emp_name) != 0:
            sql_detail = "insert into emp_detail(addr, email) values('%s', '%s')" % (emp_add, emp_email)
            cursor.execute(sql_detail)

            sql_detail_id = "select id from emp_detail where addr = '%s'" % emp_add
            cursor.execute(sql_detail_id)
            detail_id = cursor.fetchall()[0][0]
            # print(detail_id)

            sql_emp = "insert into emp(name, dep_id, detail_id) values('%s', %d, %d)" % (emp_name, dep_id, detail_id)
            # print(sql_emp)
            cursor.execute(sql_emp)

            if pro_id is not None:
                sql_emp_id = "select id from emp where name = '%s'" % emp_name
                cursor.execute(sql_emp_id)
                emp_id = cursor.fetchall()[0][0]
                # print(emp_id, pro_id)
                # print(emp_id)

                sql_emp2project = "insert into emp2pro(emp_id, pro_id) values(%d, %d)" % (emp_id, pro_id)
                # print(sql_emp2project)
                cursor.execute(sql_emp2project)

            self.log("add", emp_name)

        from add_success import success_window
        self.window = success_window()
        self.window.show()

    def log(self, action, name):
        sql = "insert into log(action, msg) values(%s, %s)"
        cursor = self.connect_database()
        cursor.execute(sql, (action, name))

class add_window(QDialog, Ui_Dialog): # 添加数据的页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)