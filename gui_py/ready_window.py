# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ready_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReadyWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 460)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ready_page_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.ready_page_back_pushButton.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.ready_page_back_pushButton.setObjectName("ready_page_back_pushButton")
        self.horizontalLayout.addWidget(self.ready_page_back_pushButton)
        self.ready_page_start_pushButton = QtWidgets.QPushButton(self.frame)
        self.ready_page_start_pushButton.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.ready_page_start_pushButton.setObjectName("ready_page_start_pushButton")
        self.horizontalLayout.addWidget(self.ready_page_start_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ready_img1_label = QtWidgets.QLabel(self.frame_3)
        self.ready_img1_label.setText("")
        self.ready_img1_label.setPixmap(QtGui.QPixmap(":/img1/learn_verbs.png"))
        self.ready_img1_label.setScaledContents(True)
        self.ready_img1_label.setObjectName("ready_img1_label")
        self.verticalLayout.addWidget(self.ready_img1_label)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ready_img2_label = QtWidgets.QLabel(self.frame_4)
        self.ready_img2_label.setText("")
        self.ready_img2_label.setPixmap(QtGui.QPixmap(":/img2/get_ready.png"))
        self.ready_img2_label.setScaledContents(True)
        self.ready_img2_label.setObjectName("ready_img2_label")
        self.verticalLayout_2.addWidget(self.ready_img2_label)
        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Verbs"))
        self.ready_page_back_pushButton.setText(_translate("MainWindow", "Back"))
        self.ready_page_start_pushButton.setText(_translate("MainWindow", "Start"))
import gui_py.ready_win


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ReadyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
