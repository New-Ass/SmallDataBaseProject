from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

from FirstWindow import Ui_Dialog

class Window(QDialog,Ui_Dialog): # 实例化初始界面
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setup_ui(self):
        pass

app = QApplication([])

window = Window()
window.show()
app.exec_()