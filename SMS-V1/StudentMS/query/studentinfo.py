# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentinfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
sys.path.append('../')
from service import service

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 787)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cboSelect = QtWidgets.QComboBox(self.centralwidget)
        self.cboSelect.setGeometry(QtCore.QRect(140, 20, 121, 31))
        self.cboSelect.setObjectName("cboSelect")
        self.cboSelect.addItem("学生编号")
        self.cboSelect.addItem("学生姓名")

        self.editKey = QtWidgets.QLineEdit(self.centralwidget)
        self.editKey.setGeometry(QtCore.QRect(410, 20, 121, 31))
        self.editKey.setObjectName("editKey")
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(580, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnQuery.setFont(font)
        self.btnQuery.setObjectName("btnQuery")
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setGeometry(QtCore.QRect(660, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnQuit.setFont(font)
        self.btnQuit.setObjectName("btnQuit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 781, 661))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnQuery.clicked.connect(self.query)  # 根据不同条件取查询，在这绑定槽函数
        self.btnQuit.clicked.connect(self.close)  # 为退出按钮绑定槽函数

    def query(self):
        self.tableWidget.setRowCount(0)  # 清空表格
        key = self.editKey.text()
        if key == "":  # 查询全部的学生信息
            result = service.query("select stuID,stuName,concat(gradeName,' ',className),age,sex,phone,address FROM v_studentinfo;")
        else:
            if self.cboSelect.currentText() == "学生编号":
                result = service.query("select stuID,stuName,concat(gradeName,' ',className),age,sex,phone,address FROM v_studentinfo WHERE stuID LIKE %s;","%"+key+"%")
            else:
                # 根据学生姓名模糊查询
                result = service.query(
                    "select stuID,stuName,concat(gradeName,' ',className),age,sex,phone,address FROM v_studentinfo WHERE stuName LIKE %s;",
                    "%" + key + "%")

        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["学生编号",'学生姓名',"年级","年龄","性别","联系电话","家庭住址"])
        for i in range(row):
            for j in range(7):
                data = QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)
        if row > 0:
            QMessageBox.information(None,'提示','数据查询成功！！！',QtWidgets.QMessageBox.Ok)
        else:
            QMessageBox.information(None,'提示','查询的数据为空！！！',QtWidgets.QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生信息查询"))
        self.btnQuery.setText(_translate("MainWindow", "查询"))
        self.btnQuit.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "选择查询列表："))
        self.label_2.setText(_translate("MainWindow", "查询关键字："))
