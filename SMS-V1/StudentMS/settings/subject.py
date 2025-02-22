# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
sys.path.append("/") # 因为grade.py需要先从当前路径切换到service中
from service import service

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.query()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 110, 101, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddSubject = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddSubject.setFont(font)
        self.btnAddSubject.setObjectName("btnAddSubject")
        self.verticalLayout.addWidget(self.btnAddSubject)
        self.btnUpdateSubject = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdateSubject.setFont(font)
        self.btnUpdateSubject.setObjectName("btnUpdateSubject")
        self.verticalLayout.addWidget(self.btnUpdateSubject)
        self.btnDeleteSubject = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDeleteSubject.setFont(font)
        self.btnDeleteSubject.setObjectName("btnDeleteSubject")
        self.verticalLayout.addWidget(self.btnDeleteSubject)
        self.btnQuitSubject = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnQuitSubject.setFont(font)
        self.btnQuitSubject.setObjectName("btnQuitSubject")
        self.verticalLayout.addWidget(self.btnQuitSubject)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 510, 591, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editSubjectID = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.editSubjectID.setFont(font)
        self.editSubjectID.setObjectName("editSubjectID")
        self.horizontalLayout.addWidget(self.editSubjectID)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.editSubjectName = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.editSubjectName.setFont(font)
        self.editSubjectName.setObjectName("editSubjectName")
        self.horizontalLayout.addWidget(self.editSubjectName)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 631, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnAddSubject.clicked.connect(self.add)  # 为添加按钮链接add()一个槽函数
        self.tableWidget.itemClicked.connect(self.getItem)  # 在点击修改时需要为表控件添加一个槽函数，以便获取表中的元素
        self.btnUpdateSubject.clicked.connect(self.edit)  # 为添加（更新数据）按钮链接edit()一个槽函数
        self.btnDeleteSubject.clicked.connect(self.delete_)  # 为删除按钮添加槽函数
        self.btnQuitSubject.clicked.connect(self.close)

    def query(self):
        """自定义一个槽函数，作用：在窗体启动时，将数据库中的考试类别信息读取出来。"""
        self.tableWidget.setRowCount(0)  # 清空表中的所有行
        # 调用公共类中的公共方法查询
        result = service.query('select * from tb_subject;')
        row = len(result)  # 获取到数据的行数
        self.tableWidget.setRowCount(row)  # 设置行数
        self.tableWidget.setColumnCount(2)  # 应为有2个字段所以要设置2列
        self.tableWidget.setHorizontalHeaderLabels(['科目编号', '科目名称'])  # 设置表格的标题
        for i in range(row):
            for j in range(self.tableWidget.columnCount()):
                date_single = QTableWidgetItem(str(result[i][j]))  # 将数据处理为表格控件能接受的数据对象
                self.tableWidget.setItem(i, j, date_single)  # 将数据依次放入表格中

    def getName(self, name):  # (name,) 元组类型，其中只有一个函数时就要加一个，。
        """到数据库中查找看是否有 name年级名称 的存在"""
        result = service.query('select * from tb_subject where subName = %s;', (name,))
        return len(result)

    def add(self):
        """执行添加操作前，需要获取添加的学科ID和科目名称"""
        subid = self.editSubjectID.text()
        subname = self.editSubjectName.text()
        if subid != '' and subname != '':
            if self.getName(subname) > 0:  # 说明要添加的数据在数据库中已经存在
                self.editSubjectName.setText('')
                QMessageBox.information(None, '提示', '科目名称已经存在！请重新输入！！')
            else:
                resl = service.execute('insert into tb_subject(subID,subName) values (%s,%s)', (subid,subname))
                if resl > 0:
                    self.query()  # 重新加载表格数据
                    QMessageBox.information(None, '提示', '信息添加成功了！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '科目编号或者科目名称不能为空！', QMessageBox.Ok)

    def getItem(self, item):
        """获取选中的表格内容，item代表鼠标点击的那一行"""
        if item.column() == 0:  # 第一列是编号
            self.select = item.text()
            self.editSubjectID.setText(self.select)  # 将点击获得的年级编个放到输入框中

        # if item.column() == 1:  # 第二列是编号
        #     self.select = item.text()
        #     self.editGradeName.setText(self.select)   # 将点击获得的年级编个放到输入框中

    def edit(self):
        """用于执行修改操作的函数"""
        try:
            if self.select != '':  # 判断年级编号是否有值
                subjectName = self.editSubjectName.text()
                if subjectName != '':  # 如果年级名称也有了，就到数据库中看看是否已经存在数据
                    if self.getName(subjectName) > 0:
                        QMessageBox.information(None, '提示', '要修改的科目名称已经存在！', QMessageBox.Ok)
                    else:
                        resl = service.execute('update tb_subject set subName=%s where subId=%s',
                                               (subjectName, self.select))
                        if resl > 0:
                            self.query()
                            QMessageBox.information(None, '提示', '数据已经修改成功了！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '警告', '科目名称不能为空！', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(None, '警告', '请选中需要修改的数据！', QMessageBox.Ok)

    def delete_(self):
        try:
            if self.select != '':  # 删除年级表中的数据
                res = service.execute('delete from tb_subject where subID=%s', (self.select,))
                if res > 0:
                    self.query()
                    QMessageBox.information(None, '提示', '删除成功!', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(None, '警告', '请选择要删除的数据!', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "考试科目设置"))
        self.btnAddSubject.setText(_translate("MainWindow", "增加"))
        self.btnUpdateSubject.setText(_translate("MainWindow", "修改"))
        self.btnDeleteSubject.setText(_translate("MainWindow", "删除"))
        self.btnQuitSubject.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "科目编号："))
        self.label_2.setText(_translate("MainWindow", "科目名称："))
