# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import *
from  settings import classes,examkinds,grade,subject
from baseinfo import student,result
from query import studentinfo,resultinfo
from system import userManager

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        # 主窗体不允许最大化
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGrade = QtWidgets.QAction(MainWindow)
        self.actionGrade.setObjectName("actionGrade")
        self.actionClass = QtWidgets.QAction(MainWindow)
        self.actionClass.setObjectName("actionClass")
        self.actionExamKind = QtWidgets.QAction(MainWindow)
        self.actionExamKind.setObjectName("actionExamKind")
        self.actionSubject = QtWidgets.QAction(MainWindow)
        self.actionSubject.setObjectName("actionSubject")
        self.actionStudent = QtWidgets.QAction(MainWindow)
        self.actionStudent.setObjectName("actionStudent")
        self.actionResult = QtWidgets.QAction(MainWindow)
        self.actionResult.setObjectName("actionResult")
        self.actionStudentInfo = QtWidgets.QAction(MainWindow)
        self.actionStudentInfo.setObjectName("actionStudentInfo")
        self.actionResultInfo = QtWidgets.QAction(MainWindow)
        self.actionResultInfo.setObjectName("actionResultInfo")
        self.actionUser = QtWidgets.QAction(MainWindow)
        self.actionUser.setObjectName("actionUser")
        self.menu.addAction(self.actionGrade)
        self.menu.addAction(self.actionClass)
        self.menu.addAction(self.actionExamKind)
        self.menu.addAction(self.actionSubject)
        self.menu_2.addAction(self.actionStudent)
        self.menu_2.addAction(self.actionResult)
        self.menu_3.addAction(self.actionStudentInfo)
        self.menu_3.addAction(self.actionResultInfo)
        self.menu_4.addAction(self.actionUser)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        # 设置窗体背景
        palette = QtGui.QPalette()
        palette.setBrush(MainWindow.backgroundRole(),
                         QBrush(QPixmap('./service/mainImg.jpg').
                                scaled(MainWindow.size(),
                                       QtCore.Qt.IgnoreAspectRatio,
                                       QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menubar.triggered[QtWidgets.QAction].connect(self.openSet)  # 菜单选项集关联功能集

    def openSet(self,m):
        """在主窗体中定义参函数"""
        if m.text() == '年级设置':
            self.m = grade.Ui_MainWindow()
            self.m.show()
        elif m.text() == '班级设置':
            self.m = classes.Ui_MainWindow()
            self.m.show()
        elif m.text() == '考试类别':
            self.m = examkinds.Ui_MainWindow()
            self.m.show()
        elif m.text() == '考试科目':
            self.m = subject.Ui_MainWindow()
            self.m.show()
        elif m.text() == '学生信息管理':
            self.m = student.Ui_MainWindow()
            self.m.show()
        elif m.text() == '学生成绩管理':
            self.m = result.Ui_MainWindow()
            self.m.show()
        elif m.text() == '学生信息查询':
            self.m = studentinfo.Ui_MainWindow()
            self.m.show()
        elif m.text() == '学生成绩查询':
            self.m = resultinfo.Ui_MainWindow()
            self.m.show()
        elif m.text() == '用户维护':
            self.m = userManager.Ui_MainWindow()
            self.m.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩管理系统"))
        self.menu.setTitle(_translate("MainWindow", "基础设置"))
        self.menu_2.setTitle(_translate("MainWindow", "基础信息管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统查询"))
        self.menu_4.setTitle(_translate("MainWindow", "系统管理"))
        self.actionGrade.setText(_translate("MainWindow", "年级设置"))
        self.actionClass.setText(_translate("MainWindow", "班级设置"))
        self.actionExamKind.setText(_translate("MainWindow", "考试类别"))
        self.actionSubject.setText(_translate("MainWindow", "考试科目"))
        self.actionStudent.setText(_translate("MainWindow", "学生信息管理"))
        self.actionResult.setText(_translate("MainWindow", "学生成绩管理"))
        self.actionStudentInfo.setText(_translate("MainWindow", "学生信息查询"))
        self.actionResultInfo.setText(_translate("MainWindow", "学生成绩查询"))
        self.actionUser.setText(_translate("MainWindow", "用户维护"))
