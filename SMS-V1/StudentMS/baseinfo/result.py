from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

from service.service import query

sys.path.append('../')
from service import service


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.query()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 794)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(890, 700, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(740, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.cboSelectKind = QtWidgets.QComboBox(self.centralwidget)
        self.cboSelectKind.setGeometry(QtCore.QRect(130, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.cboSelectKind.setFont(font)
        self.cboSelectKind.setObjectName("cboSelectKind")
        self.cboSelectGrade = QtWidgets.QComboBox(self.centralwidget)
        self.cboSelectGrade.setGeometry(QtCore.QRect(360, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.cboSelectGrade.setFont(font)
        self.cboSelectGrade.setObjectName("cboSelectGrade")
        self.cboSelectClass = QtWidgets.QComboBox(self.centralwidget)
        self.cboSelectClass.setGeometry(QtCore.QRect(590, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.cboSelectClass.setFont(font)
        self.cboSelectClass.setObjectName("cboSelectClass")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cboStuName = QtWidgets.QComboBox(self.centralwidget)
        self.cboStuName.setGeometry(QtCore.QRect(500, 700, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.cboStuName.setFont(font)
        self.cboStuName.setObjectName("cboStuName")
        self.cboExamSubject = QtWidgets.QComboBox(self.centralwidget)
        self.cboExamSubject.setGeometry(QtCore.QRect(730, 700, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.cboExamSubject.setFont(font)
        self.cboExamSubject.setObjectName("cboExamSubject")
        self.editResult = QtWidgets.QLineEdit(self.centralwidget)
        self.editResult.setGeometry(QtCore.QRect(940, 700, 71, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.editResult.setFont(font)
        self.editResult.setObjectName("editResult")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 981, 611))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1020, 170, 71, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnModify = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModify.setFont(font)
        self.btnModify.setObjectName("btnModify")
        self.verticalLayout.addWidget(self.btnModify)
        self.btnDelect = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelect.setFont(font)
        self.btnDelect.setObjectName("btnDelect")
        self.verticalLayout.addWidget(self.btnDelect)
        self.btnQuit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnQuit.setFont(font)
        self.btnQuit.setObjectName("btnQuit")
        self.verticalLayout.addWidget(self.btnQuit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.itemClicked.connect(self.getItem)
        self.btnQuit.clicked.connect(self.close) # 为退出按钮绑定槽函数
        self.bindExamKind()
        self.bindExamSub()
        self.bindGrade()
        self.bindClass()
        self.cboSelectGrade.currentIndexChanged.connect(self.bindClass)
        self.cboSelectClass.currentIndexChanged.connect(self.bindStuName)
        self.btnUpdate.clicked.connect(self.query)
        self.btnAdd.clicked.connect(self.add)
        self.btnModify.clicked.connect(self.edit)
        self.btnDelect.clicked.connect(self.delete)

    def bindGrade(self):
        """为年级组合框做数据查询，并且需要设置初始化"""
        self.cboSelectGrade.addItem("全部")
        result = service.query('select gradeName from tb_grade;')
        for i in result:
            self.cboSelectGrade.addItem(i[0])

    def bindClass(self):
        """为班级的组合框查询数据，并绑定"""
        self.cboSelectClass.clear() # 清空下拉组合中的内容
        self.cboSelectClass.addItem("全部")
        result = service.query('select className from v_classInfo WHERE gradeName = %s;',self.cboSelectGrade.currentText())
        for item in result:
            self.cboSelectClass.addItem(item[0])

    def bindExamKind(self):
        self.cboSelectKind.addItem("全部")
        result = service.query('select kindName from tb_examkinds;')
        for item in result:
            self.cboSelectKind.addItem(item[0])

    def bindStuName(self):
        self.cboStuName.clear()  # 清空下拉组合中的内容
        result = service.query("SELECT stuName FROM v_studentinfo WHERE gradeName = %s AND className = %s;",self.cboSelectGrade.currentText(),self.cboSelectClass.currentText())
        for item in result:
            self.cboStuName.addItem(item[0])

    def bindExamSub(self):
        self.cboExamSubject.addItem("全部")
        result = service.query('select subName from tb_subject;')
        for item in result:
            self.cboExamSubject.addItem(item[0])

    def query(self):
        """"在数据库中找到v_resultinfo表并且把数据查询出来放到表格控件中"""
        self.tableWidget.setRowCount(0)
        # 获取三个值
        kind = self.cboSelectKind.currentText()
        grade = self.cboSelectGrade.currentText()
        classname = self.cboSelectClass.currentText()
        if kind == '全部':
            if grade == '全部':
                if classname == '全部':
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo;")
                    # 查询全部数据
                else:
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE className = %s;",classname)
                    # 根据班级
            else:
                if classname == "全部":
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE gradeName = %s;",grade)
                    # 根据年级
                else:
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE gradeName = %s and className = %s;",grade,classname)
                    # 根据年级和班级
        else:
            if grade == "全部":
                if classname == "全部":
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s;",kind)
                    # 更具考试种类kind
                else:
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s and className;",kind,classname)
                    # 根据考试种类kind和班级
            else:
                if classname == "全部":
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s and gradeName = %s;",kind,grade)
                    # 根据考试的种类kind和年级
                else:
                    result = query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s and gradeName = %s and className = %s;",kind,grade,classname)
                    # 根据考试的种类kind和年级、班级

        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['学生编号','学生姓名','班级','考试类型','科目名称','成绩'])
        for i in range(row):
            for j in range(6):
                data = QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i,j,data)

    def judge_stu(self,stuid,kindid,subid):
        result = service.query("SELECT * FROM tb_result WHERE stuID = %s AND kindID =%s AND subID =%s;",stuid,kindid,subid)
        if len(result) >0:
            return False
        else:
            return True

    def add(self):
        """判断，并添加"""
        e_kind = self.cboSelectKind.currentText()
        e_grade = self.cboSelectGrade.currentText()
        e_class = self.cboSelectClass.currentText()
        e_sub = self.cboExamSubject.currentText()
        e_stuName = self.cboStuName.currentText()
        e_score = self.editResult.text()
        if e_kind != '全部':
            kindid = service.query("SELECT kindID FROM tb_examkinds where kindName=%s;",e_kind)[0][0]
            if e_sub != '全部':
                subid = service.query("SELECT subID FROM tb_subject where subName=%s;", e_sub)[0][0]
                if e_stuName != '':
                    if e_grade != "全部" and e_class != "全部":
                        stuid = service.query("SELECT stuID FROM v_studentinfo WHERE gradeName = %s AND className = %s AND stuName = %s;",e_grade,e_class,e_stuName)[0][0]
                        if e_score !="":
                            if self.judge_stu(stuid,kindid,subid):
                                reut = service.execute('INSERT INTO tb_result (stuID,kindID,subID,result) VALUES(%s,%s,%s,%s);',(stuid,kindid,subid,e_score))
                                if reut> 0:
                                    self.query()
                                    QMessageBox.information(None,"提示","数据添加成功！",QMessageBox.Ok)
                            else:
                                QMessageBox.warning(None, "警告", "该学生成绩已经存在！！！", QMessageBox.Ok)

                        else:
                            QMessageBox.warning(None, "警告", "请先填写分数！！！", QMessageBox.Ok)
                    else:
                        QMessageBox.warning(None, "警告", "请先选择年级和班级！！！", QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, "警告", "请先选择姓名！！！", QMessageBox.Ok)
            else:
                QMessageBox.warning(None, "警告", "请先选择考试科目！！！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, "警告", "请先选择考试类别！！！", QMessageBox.Ok)

    def getItem(self,item:QTableWidgetItem):
        if item.column() == 0:
            self.select = item.text()
            row = item.row()
            cols = self.tableWidget.columnCount()
            row_data = [self.tableWidget.item(row,col).text() for col in range(cols)]
            self.cboStuName.setCurrentText(row_data[1])
            self.cboSelectGrade.setCurrentText(row_data[2].split(" ")[0])
            self.cboSelectClass.setCurrentText(row_data[2].split(" ")[1])
            self.cboSelectKind.setCurrentText(row_data[3])
            self.cboExamSubject.setCurrentText(row_data[4])
            self.editResult.setText('')
            self.k_id = service.query("SELECT kindID FROM tb_examkinds where kindName=%s;", row_data[3])[0][0]
            self.suid = service.query("SELECT subID FROM tb_subject where subName=%s;", row_data[4])[0][0]

    def edit(self):
        try :
            if self.select != '':
                score_ = self.editResult.text()
                if score_ != '':
                    reu = service.execute("UPDATE tb_result SET result=%s WHERE stuID = %s AND kindID =%s AND subID =%s",(score_,self.select,self.k_id,self.suid))
                    if reu > 0:
                        self.query()
                        QMessageBox.information(None,"提示","数据修改成功！！",QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '警告', '请先填入数据！！', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(None, '警告', '请先选择需要修改的成绩的学生编号！！', QMessageBox.Ok)

    def delete(self):
        try:
            if self.select != '':
                sure_ = QMessageBox.warning(None, '警告', '请确认是否需要删除该学生的成绩！！！学生信息删除后不能恢复！',
                                           QMessageBox.Yes | QMessageBox.Cancel)
                if sure_ == QMessageBox.Yes:
                    resu = service.execute("DELETE FROM tb_result WHERE stuID = %s AND kindID =%s AND subID =%s;", (self.select,self.k_id,self.suid))
                    if resu > 0:
                        self.editResult.clear()
                        self.query()
                        QMessageBox.information(None, '提示', '学生考试成绩信息已被成功删除!', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(None, '警告', '请先选择需要删除的数据！！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩管理"))
        self.label.setText(_translate("MainWindow", "考试种类："))
        self.label_2.setText(_translate("MainWindow", "选择年级："))
        self.label_3.setText(_translate("MainWindow", "选择班级："))
        self.label_4.setText(_translate("MainWindow", "成绩："))
        self.btnUpdate.setText(_translate("MainWindow", "刷新"))
        self.label_5.setText(_translate("MainWindow", "学生姓名："))
        self.label_6.setText(_translate("MainWindow", "考试科目："))
        self.btnAdd.setText(_translate("MainWindow", "增加"))
        self.btnModify.setText(_translate("MainWindow", "修改"))
        self.btnDelect.setText(_translate("MainWindow", "删除"))
        self.btnQuit.setText(_translate("MainWindow", "退出"))
