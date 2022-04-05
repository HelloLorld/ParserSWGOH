# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import threading

import res_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal
import time


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent=parent)
        self.setPlaceholderText('000-000-000')

    def focusInEvent(self, event):
        self.setInputMask('999-999-999')

class MyThread(QThread):
    def __init__(self, sleep):
        super().__init__()
        self.sleepBar = sleep
        self.exit_event = threading.Event()
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 1000:
            cnt+=1
            time.sleep(self.sleepBar)
            self.change_value.emit(cnt)
            if self.exit_event.is_set():
                break

    def stop(self):
        self.exit_event.set()

class PopupException(QDialog):
    def __init__(self, labelText, id=None):
        super().__init__()
        self.text = labelText
        self.id = id
    def setupUi(self, Form):
        Form.setObjectName("Popup")
        Form.resize(430, 140)
        Form.setStyleSheet("background-color: rgb(192, 222, 229);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 105, 30))
        self.pushButton.setStyleSheet("background: autoFill;\n"
"background-color: rgb(1, 74, 88);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 391, 41))
        self.label.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background: transparent;\n"
"color: rgb(1, 74, 88);")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Popup"))
        self.pushButton.setText(_translate("Form", "OK"))
        if self.id:
            self.label.setText(_translate("Form", self.text + self.id))
        else:
            self.label.setText(_translate("Form", self.text))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton.clicked.connect(self.close)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 500)
        MainWindow.setMinimumSize(QtCore.QSize(685, 500))
        MainWindow.setMaximumSize(QtCore.QSize(685, 500))
        MainWindow.setStyleSheet(
            "background-image: url(:/resources/image/background.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 295, 130, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: autoFill;\n"
                                      "background-color: rgb(1, 74, 88);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 75 12pt \"Arial\";\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 23px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(515, 295, 130, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 23px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(199, 423, 444, 15))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    border-style: solid;\n"
                                       "    border-width: 1px;\n"
                                       "    border-radius: 23px;\n"
                                       "    background:transparent;\n"
                                       "    background-color: rgb(203, 228, 233);\n"
                                       "    text-align: center;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk  {\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: rgb(0, 105, 109);\n"
                                       "}\n"
                                       "")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setInputMask('000-000-000')
        # self.lineEdit = LineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 111, 290, 30))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setStyleSheet("border-style: outset;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 8px;\n"
                                    "border-color: rgb(0, 0, 0);\n"
                                    "background: transparent;\n"
                                    "font-size: 20px")
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setInputMask('999-999-999')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(245, 115, 67, 23))
        self.label.setStyleSheet("background: transparent;\n"
                                 "font: 75 12pt \"Arial\";\n"
                                 "color: rgb(0, 59, 70);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(245, 175, 87, 23))
        self.label_2.setStyleSheet("background: transparent;\n"
                                   "font: 75 12pt \"Arial\";\n"
                                   "color: rgb(0, 59, 70);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(428, 175, 91, 24))
        self.label_3.setWhatsThis("")
        self.label_3.setStyleSheet("background: transparent;\n"
                                   "font: 75 12pt \"Arial\";\n"
                                   "color: rgb(0, 59, 70);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(245, 245, 80, 23))
        self.label_4.setStyleSheet("font: 75 12pt \"Arial\";\n"
                                   "color: rgb(0, 61, 74);\n"
                                   "background: transparent;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(522, 449, 231, 31))
        self.label_6.setStyleSheet("background: transparent;\n"
                                   "font: 75 12pt \"Arial\";\n"
                                   "color: rgb(64, 110, 119);")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 20, 321, 41))
        self.label_5.setStyleSheet("font: 75 26pt \"Arial\";\n"
                                   "color: rgb(235, 242, 244);\n"
                                   "background:transparent;")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 240, 290, 30))
        self.lineEdit_2.setStyleSheet("border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 8px;\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "background: transparent;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setText(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop').replace('\\','/'))
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(355, 160, 57, 50))
        self.checkBox.setStyleSheet("QCheckBox::indicator {\n"
                                    "    width: 50px;\n"
                                    "    height: 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox::indicator::checked {\n"
                                    "    image: url(:/resources/image/swith-on.png);\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox::indicator::unchecked {\n"
                                    "    image: url(:/resources/image/switch-off.png);\n"
                                    "}")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(True)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(570, 370, 57, 51))
        self.checkBox_2.setStyleSheet("QCheckBox::indicator {\n"
                                      "    width: 50px;\n"
                                      "    height: 50px;\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox::indicator::checked {\n"
                                      "    \n"
                                      "    image: url(:/resources/image/robot2.png);\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox::indicator::unchecked {\n"
                                      "    image: url(:/resources/image/robot.png);\n"
                                      "}")
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUILD HELPER"))
        self.pushButton.setText(_translate("MainWindow", "GO"))
        self.pushButton_2.setText(_translate("MainWindow", "Change \n"
                                             " Directory"))
        self.label.setText(_translate("MainWindow", "User ID"))
        self.label_2.setText(_translate("MainWindow", "Only User"))
        self.label_3.setToolTip(_translate(
            "MainWindow", "<span style=\'font-size: 13px;\'>Переключатель в режиме \"All guild\" предоставляет информацию о всех участниках гильдии в которой состоит игрок.</span>"))
        self.label_3.setToolTipDuration(0)
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p>All Guild <span style=\" vertical-align:super;\">ⓘ</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Directory"))
        self.label_6.setText(_translate("MainWindow", "SWGOH.GG"))
        self.label_5.setText(_translate("MainWindow", "GUILD HELPER"))
        self.pushButton_2.clicked.connect(self.changeDirectory)
        # self.connect(self.progressBar.value==100, self.show_popup_success)
        

    def changeDirectory(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        fname = dialog.getExistingDirectory(self, 'Open file', os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        self.lineEdit_2.setText(fname)

    
    def startProgressBar(self):
        self.thread1 = MyThread(sleep=1.5)
        self.thread1.change_value.connect(self.changeValueOfProgressBar)
        self.thread1.start()
        self.thread2 = MyThread(sleep=0.3)
        self.thread2.change_value.connect(self.changeValueOfRobot)
        self.thread2.start()
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.checkBox.setEnabled(False)

    def changeValueOfProgressBar(self, val):
        self.progressBar.setValue(val)

    def changeValueOfRobot(self):
        self.checkBox_2.setChecked(not self.checkBox_2.isChecked())

    def show_popup(self):
        msg = PopupException("Can't find the player with id: ", self.lineEdit.text())
        msg.setupUi(msg)
        msg.exec_()

    def show_popup_ex(self):
        msg = PopupException("An unexpected error has occurred")
        msg.setupUi(msg)
        msg.exec_()

    def show_popup_success(self):
        msg = PopupException("Statistic was successfully complete")
        msg.setupUi(msg)
        msg.exec_()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
