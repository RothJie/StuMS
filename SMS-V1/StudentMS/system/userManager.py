from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

sys.path.append("../") # 因为grade.py需要先从当前路径切换到service中
from service import service


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.query()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 20, 551, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.editUser = QtWidgets.QLineEdit(self.centralwidget)
        self.editUser.setGeometry(QtCore.QRect(169, 390, 141, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.editUser.setFont(font)
        self.editUser.setObjectName("editUser")
        self.editCode = QtWidgets.QLineEdit(self.centralwidget)
        self.editCode.setGeometry(QtCore.QRect(489, 390, 141, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.editCode.setFont(font)
        self.editCode.setObjectName("editCode")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 400, 61, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 400, 51, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 440, 531, 91))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnUpdate = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnQuit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnQuit.setFont(font)
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout.addWidget(self.btnQuit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnAdd.clicked.connect(self.add_)
        self.tableWidget.itemClicked.connect(self.getItem)
        self.btnUpdate.clicked.connect(self.edit)
        self.btnDelete.clicked.connect(self.delete)
        self.btnQuit.clicked.connect(self.close)

    def query(self):
        self.tableWidget.setRowCount(0)  # 清空表中的所有行
        # 调用公共类中的公共方法查询
        result = service.query('select * from tb_user;')
        row = len(result)  # 获取到数据的行数
        self.tableWidget.setRowCount(row)  # 设置行数
        self.tableWidget.setColumnCount(2)  # 应为有2个字段所以要设置2列
        self.tableWidget.setHorizontalHeaderLabels(['用户名', '密 码'])  # 设置表格的标题
        for i in range(row):
            for j in range(self.tableWidget.columnCount()):
                date_single = QTableWidgetItem(str(result[i][j]))  # 将数据处理为表格控件能接受的数据对象
                self.tableWidget.setItem(i, j, date_single)  # 将数据依次放入表格中

    def getName(self,name):     # (name,) 元组类型，其中只有一个函数时就要加一个，。
        """到数据库中查找看是否有 name年级名称 的存在"""
        result = service.query('select * from tb_user where userName = %s;',(name,))
        return len(result)

    def add_(self):
        username = self.editUser.text()
        pwd = self.editCode.text()
        if username != '' and pwd != '':
            if self.getName(username) > 0:  # 说明要添加的数据在数据库中已经存在
                self.editUser.setText('')
                QMessageBox.information(None, '提示', '年级名称已经存在！请重新输入！！')
            else:
                resu = service.execute("INSERT INTO tb_user(userName,userPwd) VALUES (%s,%s);", (username, pwd))
                if resu > 0:
                    self.query()
                    QMessageBox.information(None, '提示', '信息添加成功了！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '用户名或密码不能为空！', QMessageBox.Ok)

    def getItem(self,item):
        """获取选中的表格内容，item代表鼠标点击的那一行"""
        if item.column() == 0:  # 第一列是user
            self.select = item.text()
            self.editUser.setText(self.select)
            row = item.row()
            self.editCode.setText(self.tableWidget.item(row,1).text())

    def edit(self):
        try:
            if self.select != "":
                if self.editCode.text() != "":
                    resu = service.execute("UPDATE tb_user SET userPwd=%s WHERE userName = %s;",(self.editCode.text(), self.editUser.text()))
                    if resu > 0:
                        self.query()
                        QMessageBox.information(None,'提示',"密码修改成功！",QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '警告', "请先确认填入密码！", QMessageBox.Ok)

        except Exception as e:
            QMessageBox.warning(None, '警告', "请先选中你要修改的数据！", QMessageBox.Ok)

    def delete(self):
        try:
            if self.select != "":
                if self.select == service.userName:
                    QMessageBox.warning(None,'警告',"正在登录的用户不能被删除！",QMessageBox.Ok)
                else:
                    resul = QMessageBox.warning(None,"警告","请确认是否需要删除用户！",QMessageBox.Yes|QMessageBox.Cancel)
                    if resul == QMessageBox.Yes:
                        resu = service.execute("DELETE FROM tb_user WHERE userName = %s;",(self.select,))
                        if resu > 0:
                            self.query()
                            QMessageBox.information(None,'提示',"删除成功！",QMessageBox.Ok)
                    elif resul == QMessageBox.Cancel:
                        self.editUser.clear()
                        self.editCode.clear()
        except Exception as e:
            print(e)
            QMessageBox.warning(None, '警告', "请先选中你要修改的数据！", QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名:"))
        self.label_2.setText(_translate("MainWindow", "密  码:"))
        self.btnAdd.setText(_translate("MainWindow", "增加"))
        self.btnUpdate.setText(_translate("MainWindow", "修改"))
        self.btnDelete.setText(_translate("MainWindow", "删除"))
        self.btnQuit.setText(_translate("MainWindow", "退出"))
