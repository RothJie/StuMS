from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
import main
from service import service
import sys


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.editUser = QtWidgets.QLineEdit(self.centralwidget)
        self.editUser.setGeometry(QtCore.QRect(300, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        self.editUser.setFont(font)
        self.editUser.setObjectName("editUser")
        self.editPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.editPwd.setGeometry(QtCore.QRect(300, 230, 171, 31))
        self.editPwd.setObjectName("editPwd")
        self.editPwd.setEchoMode(QtWidgets.QLineEdit.Password)  # 设置密码的输入保护
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        # 设置窗体背景
        palette = QtGui.QPalette()
        palette.setBrush(MainWindow.backgroundRole(),
                         QBrush(QPixmap('./service/loginImg.png').
                                scaled(MainWindow.size(),
                                QtCore.Qt.IgnoreAspectRatio,
                                QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)

        # 为登录按钮绑定槽函数
        self.pushButton.clicked.connect(self.openMain)
        # 为密码框关联槽函数
        self.editPwd.editingFinished.connect(self.openMain)
        # 为退出按钮绑定槽函数
        self.pushButton_2.clicked.connect(LoginWindow.close)

    def openMain(self):
        """定义槽函数,在点击登录时打开主界面"""
        service.userName = self.editUser.text() # 获取用户名放到全局变量
        self.user_pwd = self.editPwd.text()

        if service.userName != "" or self.user_pwd != "":
            if service.userName == "" :
                QMessageBox.warning(None,"提示！","用户名不能为空！！！",QMessageBox.Ok)
            elif self.user_pwd == "":
                QMessageBox.warning(None,"提示！","密码不能为空！！！",QMessageBox.Ok)
            else:
                sql = 'select * from tb_user where userName=%s and userPwd=%s'
                result_ = service.query(sql, service.userName, self.user_pwd)
                if len(result_) > 0 :
                    self.m = main.Ui_MainWindow() # 创建主窗体对象
                    self.m.show()
                    MainWindow.hide() # 隐藏登录窗口
                else:
                    self.editPwd.clear() #清空
                    self.editUser.clear()
                    QMessageBox.warning(None, "提示！","用户名或密码错误！！！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None,"提示！","用户名或密码不能为空！！！",QMessageBox.Ok)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "学生成绩管理系统"))
        self.label.setText(_translate("LoginWindow", "用户名："))
        self.label_2.setText(_translate("LoginWindow", "密   码："))
        self.pushButton.setText(_translate("LoginWindow", "登录"))
        self.pushButton_2.setText(_translate("LoginWindow", "退出"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_LoginWindow()  # 创建已经设计好的pyqt5窗体，登录窗体
    MainWindow.backgroundRole()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
