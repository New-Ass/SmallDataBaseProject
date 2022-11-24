from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(646, 453)

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(120, 160, 441, 71))

        self.login = QPushButton(Dialog) # 登录按钮
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(160, 320, 91, 41))
        self.login.clicked.connect(self.user_login)

        self.reg = QPushButton(Dialog) # 注册按钮
        self.reg.setObjectName(u"reg")
        self.reg.setGeometry(QRect(400, 320, 91, 41))
        self.reg.clicked.connect(self.user_reg)

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
        self.login.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.reg.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
    # retranslateUi

    def user_login(self): # 用户登录页面显示
        from PLogin import login_window
        self.window = login_window()
        self.window.show()

    def user_reg(self): # 用户注册页面展示
        from PReg import reg_window
        self.window = reg_window()
        self.window.show()