# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.View = QtWidgets.QWidget()
        self.View.setObjectName("View")
        self.media_windows = QtWidgets.QLabel(self.View)
        self.media_windows.setGeometry(QtCore.QRect(340, 50, 720, 540))
        self.media_windows.setText("")
        self.media_windows.setObjectName("media_windows")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.View)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 630, 541, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_start.setObjectName("Button_start")
        self.horizontalLayout.addWidget(self.Button_start)
        self.Button_pause = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_pause.setObjectName("Button_pause")
        self.horizontalLayout.addWidget(self.Button_pause)
        self.Button_load = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_load.setObjectName("Button_load")
        self.horizontalLayout.addWidget(self.Button_load)
        self.massage = QtWidgets.QLabel(self.View)
        self.massage.setGeometry(QtCore.QRect(20, 620, 281, 51))
        self.massage.setText("")
        self.massage.setObjectName("massage")
        self.files_list = QtWidgets.QListWidget(self.View)
        self.files_list.setGeometry(QtCore.QRect(10, 50, 241, 481))
        self.files_list.setObjectName("files_list")
        self.label = QtWidgets.QLabel(self.View)
        self.label.setGeometry(QtCore.QRect(340, 20, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.View)
        self.label_2.setGeometry(QtCore.QRect(20, 580, 121, 21))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.View, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.media_windows2 = QtWidgets.QLabel(self.tab_2)
        self.media_windows2.setText("")
        self.media_windows2.setObjectName("media_windows2")
        self.verticalLayout.addWidget(self.media_windows2)
        self.massage2 = QtWidgets.QLabel(self.tab_2)
        self.massage2.setText("")
        self.massage2.setObjectName("massage2")
        self.verticalLayout.addWidget(self.massage2)
        self.Button_receive = QtWidgets.QPushButton(self.tab_2)
        self.Button_receive.setObjectName("Button_receive")
        self.verticalLayout.addWidget(self.Button_receive)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.info_tbview = QtWidgets.QTableView(self.tab)
        self.info_tbview.setObjectName("info_tbview")
        self.horizontalLayout_2.addWidget(self.info_tbview)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_start.setText(_translate("MainWindow", "start"))
        self.Button_pause.setText(_translate("MainWindow", "pause"))
        self.Button_load.setText(_translate("MainWindow", "Load_local_data"))
        self.label.setText(_translate("MainWindow", "View"))
        self.label_2.setText(_translate("MainWindow", "massage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.View), _translate("MainWindow", "loacl"))
        self.label_4.setText(_translate("MainWindow", "Real time video streaming"))
        self.Button_receive.setText(_translate("MainWindow", "receive in real time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "real time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "data"))
