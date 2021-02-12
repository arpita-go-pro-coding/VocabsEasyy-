# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verb_target_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VerbTargetWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 550)
        MainWindow.setMinimumSize(QtCore.QSize(930, 550))
        MainWindow.setMaximumSize(QtCore.QSize(950, 800))
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(930, 0))
        self.frame.setMaximumSize(QtCore.QSize(950, 800))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verb_target_img_label = QtWidgets.QLabel(self.frame_2)
        self.verb_target_img_label.setText("")
        self.verb_target_img_label.setPixmap(QtGui.QPixmap(":/set_target/set_target.jpg"))
        self.verb_target_img_label.setScaledContents(True)
        self.verb_target_img_label.setObjectName("verb_target_img_label")
        self.gridLayout.addWidget(self.verb_target_img_label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verb_target_heading_label = QtWidgets.QLabel(self.frame_3)
        self.verb_target_heading_label.setGeometry(QtCore.QRect(10, 10, 430, 58))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.verb_target_heading_label.setFont(font)
        self.verb_target_heading_label.setWordWrap(True)
        self.verb_target_heading_label.setObjectName("verb_target_heading_label")
        self.verb_target_no_lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.verb_target_no_lineEdit.setGeometry(QtCore.QRect(10, 100, 431, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.verb_target_no_lineEdit.setFont(font)
        self.verb_target_no_lineEdit.setObjectName("verb_target_no_lineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 170, 431, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verb_target_go_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.verb_target_go_pushButton.setFont(font)
        self.verb_target_go_pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.verb_target_go_pushButton.setObjectName("verb_target_go_pushButton")
        self.gridLayout_2.addWidget(self.verb_target_go_pushButton, 2, 0, 1, 1)
        self.verb_target_back_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.verb_target_back_pushButton.setFont(font)
        self.verb_target_back_pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.verb_target_back_pushButton.setObjectName("verb_target_back_pushButton")
        self.gridLayout_2.addWidget(self.verb_target_back_pushButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.verb_target_no_lineEdit, self.verb_target_back_pushButton)
        MainWindow.setTabOrder(self.verb_target_back_pushButton, self.verb_target_go_pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Verbs"))
        self.verb_target_heading_label.setText(_translate("MainWindow", "How many Verbs would you like to learn now?"))
        self.verb_target_no_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter no. of verbs to learn"))
        self.verb_target_go_pushButton.setText(_translate("MainWindow", "Let\'s Go!"))
        self.verb_target_back_pushButton.setText(_translate("MainWindow", "Back"))
import gui_py.verb_target


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_VerbTargetWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
