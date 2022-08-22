import sys
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)


class Exam(QMainWindow, Ui_MainWindow):
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
        self.ed1_2 = QLineEdit()
        self.ed1_3 = QLineEdit()
        self.ed1_2.setPlaceholderText("2022-04")
        self.ed1_3.setPlaceholderText("2022-06")
        self.ed1_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ed1_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.rbt0 = QRadioButton(self)
        self.rbt1 = QRadioButton(self)
        self.rbt2 = QRadioButton(self)
        self.rbt3 = QRadioButton(self)
        self.rbt4 = QRadioButton(self)
        self.rbt5 = QRadioButton(self)

        self.rbt0.setText("NONE")
        self.rbt1.setText("파트너")
        self.rbt2.setText("장비사")
        self.rbt3.setText("SPR_NO")
        self.rbt4.setText("LGES")
        self.rbt5.setText("날짜")

        self.hbox1.addWidget(self.ed1_2)
        self.hbox1.addWidget(self.ed1_3)

        self.hbox1.addWidget(self.rbt0)
        self.hbox1.addWidget(self.rbt1)
        self.hbox1.addWidget(self.rbt2)
        self.hbox1.addWidget(self.rbt3)
        self.hbox1.addWidget(self.rbt4)
        self.hbox1.addWidget(self.rbt5)

        self.ed2_2 = QLineEdit()
        self.ed2_3 = QLineEdit()
        self.ed2_4 = QLineEdit()
        self.ed2_5 = QLineEdit()
        self.ed2_6 = QLineEdit()
        self.ed2_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ed2_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ed2_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ed2_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ed2_6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.ed2_1.setPlaceholderText("파트너")
        self.ed2_2.setPlaceholderText("장비사")
        self.ed2_3.setPlaceholderText("LGES")
        self.ed2_4.setPlaceholderText("공정")
        self.ed2_5.setPlaceholderText("2022-06")
        self.ed2_6.setPlaceholderText("2022-07")

        self.ed3_1.setPlaceholderText("6ES7135-6HD00-0BA1")

        self.hbox2.addWidget(self.ed2_2)
        self.hbox2.addWidget(self.ed2_3)
        self.hbox2.addWidget(self.ed2_4)
        self.hbox2.addWidget(self.ed2_5)
        self.hbox2.addWidget(self.ed2_6)

        print("define")

    def Decolation(self):
        self.bt1_1.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt1_2.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt1_3.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt1_4.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt1_5.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt1_6.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )

        self.bt2_1.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt2_2.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt2_3.setStyleSheet(
            "QPushButton {background-color: #FFC0CB; color: black;}"
        )
        self.bt2_4.setStyleSheet(
            "QPushButton {background-color: #FFC0CB; color: black;}"
        )
        self.bt2_5.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt2_6.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )

        self.bt3_1.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt3_2.setStyleSheet(
            "QPushButton {background-color: #B0BEC5; color: black;}"
        )
        self.bt3_3.setStyleSheet(
            "QPushButton {background-color: #FFC0CB; color: black;}"
        )
        self.bt3_4.setStyleSheet(
            "QPushButton {background-color: #FFC0CB; color: black;}"
        )
        self.bt3_5.setStyleSheet(
            "QPushButton {background-color: #FFC0CB; color: black;}"
        )
        self.bt3_6.setStyleSheet(
            "QPushButton {background-color: #FFC0CB; color: black;}"
        )

        self.tb1.setWordWrapMode(QTextOption.NoWrap)
        self.tb1.setStyleSheet("color: blue")
        self.tb1.setFont(QFont("Monospace"))
        self.tb1.setAlignment(Qt.AlignLeft)

        # setVisible(False)

    def initUI(self):
        self.bt1_1.setText("INIT E.SPR")
        self.bt1_2.setText("CLR SCREEN")
        self.bt1_3.setText("LD E.SPR DB\nTO DB")
        self.bt1_4.setText("SV E.SPR DB\nTO DB")
        self.bt1_5.setText("CLR LOG")
        self.bt1_6.setText("CLR INPUT\nDATA")

        self.bt1_1.setToolTip("SPR_SUM 엑셀을 생성.")
        self.bt1_2.setToolTip("TABLE 내용 삭제.")
        self.bt1_3.setToolTip("SQL DB 에저장된 SPR 정보를 테이블에 표기.")
        self.bt1_4.setToolTip("SPR 엑셀정보를 SQL DB 에 저장.")
        self.bt1_5.setToolTip("로그 삭제.")
        self.bt1_6.setToolTip("인풋 내용을 삭제")

        self.bt2_1.setText("LD E.INFO\nTO TB")
        self.bt2_2.setText("SV TB TO\nE.F.INFO")
        self.bt2_3.setText("-")
        self.bt2_4.setText("-")
        self.bt2_5.setText("LD E.SPR\nTO TB")
        self.bt2_6.setText("SV TB\nE.F.SPR")

        self.bt2_1.setToolTip("SPR_INFO 엑셀을 테이블로 로딩.")
        self.bt2_2.setToolTip("필터된 SPR_INFO 를 저장.")
        self.bt2_3.setToolTip("")
        self.bt2_4.setToolTip("")
        self.bt2_5.setToolTip("SPR_SUM 엑셀을 테이블로 로딩")
        self.bt2_6.setToolTip("테이블데이터를 필터된 SPR_SUM 엑셀에 저장")

        self.bt3_1.setText("CT E.RAW\nTO TB")
        self.bt3_2.setText("SV TB TO\nE.SPR")
        self.bt3_3.setText("-")
        self.bt3_4.setText("-")
        self.bt3_5.setText("LD E.SPR\nLLP TO TB")
        self.bt3_6.setText("SV TB TO\nE.LLP")

        self.bt3_1.setToolTip("RAW SPR 엑셀을 테이블로 로딩.")
        self.bt3_2.setToolTip("로딩된 SPR DF와 E.SPR DF를 비교해서 합쳐서 엑셀에 저장")
        self.bt3_3.setToolTip("")
        self.bt3_4.setToolTip("")
        self.bt3_5.setToolTip("SPR_SUM 엑셀에 MLFB 를 가지고 LLP 정보 테이블로 로딩")
        self.bt3_6.setToolTip("테이블데이터를 LLP 엑셀에 저장")

        self.setWindowTitle("SPR 관리 앱")
        self.bar1.setOrientation(Qt.Horizontal)
        self.bar1.setRange(0, 30)
        self.bar1_timer = QTimer()
        self.bar1_time = QTime(0, 0, 0)

    def UIconnectFC(self):
        self.bt1_1.clicked.connect(lambda x: ps.ui_process1(self, Cmd.INIT))
        self.bt1_2.clicked.connect(lambda x: ps.ui_process1(self, Cmd.SCREEN_CLR))
        self.bt1_3.clicked.connect(lambda x: ps.ui_process1(self, Cmd.LOAD_SERVER))
        self.bt1_4.clicked.connect(lambda x: ps.ui_process1(self, Cmd.SAVE_SERVER))
        self.bt1_5.clicked.connect(lambda x: ps.ui_process1(self, Cmd.LOG_CLR))
        self.bt1_6.clicked.connect(lambda x: ps.ui_process1(self, Cmd.INPUT_CLR))

        self.bt2_1.clicked.connect(lambda x: ps.ui_process2(self, Cmd.LOAD_SPR_INFO))
        self.bt2_2.clicked.connect(
            lambda x: ps.ui_process2(self, Cmd.SAVE_F_SPR_INFO_EXCEL)
        )
        # self.bt2_3.clicked.connect(lambda x: ps.ui_process2(self,Cmd.FILE_JOB_1))
        # self.bt2_4.clicked.connect(lambda x: ps.ui_process2(self,Cmd.CONVERT))
        self.bt2_5.clicked.connect(lambda x: ps.ui_process2(self, Cmd.LOAD_SPR_SUM))
        self.bt2_6.clicked.connect(
            lambda x: ps.ui_process2(self, Cmd.SAVE_F_SPR_SUM_EXCEL)
        )

        self.bt3_1.clicked.connect(lambda x: ps.ui_process3(self, Cmd.CONVERT_ERAW_SPR))
        self.bt3_2.clicked.connect(
            lambda x: ps.ui_process3(self, Cmd.SAVE_SUM_SPR_EXCLE)
        )
        # self.bt3_3.clicked.connect(lambda x: ps.ui_process3(self,Cmd.SAVE_SPR_EXCEL))
        # self.bt3_4.clicked.connect(lambda x: ps.ui_process3(self,Cmd.LOAD_ALL))
        self.bt3_5.clicked.connect(lambda x: ps.ui_process3(self, Cmd.LOAD_SUM_SPR_LLP))
        self.bt3_6.clicked.connect(lambda x: ps.ui_process3(self, Cmd.SAVE_LLP_EXCEL))


app = QApplication([])
ex = Exam()
sys.exit(app.exec_())
