# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 829)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.bar1 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar1.setMinimumSize(QtCore.QSize(0, 30))
        self.bar1.setProperty("value", 24)
        self.bar1.setObjectName("bar1")
        self.gridLayout.addWidget(self.bar1, 0, 0, 1, 1)
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox1.setObjectName("vbox1")
        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.setObjectName("hbox1")
        self.bt1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1_1.setMinimumSize(QtCore.QSize(0, 37))
        self.bt1_1.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt1_1.setObjectName("bt1_1")
        self.hbox1.addWidget(self.bt1_1)
        self.bt1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1_2.setMinimumSize(QtCore.QSize(0, 37))
        self.bt1_2.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt1_2.setObjectName("bt1_2")
        self.hbox1.addWidget(self.bt1_2)
        self.bt1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1_3.setMinimumSize(QtCore.QSize(0, 37))
        self.bt1_3.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt1_3.setObjectName("bt1_3")
        self.hbox1.addWidget(self.bt1_3)
        self.bt1_4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1_4.setMinimumSize(QtCore.QSize(0, 37))
        self.bt1_4.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt1_4.setObjectName("bt1_4")
        self.hbox1.addWidget(self.bt1_4)
        self.bt1_5 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1_5.setMinimumSize(QtCore.QSize(0, 37))
        self.bt1_5.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt1_5.setObjectName("bt1_5")
        self.hbox1.addWidget(self.bt1_5)
        self.bt1_6 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1_6.setMinimumSize(QtCore.QSize(0, 37))
        self.bt1_6.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt1_6.setObjectName("bt1_6")
        self.hbox1.addWidget(self.bt1_6)
        self.ed1_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(37)
        sizePolicy.setHeightForWidth(self.ed1_1.sizePolicy().hasHeightForWidth())
        self.ed1_1.setSizePolicy(sizePolicy)
        self.ed1_1.setMinimumSize(QtCore.QSize(0, 35))
        self.ed1_1.setToolTip("")
        self.ed1_1.setPlaceholderText("")
        self.ed1_1.setObjectName("ed1_1")
        self.hbox1.addWidget(self.ed1_1)
        self.vbox1.addLayout(self.hbox1)
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.setObjectName("hbox2")
        self.bt2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2_1.setMinimumSize(QtCore.QSize(0, 37))
        self.bt2_1.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt2_1.setIconSize(QtCore.QSize(16, 16))
        self.bt2_1.setObjectName("bt2_1")
        self.hbox2.addWidget(self.bt2_1)
        self.bt2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2_2.setMinimumSize(QtCore.QSize(0, 37))
        self.bt2_2.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt2_2.setObjectName("bt2_2")
        self.hbox2.addWidget(self.bt2_2)
        self.bt2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2_3.setMinimumSize(QtCore.QSize(0, 37))
        self.bt2_3.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt2_3.setObjectName("bt2_3")
        self.hbox2.addWidget(self.bt2_3)
        self.bt2_4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2_4.setMinimumSize(QtCore.QSize(0, 37))
        self.bt2_4.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt2_4.setObjectName("bt2_4")
        self.hbox2.addWidget(self.bt2_4)
        self.bt2_5 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2_5.setMinimumSize(QtCore.QSize(0, 37))
        self.bt2_5.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt2_5.setObjectName("bt2_5")
        self.hbox2.addWidget(self.bt2_5)
        self.bt2_6 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2_6.setMinimumSize(QtCore.QSize(0, 37))
        self.bt2_6.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt2_6.setObjectName("bt2_6")
        self.hbox2.addWidget(self.bt2_6)
        self.ed2_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(37)
        sizePolicy.setHeightForWidth(self.ed2_1.sizePolicy().hasHeightForWidth())
        self.ed2_1.setSizePolicy(sizePolicy)
        self.ed2_1.setMinimumSize(QtCore.QSize(0, 35))
        self.ed2_1.setClearButtonEnabled(False)
        self.ed2_1.setObjectName("ed2_1")
        self.hbox2.addWidget(self.ed2_1)
        self.vbox1.addLayout(self.hbox2)
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox3.setObjectName("hbox3")
        self.bt3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3_1.setMinimumSize(QtCore.QSize(0, 37))
        self.bt3_1.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt3_1.setObjectName("bt3_1")
        self.hbox3.addWidget(self.bt3_1)
        self.bt3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3_2.setMinimumSize(QtCore.QSize(0, 37))
        self.bt3_2.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt3_2.setObjectName("bt3_2")
        self.hbox3.addWidget(self.bt3_2)
        self.bt3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3_3.setMinimumSize(QtCore.QSize(0, 37))
        self.bt3_3.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt3_3.setObjectName("bt3_3")
        self.hbox3.addWidget(self.bt3_3)
        self.bt3_4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3_4.setMinimumSize(QtCore.QSize(0, 37))
        self.bt3_4.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt3_4.setObjectName("bt3_4")
        self.hbox3.addWidget(self.bt3_4)
        self.bt3_5 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3_5.setMinimumSize(QtCore.QSize(0, 37))
        self.bt3_5.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt3_5.setObjectName("bt3_5")
        self.hbox3.addWidget(self.bt3_5)
        self.bt3_6 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3_6.setMinimumSize(QtCore.QSize(0, 37))
        self.bt3_6.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt3_6.setObjectName("bt3_6")
        self.hbox3.addWidget(self.bt3_6)
        self.ed3_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(37)
        sizePolicy.setHeightForWidth(self.ed3_1.sizePolicy().hasHeightForWidth())
        self.ed3_1.setSizePolicy(sizePolicy)
        self.ed3_1.setMinimumSize(QtCore.QSize(0, 35))
        self.ed3_1.setObjectName("ed3_1")
        self.hbox3.addWidget(self.ed3_1)
        self.vbox1.addLayout(self.hbox3)
        self.hbox4 = QtWidgets.QHBoxLayout()
        self.hbox4.setObjectName("hbox4")
        self.bt4_1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4_1.setMinimumSize(QtCore.QSize(0, 37))
        self.bt4_1.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt4_1.setObjectName("bt4_1")
        self.hbox4.addWidget(self.bt4_1)
        self.bt4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4_2.setMinimumSize(QtCore.QSize(0, 37))
        self.bt4_2.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt4_2.setObjectName("bt4_2")
        self.hbox4.addWidget(self.bt4_2)
        self.bt4_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4_3.setMinimumSize(QtCore.QSize(0, 37))
        self.bt4_3.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt4_3.setObjectName("bt4_3")
        self.hbox4.addWidget(self.bt4_3)
        self.bt4_4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4_4.setMinimumSize(QtCore.QSize(0, 37))
        self.bt4_4.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt4_4.setObjectName("bt4_4")
        self.hbox4.addWidget(self.bt4_4)
        self.bt4_5 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4_5.setMinimumSize(QtCore.QSize(0, 37))
        self.bt4_5.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt4_5.setObjectName("bt4_5")
        self.hbox4.addWidget(self.bt4_5)
        self.bt4_6 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4_6.setMinimumSize(QtCore.QSize(0, 37))
        self.bt4_6.setMaximumSize(QtCore.QSize(16777215, 37))
        self.bt4_6.setObjectName("bt4_6")
        self.hbox4.addWidget(self.bt4_6)
        self.ed4_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(37)
        sizePolicy.setHeightForWidth(self.ed4_1.sizePolicy().hasHeightForWidth())
        self.ed4_1.setSizePolicy(sizePolicy)
        self.ed4_1.setMinimumSize(QtCore.QSize(0, 35))
        self.ed4_1.setObjectName("ed4_1")
        self.hbox4.addWidget(self.ed4_1)
        self.vbox1.addLayout(self.hbox4)
        self.tbw1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw1.setObjectName("tbw1")
        self.tbw1.setColumnCount(0)
        self.tbw1.setRowCount(0)
        self.vbox1.addWidget(self.tbw1)
        self.tb1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb1.setObjectName("tb1")
        self.vbox1.addWidget(self.tb1)
        self.vbox1.setStretch(4, 3)
        self.vbox1.setStretch(5, 1)
        self.gridLayout.addLayout(self.vbox1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondddd = QtWidgets.QAction(MainWindow)
        self.actiondddd.setObjectName("actiondddd")
        self.actiondddd_2 = QtWidgets.QAction(MainWindow)
        self.actiondddd_2.setObjectName("actiondddd_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt1_1.setText(_translate("MainWindow", "초기화"))
        self.bt1_2.setText(_translate("MainWindow", "스크린지우기"))
        self.bt1_3.setText(_translate("MainWindow", "로드 서버"))
        self.bt1_4.setText(_translate("MainWindow", "저장 서버"))
        self.bt1_5.setText(_translate("MainWindow", "--"))
        self.bt1_6.setText(_translate("MainWindow", "--"))
        self.bt2_1.setText(_translate("MainWindow", "SPR INFO1"))
        self.bt2_2.setText(_translate("MainWindow", "FILE JOB0"))
        self.bt2_3.setText(_translate("MainWindow", "FILE JOB1"))
        self.bt2_4.setText(_translate("MainWindow", "CONVERT"))
        self.bt2_5.setText(_translate("MainWindow", "CONT ALL"))
        self.bt2_6.setText(_translate("MainWindow", "--"))
        self.ed2_1.setPlaceholderText(_translate("MainWindow", "DI.KyLee.2210301.A01"))
        self.bt3_1.setText(_translate("MainWindow", "RESULT"))
        self.bt3_2.setText(_translate("MainWindow", "LD SPR F"))
        self.bt3_3.setText(_translate("MainWindow", "Save Excel"))
        self.bt3_4.setText(_translate("MainWindow", "LD All"))
        self.bt3_5.setText(_translate("MainWindow", "Save All"))
        self.bt3_6.setText(_translate("MainWindow", "--"))
        self.ed3_1.setPlaceholderText(_translate("MainWindow", "DI.KyLee.2210301.A01"))
        self.bt4_1.setText(_translate("MainWindow", "--"))
        self.bt4_2.setText(_translate("MainWindow", "--"))
        self.bt4_3.setText(_translate("MainWindow", "--"))
        self.bt4_4.setText(_translate("MainWindow", "--"))
        self.bt4_5.setText(_translate("MainWindow", "--"))
        self.bt4_6.setText(_translate("MainWindow", "--"))
        self.actiondddd.setText(_translate("MainWindow", "dddd"))
        self.actiondddd_2.setText(_translate("MainWindow", "dddd"))
