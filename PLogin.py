from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

class Login(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(647, 450)

        self.lineEdit = QLineEdit(Dialog) # 用户名
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 220, 121, 31))

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(100, 70, 441, 71))

        self.lineEdit_2 = QLineEdit(Dialog) # 密码
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(280, 280, 121, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.Password) # 密码输入星号显示

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 230, 72, 15))

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 290, 72, 15))

        self.pushButton = QPushButton(Dialog) # 登录
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 350, 211, 28))
        self.pushButton.clicked.connect(self.login)

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
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
    # retranslateUi

    def login(self): # 验证登录
        cursor = self.connect_database()

        sql = "select id from user where username = (%s) and password = (%s)"

        username = self.lineEdit.text() # 获取用户名
        # print(username)
        password = self.lineEdit_2.text() # 获取密码

        res = cursor.execute(sql, (username, password))

        # print(cursor.fetchall()[0].get("id"))

        if res == 0: # 账号密码错误

            from login_err import err_window
            self.window = err_window()
            self.window.show()


            # time.sleep(2)
            # self.window.close()
        else:
            id = cursor.fetchall()[0].get("id")

            if id != 1:
                print("登陆成功！！！！！")
                sql = "insert into log(username, action) values(%s, 'login')"
                cursor.execute(sql, (username,))

                from PUserWindow import user_window
                self.window = user_window()
                self.window.show()
            else:
                print("登陆成功！！！！！")
                sql = "insert into log(username, action) values(%s, 'login')"
                cursor.execute(sql, (username,))

                from PAdminWindow import admin_window
                self.window = admin_window()
                self.window.show()

    def connect_database(self): # 连接数据库
        import pymysql
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password=" ",
            database="classDesign",
            charset="utf8",  # 编码千万不要加 -
            autocommit = True
        )  # 连接数据库

        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 产生一个游标对象（cmd 的 光标）,帮助执行命令

        return cursor


class login_window(QDialog, Login): # 打开登录页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)