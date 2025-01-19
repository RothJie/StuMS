import sys
import time
from service import service
from StudentMS.UI import src_rc
from PyQt5.QtCore import Qt
from UI import loginUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import main

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loginUI.Ui_MainWindow()
        self.update_window_attr()
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        # 为登录按钮绑定槽函数
        self.ui.btn_login.clicked.connect(self.openMain)
        # 为注册按钮绑定槽函数
        self.ui.btn_resgister.clicked.connect(self.register_func)
        self.m = None

    def update_window_attr(self):
        self.ui.setupUi(self)

        # 设置窗口为始终在最顶层、无边框且背景透明
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def openMain(self):
        """定义槽函数,在点击登录时打开主界面"""
        service.userName = self.ui.editUser.text() # 获取用户名放到全局变量
        self.user_pwd = self.ui.editPwd.text()
        if service.userName != "" or self.user_pwd != "":
            if service.userName == "" : # 1
                self.ui.stackedWidget.setCurrentIndex(1)
            elif self.user_pwd == "": #2
                self.ui.stackedWidget.setCurrentIndex(2)
            else:
                sql = 'select * from tb_user where userName=%s and userPwd=%s'
                result_ = service.query(sql, service.userName, self.user_pwd)
                if len(result_) > 0 :
                    self.m= main.MainUI() # 创建主窗体对象
                    self.m.show()
                    self.hide() # 隐藏登录窗口
                else:
                    self.ui.editPwd.clear() #清空
                    self.ui.editUser.clear()
                    self.ui.stackedWidget.setCurrentIndex(3) #3

        else:# 4
            self.ui.stackedWidget.setCurrentIndex(4)

    def register_func(self):
        """用于实现注册功能"""
        pwd = self.ui.editPwd_2.text()
        pwd_sure = self.ui.editPwd_2sure.text()
        user = self.ui.editUser_2.text()
        if pwd != pwd_sure:
            QMessageBox.warning(self,'警告','两次输入的密码不一致！',QMessageBox.Ok)
        else:
            if user != "":
                resu = service.query('SELECT * FROM tb_user WHERE userName=%s AND userPwd=%s', user, pwd_sure)
                if len(resu) == 0 : # 说明执行失败，用户并不存在于数据库中，可以执行增加用户操作
                    resul = service.execute('INSERT INTO tb_user VALUES(%s,%s);',(user,pwd_sure))
                    if resul == 1:
                        self.ui.stackedWidget_2.setCurrentIndex(0)
                        QMessageBox.information(self, '提示', '注册成功！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, '警告', '你已经注册过了！请直接登录或更换用户名！', QMessageBox.Ok)
                    self.ui.stackedWidget_2.setCurrentIndex(0)
            else:
                QMessageBox.warning(self, '警告', '用户名不能为空！', QMessageBox.Ok)

if __name__ == '__main__':
    app  = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())