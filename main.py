import sys
import PyQt5
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from enum import Enum
from mainUi import Ui_MainWindow

import process as ps
from Class_Data.Command import Cmd

DEBUG_ON = 1
DEBUG_OFF = 0

debug = DEBUG_OFF
D_main_process = DEBUG_OFF

class QPushButton(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)


class Exam(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.defineItem()
        self.Decolation()
        self.initUI()
        self.UIconnectFC()
        self.show()
    
    def defineItem(self):
        # 추가 할것이 있다면 이곳에서 만들기 
        self.rbt0 = QRadioButton(self)
        self.rbt1 = QRadioButton(self)
        self.rbt2 = QRadioButton(self)
        self.rbt3 = QRadioButton(self)
        self.rbt4 = QRadioButton(self)
        
        self.rbt0.setText('NONE')
        self.rbt1.setText('파트너')
        self.rbt2.setText('장비사')
        self.rbt3.setText('SPR_NO')
        self.rbt4.setText('LGES')

        self.hbox1.addWidget(self.rbt0)
        self.hbox1.addWidget(self.rbt1)
        self.hbox1.addWidget(self.rbt2)
        self.hbox1.addWidget(self.rbt3)
        self.hbox1.addWidget(self.rbt4)

        self.ed2_2 = QLineEdit()
        self.ed2_3 = QLineEdit()
        self.ed2_4 = QLineEdit()
        self.ed2_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ed2_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ed2_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.ed2_1.setPlaceholderText('파트너')
        self.ed2_2.setPlaceholderText('장비사')
        self.ed2_3.setPlaceholderText('LGES')
        self.ed2_4.setPlaceholderText('공정')

        self.hbox2.addWidget(self.ed2_2)
        self.hbox2.addWidget(self.ed2_3)
        self.hbox2.addWidget(self.ed2_4)

        print('define')
        
    def Decolation(self):
        self.bt1_1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt1_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt1_3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt1_4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt1_5.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt1_6.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        
        self.bt2_1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt2_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt2_3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt2_4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt2_5.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt2_6.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        
        self.bt3_1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt3_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt3_3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt3_4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt3_5.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.bt3_6.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        

        self.tb1.setWordWrapMode(QTextOption.NoWrap)
        self.tb1.setStyleSheet('color: blue')
        self.tb1.setFont(QFont("Monospace"))
        self.tb1.setAlignment(Qt.AlignLeft)
        
    
    def initUI(self):
        self.bt1_5.setText("로그 지우기")
        self.bt1_6.setText("인풋 지우기")
        self.setWindowTitle('SPR 관리 앱')
        self.bar1.setOrientation(Qt.Horizontal)
        self.bar1.setRange(0,30)
        self.bar1_timer = QTimer()
        self.bar1_time = QTime(0,0,0)



    def UIconnectFC(self):
        self.bt1_1.clicked.connect(lambda x: ps.ui_process1(self,Cmd.INIT))
        self.bt1_2.clicked.connect(lambda x: ps.ui_process1(self,Cmd.SCREEN_CLR))
        self.bt1_3.clicked.connect(lambda x: ps.ui_process1(self,Cmd.LOAD_SERVER))
        self.bt1_4.clicked.connect(lambda x: ps.ui_process1(self,Cmd.SAVE_SERVER))
        self.bt1_5.clicked.connect(lambda x: ps.ui_process1(self,Cmd.LOG_CLR))
        self.bt1_6.clicked.connect(lambda x: ps.ui_process1(self,Cmd.INPUT_CLR))

        self.bt2_1.clicked.connect(lambda x: ps.ui_process2(self,Cmd.SPR_INFO_1))
        self.bt2_2.clicked.connect(lambda x: ps.ui_process2(self,Cmd.FILE_JOB_0))
        self.bt2_3.clicked.connect(lambda x: ps.ui_process2(self,Cmd.FILE_JOB_1))
        self.bt2_4.clicked.connect(lambda x: ps.ui_process2(self,Cmd.CONVERT))
        self.bt2_5.clicked.connect(lambda x: ps.ui_process2(self,Cmd.CONVERT_ALL))
        
        self.bt3_1.clicked.connect(lambda x: ps.ui_process3(self,Cmd.RESULT_LOAD))
        self.bt3_2.clicked.connect(lambda x: ps.ui_process3(self,Cmd.LOAD_SPR_FILE))
        self.bt3_3.clicked.connect(lambda x: ps.ui_process3(self,Cmd.SAVE_SPR_EXCEL))
        self.bt3_4.clicked.connect(lambda x: ps.ui_process3(self,Cmd.LOAD_ALL))
        self.bt3_5.clicked.connect(lambda x: ps.ui_process3(self,Cmd.SAVE_ALL))
        


app = QApplication([])
ex = Exam()
sys.exit(app.exec_())
