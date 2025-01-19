# -*- coding: utf-8 -*-
from pydoc import classname

# Form implementation generated from reading ui file 'classes.ui'
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
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.query()
        self.bindGrade()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(877, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(700, 100, 101, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddClass = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddClass.setFont(font)
        self.btnAddClass.setObjectName("btnAddClass")
        self.verticalLayout.addWidget(self.btnAddClass)
        self.btnUpdateClass = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdateClass.setFont(font)
        self.btnUpdateClass.setObjectName("btnUpdateClass")
        self.verticalLayout.addWidget(self.btnUpdateClass)
        self.btnDeleteClass = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDeleteClass.setFont(font)
        self.btnDeleteClass.setObjectName("btnDeleteClass")
        self.verticalLayout.addWidget(self.btnDeleteClass)
        self.btnQuitClass = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnQuitClass.setFont(font)
        self.btnQuitClass.setObjectName("btnQuitClass")
        self.verticalLayout.addWidget(self.btnQuitClass)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 440, 591, 41))
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
        self.editClassID = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.editClassID.setFont(font)
        self.editClassID.setObjectName("editClassID")
        self.horizontalLayout.addWidget(self.editClassID)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.editClassName = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.editClassName.setFont(font)
        self.editClassName.setObjectName("editClassName")
        self.horizontalLayout.addWidget(self.editClassName)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 490, 251, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 641, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnAddClass.clicked.connect(self.add)  # 为添加按钮链接add()一个槽函数
        self.tableWidget.itemClicked.connect(self.getItem)  # 在点击修改时需要为表控件添加一个槽函数，以便获取表中的元素
        self.btnUpdateClass.clicked.connect(self.edit)  # 为添加（更新数据）按钮链接edit()一个槽函数
        self.btnDeleteClass.clicked.connect(self.delete_)  # 为删除按钮添加槽函数
        self.btnQuitClass.clicked.connect(self.close)

    def query(self):
        """自定义一个槽函数，作用：在窗体启动时，将数据库中的考试类别信息读取出来。"""
        self.tableWidget.setRowCount(0)  # 清空表中的所有行
        # 调用公共类中的公共方法查询
        result = service.query("SELECT c.classID,g.gradeName,c.className FROM tb_grade g JOIN tb_class c ON g.gradeID = c.gradeID;")
        row = len(result)  # 获取到数据的行数
        self.tableWidget.setRowCount(row)  # 设置行数
        self.tableWidget.setColumnCount(3)  # 应为有2个字段所以要设置2列
        self.tableWidget.setHorizontalHeaderLabels(['班级编号','年级名称','班级名称'])  # 设置表格的标题
        for i in range(row):
            for j in range(self.tableWidget.columnCount()):
                date_single = QTableWidgetItem(str(result[i][j]))  # 将数据处理为表格控件能接受的数据对象
                self.tableWidget.setItem(i, j, date_single)  # 将数据依次放入表格中

    def bindGrade(self):
        """为年级组合框做数据查询，并且需要设置初始化"""
        self.comboBox.addItem("全部")
        result = service.query('select gradeName from tb_grade;')
        for i in result:
            self.comboBox.addItem(i[0])

    def getName(self,g_id,name):
        """到数据库中查找看是否有 name考试科目 的存在"""
        result = service.query('select * from tb_class where className = %s and gradeID = %s;', name,g_id) # 这里传参不能用元组
        return len(result)

    def add(self):
        """定义添加的槽函数，首先需要获取到需要的数据"""
        classid = self.editClassID.text()
        classname = self.editClassName.text()
        gradename = self.comboBox.currentText()   # 获取到年级名称必须赋值给新变量
        if gradename != '全部':
            gradeid = service.query('SELECT gradeID FROM tb_grade where gradeName = %s;', (gradename,))[0][0]
            print(gradeid)
            if classid != '' and classname != '':
                res = service.query('select * from tb_class where classID=%s;',(classid,))
                if len(res) > 0:
                    self.editClassID.setText("")
                    self.editClassName.setText("")
                    QMessageBox.warning(None, "警告", "该班级已经存在！请重新输入！！", QMessageBox.Ok)
                else:
                    res__ = service.execute('INSERT INTO tb_class(classID,gradeID,className) VALUES(%s,%s,%s)',(classid,gradeid,classname))
                    if res__ > 0:
                        self.query()
                        QMessageBox.information(None,'提示','数据添加成功了！',QMessageBox.Ok)
            else:
                QMessageBox.warning(None, "警告", "班级编号和年级名称不能为空！！！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None,"警告","请先选择年级！！！",QMessageBox.Ok)

    def getItem(self,item):
        """获取选中的表格内容，item代表鼠标点击的那一行"""
        if item.column() == 0:  # 第一列是编号
            self.select = item.text()
            self.editClassID.setText(self.select)   # 将点击获得的年级编个放到输入框中

        # if item.column() == 1:  # 第二列是编号
        #     self.select = item.text()
        #     self.editGradeName.setText(self.select)   # 将点击获得的年级编个放到输入框中

    def edit(self):
        """用于执行修改操作的槽函数"""
        try:
            if self.select != '':
                gradename = self.comboBox.currentText()
                if gradename == '全部':
                    QMessageBox.warning(None, "警告", "请先选择年级！！！", QMessageBox.Ok)
                else:
                    gradeid = service.query("select gradeID from tb_grade where gradeName = %s;",gradename)[0][0]
                    c_name = self.editClassName.text()
                    if c_name != '':
                        resu = self.getName(gradeid,c_name)
                        if resu > 0:
                                self.editClassName.setText("")
                                QMessageBox.warning(None, '警告', '需要修改的班级名称已经存在！！！', QMessageBox.Ok)
                        else:
                            resl = service.execute("UPDATE tb_class SET gradeID = %s, className = %s WHERE classID = %s;",
                                                   (gradeid,c_name,self.select))
                            if resl > 0:
                                self.query()
                                QMessageBox.information(None, '提示', "数据修改成功！", QMessageBox.Ok)
                    else:
                        QMessageBox.warning(None, '警告', '需要修改的班级名称不能为空！！！', QMessageBox.Ok)

        except Exception as e:
            print(e)
            QMessageBox.warning(None,'警告','请选中需要修改的班级编号！！！',QMessageBox.Ok)

    def delete_(self):
        try:
            if self.select != '':  # 删除年级表中的数据
                res = service.execute('delete from tb_class where classId=%s',(self.select,))
                if res > 0:
                    self.query()
                    QMessageBox.information(None,'提示','删除成功!',QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(None,'警告','请选择要删除的数据!',QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "班级设置"))
        self.btnAddClass.setText(_translate("MainWindow", "增加"))
        self.btnUpdateClass.setText(_translate("MainWindow", "修改"))
        self.btnDeleteClass.setText(_translate("MainWindow", "删除"))
        self.btnQuitClass.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "班级编号："))
        self.label_2.setText(_translate("MainWindow", "班级名称："))
        self.label_3.setText(_translate("MainWindow", "选择年级："))
