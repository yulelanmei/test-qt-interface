# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\VScode Python\Human_Remover\the_olds_defender\frontend\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.media_windows = QtWidgets.QLabel(self.centralwidget)
        self.media_windows.setGeometry(QtCore.QRect(0, -1, 540, 361))
        self.media_windows.setText("")
        self.media_windows.setObjectName("media_windows")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 440, 541, 151))
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
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(-10, 360, 551, 81))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.files_list = QtWidgets.QListWidget(self.centralwidget)
        self.files_list.setGeometry(QtCore.QRect(540, 50, 491, 311))
        self.files_list.setObjectName("files_list")
        self.search_line = QtWidgets.QLineEdit(self.centralwidget)
        self.search_line.setGeometry(QtCore.QRect(540, 10, 491, 31))
        self.search_line.setObjectName("search_line")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1040, 50, 31, 311))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.massage = QtWidgets.QLabel(self.centralwidget)
        self.massage.setGeometry(QtCore.QRect(0, 620, 541, 61))
        self.massage.setText("")
        self.massage.setObjectName("massage")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_start.setText(_translate("MainWindow", "start"))
        self.Button_pause.setText(_translate("MainWindow", "pause"))
        self.Button_load.setText(_translate("MainWindow", "Load"))
