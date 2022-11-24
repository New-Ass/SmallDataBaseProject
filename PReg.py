from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(647, 450)

        self.username = QLineEdit(Dialog)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(280, 220, 121, 31))

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(100, 70, 441, 71))

        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(280, 280, 121, 31))
        self.password.setEchoMode(QLineEdit.Password)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 230, 72, 15))

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 290, 72, 15))

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 350, 211, 28))
        self.pushButton.clicked.connect(self.reg)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">\u6b22\u8fce\u4f7f\u7528 XXX \u7cfb\u7edf</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
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

        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 产生一个游标对象（cmd 的 光标）,帮助执行命令

        return cursor

    def reg(self):
        username = self.username.text()
        password = self.password.text()
        # print(username, password)

        cursor = self.connect_database()

        sql = "select id from user where username = '%s' " % username

        res = cursor.execute(sql)

        if res != 0:
            from reg_err import err_window
            self.window = err_window()
            self.window.show()
        else:
            sql = "insert into user(username, password) values(%s, %s)"
            cursor.execute(sql, (username, password))

            print("注册成功！！！！")
            from PLogin import login_window
            self.window = login_window()
            self.window.show()

class reg_window(QDialog, Ui_Dialog): # 打开注册页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)