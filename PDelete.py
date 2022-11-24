from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(741, 322)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(290, 80, 281, 81))

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 110, 141, 21))

        self.pushButton = QPushButton(Dialog) # 按姓名删除
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 250, 111, 41))
        self.pushButton.clicked.connect(self.name)

        self.pushButton_2 = QPushButton(Dialog) # 按部门删除
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 250, 111, 41))
        self.pushButton_2.clicked.connect(self.dep)

        self.pushButton_3 = QPushButton(Dialog) # 按项目删除
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(520, 250, 111, 41))
        self.pushButton_3.clicked.connect(self.pro)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u5220\u9664\u7684\u5185\u5bb9", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u804c\u5de5\u59d3\u540d\u5220\u9664", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u90e8\u95e8\u5220\u9664", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u5220\u9664", None))
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

    def name(self):
        name = self.lineEdit.text()
        sql = "delete from emp where name = '%s'" % name
        cursor = self.connect_database()
        cursor.execute(sql)

        self.log("delete", name)

        from delete_success import success_window
        self.window = success_window()
        self.window.show()

    def dep(self):
        dep = self.lineEdit.text()
        sql_pro_id = "select id from dep where name = %s"
        cursor = self.connect_database()
        res = cursor.execute(sql_pro_id, dep)
        dep_id = cursor.fetchall()[0][0]

        sql = "delete from emp where dep_id = %d" % dep_id
        sql2 = "delete from dep where name = '%s'" % dep
        cursor.execute(sql)
        cursor.execute(sql2)

        self.log("delete", dep)

        from delete_success import success_window
        self.window = success_window()
        self.window.show()

    def pro(self):
        pro = self.lineEdit.text()
        sql_pro_id = "select id from project where name = %s"
        cursor = self.connect_database()
        res = cursor.execute(sql_pro_id, pro)
        pro_id = cursor.fetchall()[0][0]

        sql = "delete from emp2pro where pro_id = %d" % pro_id
        cursor.execute(sql)

        self.log("delete", pro)

        from delete_success import success_window
        self.window = success_window()
        self.window.show()

    def log(self, action, name):
        sql = "insert into log(action, msg) values(%s, %s)"
        cursor = self.connect_database()
        cursor.execute(sql, (action, name))

class delete_window(QDialog, Ui_Dialog): # 打开删除的页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)