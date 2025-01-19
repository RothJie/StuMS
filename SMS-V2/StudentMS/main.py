import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


from StudentMS.UI import src_rc
from service import service
from UI import mainUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QTableWidgetItem, QMessageBox, QPushButton, QVBoxLayout


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainUI.Ui_MainWindow()
        self.update_window_attr()

        self.baseSetMenu = QMenu()
        self.setInfo = QMenu()
        self.queryInfo = QMenu()

        action1 = self.baseSetMenu.addAction("年级设置")
        action2 = self.baseSetMenu.addAction("班级设置")
        action3 = self.baseSetMenu.addAction("考试类别设置")
        action4 = self.baseSetMenu.addAction("考试科目设置")
        action5 = self.setInfo.addAction("学生信息设置")
        action6 = self.setInfo.addAction("考试信息设置")
        action7 = self.queryInfo.addAction("学生信息查询")
        action8 = self.queryInfo.addAction("考试结果查询")

        self.ui.pushButton_6.setMenu(self.baseSetMenu)
        self.ui.pushButton_7.setMenu(self.setInfo)
        self.ui.pushButton_8.setMenu(self.queryInfo)
        # 菜单栏绑定界面
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        action1.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        action2.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(2))
        action3.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(3))
        action4.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(4))
        action5.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(5))
        action6.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(6))
        action7.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(7))
        action8.triggered.connect(lambda:self.ui.stackedWidget.setCurrentIndex(8))
        # 为班级绑定槽函数
        self.class_query()
        self.ui.pushButton_10.clicked.connect(self.class_add)
        self.class_bindGrade()
        self.ui.tableWidget_4.itemClicked.connect(self.class_getItem)

        # 为年级绑定槽函数
        self.grade_query()
        self.ui.pushButton_9.clicked.connect(self.grade_add)
        self.ui.tableWidget_3.itemClicked.connect(self.grade_getItem)

        # 为考试类别绑定槽函数
        self.kind_query()
        self.ui.pushButton_11.clicked.connect(self.kind_add)
        self.ui.tableWidget_5.itemClicked.connect(self.kind_getItem)

        # 为考试科目绑定槽函数
        self.sub_query()
        self.ui.pushButton_12.clicked.connect(self.sub_add)
        self.ui.tableWidget_6.itemClicked.connect(self.sub_getItem)

        # 为学生信息shezhi绑定槽函数
        self.bas_re_bindGrade()
        self.ui.cboClass_2.addItem("全部")
        self.ui.cboGrde_2.currentIndexChanged.connect(self.bas_re_bindClass)
        self.ui.btnBush_2.clicked.connect(self.bas_re_query)
        self.ui.btnAdd_2.clicked.connect(self.bas_re_add)
        self.ui.tableWidget.itemClicked.connect(self.bas_re_getItem)

        # 为学生考试成绩设置绑定函数
        self.ui.tableWidget_2.itemClicked.connect(self.bas_resu_getItem)
        self.bas_resu_bindExamKind()
        self.bas_resu_bindExamSub()
        self.bas_resu_bindGrade()
        self.ui.cboSelectKind_6.addItem("全部")
        self.ui.cboSelectKind_7.currentIndexChanged.connect(self.bas_resu_bindClass)
        self.ui.cboSelectKind_6.currentIndexChanged.connect(self.bas_resu_bindStuName)
        self.ui.btnUpdate.clicked.connect(self.bas_resu_query)
        self.ui.btnUpdate_2.clicked.connect(self.bas_resu_add)

        # 为查询学生信息绑定槽函数
        self.ui.btnQuery.clicked.connect(self.q_query)
        self.ui.cboSelect.addItem("学生编号")
        self.ui.cboSelect.addItem("学生姓名")

        # 为查询学生考试结果绑定槽函数
        self.q_bindExamKind()
        self.q_bindSubject()
        self.ui.pushButton_13.clicked.connect(self.q_r_query)

    def update_window_attr(self):
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

# 班级设置，班级设置班级设置班级设置班级设置班级设置班级设置班级设置班级设置
    def class_query(self):
        """自定义一个槽函数，作用：在窗体启动时，将数据库中的考试类别信息读取出来。"""
        self.ui.tableWidget_4.setRowCount(0)  # 清空表中的所有行
        # 调用公共类中的公共方法查询
        result = service.query("SELECT c.classID,g.gradeName,c.className FROM tb_grade g JOIN tb_class c ON g.gradeID = c.gradeID;")
        row = len(result)  # 获取到数据的行数
        self.ui.tableWidget_4.setRowCount(row)  # 设置行数
        self.ui.tableWidget_4.setColumnCount(5)

        self.ui.tableWidget_4.setHorizontalHeaderLabels(['班级编号','年级名称','班级名称','操作1','操作2'])  # 设置表格的标题
        for i in range(row):
            for j in range(3):
                date_single = QTableWidgetItem(str(result[i][j]))  # 将数据处理为表格控件能接受的数据对象
                self.ui.tableWidget_4.setItem(i, j, date_single)  # 将数据依次放入表格中
            # 创建两个按钮
            button1 = QPushButton("修改")
            button2 = QPushButton("删除")
            # 将按钮的点击信号连接到槽函数
            button1.clicked.connect(lambda checked, r = i: self.grade_edit(r))
            button2.clicked.connect(lambda checked, r = i: self.grade_delete_(r))
            # 将按钮添加到表格布局中
            self.ui.tableWidget_4.setCellWidget(i, 3, button1)
            self.ui.tableWidget_4.setCellWidget(i, 4, button2)

    def class_bindGrade(self):
        """为年级组合框做数据查询，并且需要设置初始化"""
        self.ui.comboBox.addItem("全部")
        result = service.query('select gradeName from tb_grade;')
        for i in result:
            self.ui.comboBox.addItem(i[0])

    def class_getName(self,g_id,name):
        """到数据库中查找看是否有 name考试科目 的存在"""
        result = service.query('select * from tb_class where className = %s and gradeID = %s;', name,g_id) # 这里传参不能用元组
        return len(result)

    def class_add(self):
        """定义添加的槽函数，首先需要获取到需要的数据"""
        classid = self.ui.lineEdit_3.text()
        classname = self.ui.lineEdit_4.text()
        gradename = self.ui.comboBox.currentText()   # 获取到年级名称必须赋值给新变量
        print(classid,classname,gradename)
        if gradename != '全部':
            gradeid = service.query('SELECT gradeID FROM tb_grade where gradeName = %s;', (gradename,))[0][0]
            if classid != '' and classname != '':
                res = service.query('select * from tb_class where classID=%s;',(classid,))
                if len(res) > 0:
                    self.ui.lineEdit_3.setText("")
                    self.ui.lineEdit_4.setText("")
                    QMessageBox.warning(self, "警告", "该班级已经存在！请重新输入！！", QMessageBox.Ok)
                else:
                    res__ = service.execute('INSERT INTO tb_class(classID,gradeID,className) VALUES(%s,%s,%s)',(classid,gradeid,classname))
                    if res__ > 0:
                        self.class_query()
                        QMessageBox.information(self,'提示','数据添加成功了！',QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "警告", "班级编号和年级名称不能为空！！！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"警告","请先选择年级！！！",QMessageBox.Ok)

    def class_getItem(self,item):
        """获取选中的表格内容，item代表鼠标点击的那一行"""
        if item.column() == 0:  # 第一列是编号
            self.select = item.text()
            row = item.row()
            cols = 3
            row_data = [self.ui.tableWidget_4.item(row, col).text() for col in range(cols)]
            self.ui.comboBox.setCurrentText(row_data[1])
            self.ui.lineEdit_3.setText(row_data[0])
            self.ui.lineEdit_4.setText(row_data[2])

        # if item.column() == 1:  # 第二列是编号
        #     self.select = item.text()
        #     self.editGradeName.setText(self.select)   # 将点击获得的年级编个放到输入框中

    def class_edit(self,row):
        """用于执行修改操作的槽函数"""
        try:
            class_id = self.ui.lineEdit_3.text()
            if class_id != '':
                gradename = self.ui.comboBox.currentText()
                if gradename == '全部':
                    QMessageBox.warning(self, "警告", "请先选择年级！！！", QMessageBox.Ok)
                else:
                    gradeid = service.query("select gradeID from tb_grade where gradeName = %s;",gradename)[0][0]
                    c_name = self.ui.lineEdit_4.text()
                    if c_name != '':
                        resu = self.class_getName(gradeid,c_name)
                        if resu > 0:
                                self.ui.lineEdit_4.setText("")
                                QMessageBox.warning(self, '警告', '需要修改的班级名称已经存在！！！', QMessageBox.Ok)
                        else:
                            resl = service.execute("UPDATE tb_class SET gradeID = %s, className = %s WHERE classID = %s;",
                                                   (gradeid,c_name,class_id))
                            if resl > 0:
                                self.class_query()
                                QMessageBox.information(self, '提示', "第{}数据修改成功！".format(row), QMessageBox.Ok)
                    else:
                        QMessageBox.warning(self, '警告', '需要修改的班级名称不能为空！！！', QMessageBox.Ok)

        except Exception as e:
            print(e)
            QMessageBox.warning(self,'警告','请选中需要修改的班级编号！！！',QMessageBox.Ok)

    def class_delete_(self,row):
        try:
            if self.select != '':  # 删除年级表中的数据
                res = service.execute('delete from tb_class where classId=%s',(self.ui.lineEdit_3.text(),))
                if res > 0:
                    self.class_query()
                    QMessageBox.information(self,'提示',f'第{row}数据删除成功!',QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self,'警告','请选择要删除的数据!',QMessageBox.Ok)
# 年级年级年级年级年级年级年级年级年级年级年级年级年级年级年级年级年级年级设置
    def grade_query(self):
        """自定义一个槽函数，作用：在窗体启动时，将数据库中的考试类别信息读取出来。"""
        self.ui.tableWidget_3.setRowCount(0)  # 清空表中的所有行
        # 调用公共类中的公共方法查询
        result_g = service.query("select * from tb_grade;")
        row = len(result_g)  # 获取到数据的行数
        self.ui.tableWidget_3.setRowCount(row)  # 设置行数
        self.ui.tableWidget_3.setColumnCount(4)

        self.ui.tableWidget_3.setHorizontalHeaderLabels(['年级编号','年级名称','操作1','操作2'])  # 设置表格的标题
        for i in range(row):
            for j in range(2):
                date_single_ = QTableWidgetItem(str(result_g[i][j]))  # 将数据处理为表格控件能接受的数据对象
                self.ui.tableWidget_3.setItem(i, j, date_single_)  # 将数据依次放入表格中
            # 创建两个按钮
            button1 = QPushButton("修改")
            button2 = QPushButton("删除")
            # 将按钮的点击信号连接到槽函数
            button1.clicked.connect(lambda checked, r = i: self.grade_edit(r))
            button2.clicked.connect(lambda checked, r = i: self.grade_delete_(r))
            # 将按钮添加到表格布局中
            self.ui.tableWidget_3.setCellWidget(i, 2, button1)
            self.ui.tableWidget_3.setCellWidget(i, 3, button2)

    def grade_getName(self,name):     # (name,) 元组类型，其中只有一个函数时就要加一个，。
        """到数据库中查找看是否有 name年级名称 的存在"""
        result = service.query('select * from tb_grade where gradeName = %s;',(name,))
        return len(result)

    def grade_add(self):
        """执行添加操作前，需要获取添加的年级名称和年级ID"""
        gradeid = self.ui.lineEdit.text()
        gradename  = self.ui.lineEdit_2.text()
        if gradeid != '' and gradename != '':
            if self.grade_getName(gradename) > 0:  # 说明要添加的数据在数据库中已经存在
                self.ui.lineEdit_2.setText('')
                QMessageBox.information(self, '提示', '年级名称已经存在！请重新输入！！')
            else:
                resl = service.execute('insert into tb_grade(gradeID,gradeName) values (%s,%s)', (gradeid, gradename))
                if resl > 0:
                    self.grade_query()  # 重新加载表格数据
                    QMessageBox.information(self, '提示', '信息添加成功了！', QMessageBox.Ok)
        else:
            QMessageBox.warning(self,'警告','年级编号或者年级名称不能为空！',QMessageBox.Ok)

    def grade_getItem(self,item):
        """获取选中的表格内容，item代表鼠标点击的那一行"""
        if item.column() == 0:  # 第一列是编号
            self.select = item.text()
            row = item.row()
            self.ui.lineEdit.setText(self.select)   # 将点击获得的年级编个放到输入框中
            self.ui.lineEdit_2.setText(self.ui.tableWidget_3.item(row, 1).text())

    def grade_edit(self,row):
        """用于执行修改操作的函数"""
        try:
            if self.select != '': # 判断年级编号是否有值
                gradeName = self.ui.lineEdit_2.text()
                if gradeName != '': # 如果年级名称也有了，就到数据库中看看是否已经存在数据
                    if self.grade_getName(gradeName) > 0:
                        QMessageBox.information(self,'提示','要修改的年级名称已经存在！',QMessageBox.Ok)
                    else:
                        resl = service.execute('update tb_grade set gradeName=%s where gradeid=%s',(gradeName,self.ui.lineEdit.text()))
                        if resl > 0:
                            self.grade_query()
                            QMessageBox.information(self,'提示',f'第{row}行数据已经修改成功了！',QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, '警告', '年级名称不能为空！', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self,'警告','请选中需要修改的数据！',QMessageBox.Ok)

    def grade_delete_(self,row):
        try:
            if self.select != '':  # 删除年级表中的数据
                res = service.execute('delete from tb_grade where gradeID=%s',(self.ui.lineEdit.text(),))
                if res > 0:
                    self.grade_query()
                    QMessageBox.information(self,'提示',f'第{row}删除成功!',QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self,'警告','请选择要删除的数据!',QMessageBox.Ok)
# 考试类别考试类别考试类别考试类别考试类别考试类别考试类别考试类别考试类别考试类别设置
    def kind_query(self):
        """自定义一个槽函数，作用：在窗体启动时，将数据库中的考试类别信息读取出来。"""
        self.ui.tableWidget_5.setRowCount(0)  # 清空表中的所有行
        # 调用公共类中的公共方法查询
        result = service.query('select * from tb_examkinds;')
        row = len(result)  # 获取到数据的行数
        self.ui.tableWidget_5.setRowCount(row)  # 设置行数
        self.ui.tableWidget_5.setColumnCount(4)  # 应为有2个字段所以要设置2列
        self.ui.tableWidget_5.setHorizontalHeaderLabels(['类别编号', '类别名称','操作1','操作2'])  # 设置表格的标题
        for i in range(row):
            for j in range(2):
                date_single = QTableWidgetItem(str(result[i][j]))  # 将数据处理为表格控件能接受的数据对象
                self.ui.tableWidget_5.setItem(i, j, date_single)  # 将数据依次放入表格中
            # 创建两个按钮
            button1 = QPushButton("修改")
            button2 = QPushButton("删除")
            # 将按钮的点击信号连接到槽函数
            button1.clicked.connect(lambda checked, r=i: self.kind_edit(r))
            button2.clicked.connect(lambda checked, r=i: self.kind_delete_(r))
            # 将按钮添加到表格布局中
            self.ui.tableWidget_5.setCellWidget(i, 2, button1)
            self.ui.tableWidget_5.setCellWidget(i, 3, button2)

    def kind_getName(self,name):     # (name,) 元组类型，其中只有一个函数时就要加一个，。
        """到数据库中查找看是否有 name考试科目 的存在"""
        result = service.query('select * from tb_examkinds where kindName = %s;',(name,))
        return len(result)

    def kind_add(self):
        """执行添加操作前，需要获取添加的考试科目的ID和考试科目的名称"""
        kindid = self.ui.lineEdit_5.text()
        kindname  = self.ui.lineEdit_6.text()
        if kindid != '' and kindname != '':
            if self.kind_getName(kindname) > 0:  # 说明要添加的数据在数据库中已经存在
                self.ui.lineEdit_6.setText('')
                QMessageBox.information(self, '提示', '考试科目已经存在！请重新输入！！')
            else:
                resl = service.execute('insert into tb_examkinds(kindID,kindName) values (%s,%s)', (kindid, kindname))
                if resl > 0:
                    self.kind_query()  # 重新加载表格数据
                    QMessageBox.information(self, '提示', '信息添加成功了！', QMessageBox.Ok)
        else:
            QMessageBox.warning(self,'警告','类别编号或者类别名称不能为空！！',QMessageBox.Ok)

    def kind_getItem(self,item):
        """获取选中的表格内容，item代表鼠标点击的那一行"""
        if item.column() == 0:  # 第一列是编号
            self.select = item.text()
            row = item.row()
            self.ui.lineEdit_5.setText(self.select)
            self.ui.lineEdit_6.setText(self.ui.tableWidget_5.item(row, 1).text())

    def kind_edit(self,row):
        """用于执行修改操作的槽函数"""
        try:
            if self.select != '':
                kindname = self.ui.lineEdit_6.text()
                if kindname != '':
                    if self.kind_getName(kindname) > 0:
                        QMessageBox.warning(self, '警告', '需要修改的类别名称已经存在！！！', QMessageBox.Ok)
                    else:
                        resl = service.execute("update tb_examkinds set kindName=%s where kindID=%s;",
                                               (kindname, self.select))
                        if resl > 0:
                            self.kind_query()
                            QMessageBox.information(self, '提示', f"第{row}科目类别数据修改成功！", QMessageBox.Ok)
                else:
                    QMessageBox.warning(self,'警告','需要修改的类别名称不能为空！！！',QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self,'警告','请选中需要修改的类别编号！！！',QMessageBox.Ok)

    def kind_delete_(self,row):
        try:
            if self.select != '':
                ree = service.execute("delete from tb_examkinds where kindID=%s;",(self.ui.lineEdit_5.text(),))
                if ree > 0:
                    self.kind_query()
                    QMessageBox.information(self,'提示',f'第{row}删除成功！', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self,'警告','请选中需要删除的类别编号！',QMessageBox.Ok)
# 为考试类别考试类别考试类别考试类别实现功能
    def sub_query(self):
        """自定义一个槽函数，作用：在窗体启动时，将数据库中的考试类别信息读取出来。"""
        self.ui.tableWidget_6.setRowCount(0)  # 清空表中的所有行
        # 调用公共类中的公共方法查询
        result = service.query('select * from tb_subject;')
        row = len(result)  # 获取到数据的行数
        self.ui.tableWidget_6.setRowCount(row)  # 设置行数
        self.ui.tableWidget_6.setColumnCount(4)  # 应为有2个字段所以要设置2列
        self.ui.tableWidget_6.setHorizontalHeaderLabels(['科目编号', '科目名称','操作1','操作2'])  # 设置表格的标题
        for i in range(row):
            for j in range(2):
                date_single = QTableWidgetItem(str(result[i][j]))  # 将数据处理为表格控件能接受的数据对象
                self.ui.tableWidget_6.setItem(i, j, date_single)  # 将数据依次放入表格中
            button1 = QPushButton('修改')
            button2 = QPushButton('删除')

            button1.clicked.connect(lambda checked, r=i: self.sub_edit(r))
            button2.clicked.connect(lambda checked, r=i: self.sub_delete_(r))

            self.ui.tableWidget_6.setCellWidget(i, 2, button1)
            self.ui.tableWidget_6.setCellWidget(i, 3, button2)

    def sub_getName(self, name):  # (name,) 元组类型，其中只有一个函数时就要加一个，。
        """到数据库中查找看是否有 name年级名称 的存在"""
        result = service.query('select * from tb_subject where subName = %s;', (name,))
        return len(result)

    def sub_add(self):
        """执行添加操作前，需要获取添加的学科ID和科目名称"""
        subid = self.ui.lineEdit_7.text()
        subname = self.ui.lineEdit_8.text()
        if subid != '' and subname != '':
            if self.sub_getName(subname) > 0:  # 说明要添加的数据在数据库中已经存在
                self.ui.lineEdit_8.setText('')
                QMessageBox.information(self, '提示', '科目名称已经存在！请重新输入！！')
            else:
                resl = service.execute('insert into tb_subject(subID,subName) values (%s,%s)', (subid,subname))
                if resl > 0:
                    self.sub_query()  # 重新加载表格数据
                    QMessageBox.information(self, '提示', '信息添加成功了！', QMessageBox.Ok)
        else:
            QMessageBox.warning(self, '警告', '科目编号或者科目名称不能为空！', QMessageBox.Ok)

    def sub_getItem(self, item):
        """获取选中的表格内容，item代表鼠标点击的那一行"""
        if item.column() == 0:  # 第一列是编号
            self.select = item.text()
            row = item.row()
            self.ui.lineEdit_7.setText(self.select)
            self.ui.lineEdit_8.setText(self.ui.tableWidget_6.item(row,1).text())

    def sub_edit(self,row):
        """用于执行修改操作的函数"""
        try:
            if self.select != '':  # 判断年级编号是否有值
                subjectName = self.ui.lineEdit_8.text()
                if subjectName != '':  # 如果年级名称也有了，就到数据库中看看是否已经存在数据
                    if self.sub_getName(subjectName) > 0:
                        QMessageBox.information(self, '提示', '要修改的科目名称已经存在！', QMessageBox.Ok)
                    else:
                        resl = service.execute('update tb_subject set subName=%s where subId=%s',
                                               (subjectName, self.select))
                        if resl > 0:
                            self.sub_query()
                            QMessageBox.information(self, '提示', f'第{row}行数据已经修改成功了！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, '警告', '科目名称不能为空！', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, '警告', '请选中需要修改的数据！', QMessageBox.Ok)

    def sub_delete_(self,row):
        try:
            if self.select != '':  # 删除年级表中的数据
                res = service.execute('delete from tb_subject where subID=%s', (self.select,))
                if res > 0:
                    self.sub_query()
                    QMessageBox.information(self, '提示', f'第{row}行删除成功!', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, '警告', '请选择要删除的数据!', QMessageBox.Ok)
# 为学生信息学生信息学生信息学生信息学生信息学生信息学生信息
    def bas_re_bindGrade(self):
        """为年级组合框做数据查询，并且需要设置初始化"""
        self.ui.cboGrde_2.addItem("全部")
        result = service.query('select gradeName from tb_grade;')
        for i in result:
            self.ui.cboGrde_2.addItem(i[0])
        self.ui.cboSex.addItem("男")
        self.ui.cboSex.addItem("女")

    def bas_re_bindClass(self):
        """为班级的组合框查询数据，并绑定"""
        self.ui.cboClass_2.clear() # 清空下拉组合中的内容
        self.ui.cboClass_2.addItem("全部")
        all_gradename = self.ui.cboGrde_2.currentText()
        result = service.query('select className from v_classinfo WHERE gradeName = %s;',all_gradename)
        for item in result:
            self.ui.cboClass_2.addItem(item[0])

    def bas_re_query(self):
        """从v_studentInfo中将数据查询出来，并放到表格中"""
        self.ui.tableWidget.setRowCount(0)  # 查询之前需要将表格中现有的数据清空
        grede_name = self.ui.cboGrde_2.currentText() # 获取当前选择的年级名称
        cname = self.ui.cboClass_2.currentText() # 获取当前选中的班级名称

        if grede_name == '全部':
            resul_ = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),sex,age,address,phone FROM v_studentinfo;")
        if grede_name != '全部' and cname == '全部': # 查询指定年级的所有班级里的学生。
            resul_ = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),sex,age,address,phone FROM v_studentinfo where gradeName = %s;",grede_name)
        if grede_name != '全部' and cname != '全部': # 查询指定年级下的指定班级下的所有学生。
            resul_ = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),sex,age,address,phone FROM v_studentinfo where gradeName = %s and className = %s;",grede_name,cname)

        row = len(resul_)
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(['学生编号','学生姓名','班  级','性  别','年  龄','家庭地址','联系电话','操作1','操作2'])
        for i in range(row):
            for j in range(7):
                data = QTableWidgetItem(str(resul_[i][j]))  # 将每一个数据加载成QTableWidgetItem
                self.ui.tableWidget.setItem(i, j, data) # 将数据添加到表格控件中去

            button1 = QPushButton('修改')
            button2 = QPushButton('删除')
            button1.clicked.connect(lambda checked,r=row:self.bas_res_edit(r))
            button2.clicked.connect(lambda checked,r=row:self.bas_res_edit(r))
            self.ui.tableWidget.setCellWidget(i, 7, button1)
            self.ui.tableWidget.setCellWidget(i, 8, button2)

    def bas_re_getName(self,stuId):
        """获取数据stuName依据stuId"""
        result = service.query("SELECT stuName FROM tb_student WHERE stuID = %s;",stuId)
        return len(result)

    def bas_re_add(self):
        """添加数据的槽函数"""
        stuId = self.ui.editStuNum.text()
        stuName = self.ui.editStuName.text()
        sex = self.ui.cboSex.currentText()
        age = self.ui.editStuAge.text()
        address = self.ui.editAddress.text()
        phone = self.ui.editPhone.text()

        if self.ui.cboGrde_2.currentText() != '全部':
            # 根据年级的名称查询当前选择的ID
            result = service.query('SELECT gradeID FROM tb_grade WHERE gradeName = %s;',self.ui.cboGrde_2.currentText())
            if len(result) > 0:
                gradeId = result[0][0]
                if self.ui.cboClass_2.currentText() != '全部':
                    # 根据班级的名称去查询班级的编号（需要考虑年级，原因：不同年级会有相同名字的班级）
                    res = service.query('SELECT classID FROM tb_class WHERE className = %s AND gradeID = %s;',
                                           self.ui.cboClass_2.currentText(),gradeId)  # 这里查到的数据可能是多个
                    if len(res) > 0:
                        classId = res[0][0]
                        # 接下来判断学号和姓名是否为空
                        if stuId != "" and stuName != "":
                            # 判断学生的id是否已经存在于数据库之中
                            if self.bas_re_getName(stuId) > 0:
                                self.ui.editStuNum.setText('')
                                QMessageBox.information(self,'提示','该学生的信息已经存在！请重新输入！！！',QMessageBox.Ok)
                            else:
                                resul = service.execute("INSERT INTO tb_student(stuID,stuName,classID,gradeID,age,sex,phone,address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",(stuId,stuName,classId,gradeId,age,sex,phone,address))
                                if resul > 0:
                                    self.ui.cboGrde_2.setCurrentText("全部")
                                    self.ui.cboClass_2.setCurrentText("全部")
                                    self.ui.editStuAge.clear()
                                    self.ui.editAddress.clear()
                                    self.ui.editPhone.clear()
                                    self.ui.editStuNum.clear()
                                    self.ui.editStuName.clear()
                                    self.bas_re_query()
                                    QMessageBox.information(self,'提示','信息添加成功！',QMessageBox.Ok)
                        else:
                            QMessageBox.warning(self,"警告","学生的学号或姓名不能为空！",QMessageBox.Ok)

                else:
                    QMessageBox.warning(self, '警告', '请选择班级！', QMessageBox.Ok)
        else:
            QMessageBox.warning(self,'警告','请选择年级！',QMessageBox.Ok)

    def bas_re_getItem(self,item:QTableWidgetItem):
        if item.column() == 0:
            self.select = item.text()
            self.ui.editStuName.setText(self.select)

            row = item.row()
            cols = self.ui.tableWidget.columnCount() - 2
            row_data = [self.ui.tableWidget.item(row,col).text() for col in range(cols)]
            self.ui.editStuName.setText(row_data[1])
            self.ui.cboGrde_2.setCurrentText(row_data[2].split(" ")[0])
            self.ui.cboClass_2.setCurrentText(row_data[2].split(" ")[1])
            self.ui.cboSex.setCurrentText(row_data[3])
            self.ui.editStuAge.setText(row_data[4])
            self.ui.editAddress.setText(row_data[5])
            self.ui.editPhone.setText(row_data[6])
            self.ui.editStuNum.setText(row_data[0])

    def bas_re_edit(self,row):
        try:
            if self.select != "":
                stuSex = self.ui.cboSex.currentText()
                stuName = self.ui.editStuName.text()
                stuAge = self.ui.editStuAge.text()
                stuAddress = self.ui.editAddress.text()
                stuPhone = self.ui.editPhone.text()
                print(stuSex,stuName,stuAge,stuAddress,stuPhone)
                resu = service.execute("UPDATE tb_student SET stuName=%s,age=%s,sex=%s,phone=%s,address =%s  WHERE stuID = %s;",
                                (stuName,stuAge,stuSex,stuPhone,stuAddress,self.ui.editStuNum.text()))
                print()
                if resu > 0:
                    self.ui.editStuAge.clear()
                    self.ui.editAddress.clear()
                    self.ui.editPhone.clear()
                    self.ui.editStuNum.clear()
                    self.ui.editStuName.clear()
                    self.bas_re_query()
                    QMessageBox.information(self, '提示', f'第{row}行修改数据成功了！', QMessageBox.Ok)
            else:
                QMessageBox.warning(self, '警告', '请先选择需要修改的数据！！', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self,'警告','请先选择需要修改的数据！！',QMessageBox.Ok)

    def bas_re_delect_(self,row):
        try:
            if self.select != "":
                res = service.query("SELECT * FROM tb_student WHERE stuID = %s;",self.select)
                if len(res) > 0:
                    resu = service.execute("DELETE FROM tb_student WHERE stuID = %s;",(self.select,))
                    if resu > 0:
                        self.ui.editStuName.clear()
                        self.ui.cboGrde_2.setCurrentText("全部")
                        self.ui.cboClass_2.setCurrentText("全部")
                        self.ui.cboSex.setCurrentText("男")
                        self.ui.editStuAge.clear()
                        self.ui.editAddress.clear()
                        self.ui.editPhone.clear()
                        self.ui.editStuNum.clear()
                        self.bas_re_query()
                        QMessageBox.information(self, '提示', f'第{row}行学生信息删除成功!', QMessageBox.Ok)

                else:
                    QMessageBox.information(self,'提示',"该学生信息不存在！或已经被删除了！")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, '警告', '请先选择需要删除的数据！！', QMessageBox.Ok)

#为基础设置result基础设置result基础设置result基础设置result基础设置result
    def bas_resu_bindClass(self):
        """为班级的组合框查询数据，并绑定"""
        self.ui.cboSelectKind_6.clear() # 清空下拉组合中的内容
        self.ui.cboSelectKind_6.addItem("全部")
        result = service.query('select className from v_classInfo WHERE gradeName = %s;',self.ui.cboSelectKind_7.currentText())
        for item in result:
            self.ui.cboSelectKind_6.addItem(item[0])

    def bas_resu_bindGrade(self):
        """为年级组合框做数据查询，并且需要设置初始化"""
        self.ui.cboSelectKind_7.clear()
        self.ui.cboSelectKind_7.addItem("全部")
        result = service.query('select gradeName from tb_grade;')
        for i in result:
            self.ui.cboSelectKind_7.addItem(i[0])

    def bas_resu_bindExamKind(self):
        self.ui.cboSelectKind.addItem("全部")
        result = service.query('select kindName from tb_examkinds;')
        for item in result:
            self.ui.cboSelectKind.addItem(item[0])

    def bas_resu_bindStuName(self):
        self.ui.cboSelectKind_4.clear()  # 清空下拉组合中的内容
        result = service.query("SELECT stuName FROM v_studentinfo WHERE gradeName = %s AND className = %s;",self.ui.cboSelectKind_7.currentText(),self.ui.cboSelectKind_6.currentText())
        for item in result:
            self.ui.cboSelectKind_4.addItem(item[0])

    def bas_resu_bindExamSub(self):
        self.ui.cboSelectKind_5.addItem("全部")
        result = service.query('select subName from tb_subject;')
        for item in result:
            self.ui.cboSelectKind_5.addItem(item[0])

    def bas_resu_query(self):
        """"在数据库中找到v_resultinfo表并且把数据查询出来放到表格控件中"""
        self.ui.tableWidget_2.setRowCount(0)
        # 获取三个值
        kind = self.ui.cboSelectKind.currentText()
        grade = self.ui.cboSelectKind_7.currentText()
        classname = self.ui.cboSelectKind_6.currentText()
        if kind == '全部':
            if grade == '全部':
                if classname == '全部':
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo;")
                    # 查询全部数据
                else:
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE className = %s;",classname)
                    # 根据班级
            else:
                if classname == "全部":
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE gradeName = %s;",grade)
                    # 根据年级
                else:
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE gradeName = %s and className = %s;",grade,classname)
                    # 根据年级和班级
        else:
            if grade == "全部":
                if classname == "全部":
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s;",kind)
                    # 更具考试种类kind
                else:
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s and className;",kind,classname)
                    # 根据考试种类kind和班级
            else:
                if classname == "全部":
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s and gradeName = %s;",kind,grade)
                    # 根据考试的种类kind和年级
                else:
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName = %s and gradeName = %s and className = %s;",kind,grade,classname)
                    # 根据考试的种类kind和年级、班级

        row = len(result)
        self.ui.tableWidget_2.setRowCount(row)
        self.ui.tableWidget_2.setColumnCount(8)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(['学生编号','学生姓名','班级','考试类型','科目名称','成绩','操作1','操作2'])
        for i in range(row):
            for j in range(6):
                data = QTableWidgetItem(str(result[i][j]))
                self.ui.tableWidget_2.setItem(i,j,data)
            button1 = QPushButton('修改')
            button2 = QPushButton('删除')

            button1.clicked.connect(lambda checked, r=i: self.bas_resu_edit(r))
            button2.clicked.connect(lambda checked, r=i: self.bas_resu_delete(r))

            self.ui.tableWidget_2.setCellWidget(i, 6, button1)
            self.ui.tableWidget_2.setCellWidget(i, 7, button2)

    def judge_stu(self,stuid,kindid,subid):
        result = service.query("SELECT * FROM tb_result WHERE stuID = %s AND kindID =%s AND subID =%s;",stuid,kindid,subid)
        if len(result) >0:
            return False
        else:
            return True

    def bas_resu_add(self):
        """判断，并添加"""
        e_kind = self.ui.cboSelectKind.currentText()
        e_grade = self.ui.cboSelectKind_7.currentText()
        e_class = self.ui.cboSelectKind_6.currentText()
        e_sub = self.ui.cboSelectKind_5.currentText()
        e_stuName = self.ui.cboSelectKind_4.currentText()
        e_score = self.ui.editResult_2.text()
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
                                    self.bas_resu_query()
                                    QMessageBox.information(self,"提示","数据添加成功！",QMessageBox.Ok)
                            else:
                                QMessageBox.warning(self, "警告", "该学生成绩已经存在！！！", QMessageBox.Ok)

                        else:
                            QMessageBox.warning(self, "警告", "请先填写分数！！！", QMessageBox.Ok)
                    else:
                        QMessageBox.warning(self, "警告", "请先选择年级和班级！！！", QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, "警告", "请先选择姓名！！！", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "警告", "请先选择考试科目！！！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "警告", "请先选择考试类别！！！", QMessageBox.Ok)

    def bas_resu_getItem(self, item: QTableWidgetItem):
        if item.column() == 0:
            self.select = item.text()
            row = item.row()
            cols = 6
            row_data = [self.ui.tableWidget_2.item(row, col).text() for col in range(cols)]
            self.ui.cboSelectKind_4.setCurrentText(row_data[1])
            self.ui.cboSelectKind_7.setCurrentText(row_data[2].split(" ")[0])
            self.ui.cboSelectKind_6.setCurrentText(row_data[2].split(" ")[1])
            self.ui.cboSelectKind.setCurrentText(row_data[3])
            self.ui.cboSelectKind_5.setCurrentText(row_data[4])
            self.ui.editResult_2.setText('')
            self.k_id = service.query("SELECT kindID FROM tb_examkinds where kindName=%s;", row_data[3])[0][0]
            self.suid = service.query("SELECT subID FROM tb_subject where subName=%s;", row_data[4])[0][0]

    def bas_resu_edit(self,row):
        try:
            if self.select != '':
                score_ = self.ui.editResult_2.text()
                if score_ != '':
                    reu = service.execute(
                        "UPDATE tb_result SET result=%s WHERE stuID = %s AND kindID =%s AND subID =%s",
                        (score_, self.select, self.k_id, self.suid))
                    if reu > 0:
                        self.bas_resu_query()
                        QMessageBox.information(self, "提示", f"第{row}行数据修改成功！！", QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, '警告', '请先填入数据！！', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, '警告', '请先选择需要修改的成绩的学生编号！！', QMessageBox.Ok)

    def bas_resu_delete(self,row):
        try:
            if self.select != '':
                sure_ = QMessageBox.warning(self, '警告', '请确认是否需要删除该学生的成绩！！！学生信息删除后不能恢复！',
                                            QMessageBox.Yes | QMessageBox.Cancel)
                if sure_ == QMessageBox.Yes:
                    resu = service.execute("DELETE FROM tb_result WHERE stuID = %s AND kindID =%s AND subID =%s;",
                                           (self.select, self.k_id, self.suid))
                    if resu > 0:
                        self.ui.editResult_2.clear()
                        self.bas_resu_query()
                        QMessageBox.information(self, '提示', f'第{row}行学生考试成绩信息已被成功删除!', QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, '警告', '请先选择需要删除的数据！！', QMessageBox.Ok)

    def q_query(self):
        self.ui.tableWidget_7.setRowCount(0)  # 清空表格
        key = self.ui.editKey.text()
        if key == "":  # 查询全部的学生信息
            result = service.query("select stuID,stuName,concat(gradeName,' ',className),age,sex,phone,address FROM v_studentinfo;")
        else:
            if self.ui.cboSelect.currentText() == "学生编号":
                result = service.query("select stuID,stuName,concat(gradeName,' ',className),age,sex,phone,address FROM v_studentinfo WHERE stuID LIKE %s;","%"+key+"%")
            else:
                # 根据学生姓名模糊查询
                result = service.query(
                    "select stuID,stuName,concat(gradeName,' ',className),age,sex,phone,address FROM v_studentinfo WHERE stuName LIKE %s;",
                    "%" + key + "%")

        row = len(result)
        self.ui.tableWidget_7.setRowCount(row)
        self.ui.tableWidget_7.setColumnCount(7)
        self.ui.tableWidget_7.setHorizontalHeaderLabels(["学生编号",'学生姓名',"年级","年龄","性别","联系电话","家庭住址"])
        for i in range(row):
            for j in range(7):
                data = QTableWidgetItem(str(result[i][j]))
                self.ui.tableWidget_7.setItem(i, j, data)
        if row > 0:
            QMessageBox.information(self,'提示','数据查询成功！！！',QtWidgets.QMessageBox.Ok)
        else:
            QMessageBox.information(self,'提示','查询的数据为空！！！',QtWidgets.QMessageBox.Ok)

    def q_bindExamKind(self):
        self.ui.comboBox_2.addItem("全部")
        resu = service.query("SELECT kindName FROM tb_examkinds;")
        for i in resu:
            self.ui.comboBox_2.addItem(i[0])

    def q_bindSubject(self):
        self.ui.comboBox_3.addItem("全部")
        resu = service.query("SELECT subName FROM tb_subject;")
        for i in resu:
            self.ui.comboBox_3.addItem(i[0])

    def q_r_query(self):
        self.ui.tableWidget_8.setRowCount(0) # 清空全部行
        stuName = self.ui.lineEdit_9.text()
        examKind = self.ui.comboBox_2.currentText()
        examSubject = self.ui.comboBox_3.currentText()
        if stuName == '':
            if examKind == '全部':
                if examSubject == '全部':  # 查询全部的数据
                    result = service.query(
                        "SELECT stuID,stuName,CONCAT(gradeName,'',className),kindName,subName,result FROM v_resultinfo;")
                else: # 依据考试科目去查询
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE subName = %s;",examSubject)
            else:
                if examSubject == '全部': # 依据考试类型examkinds查询
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE kindName=%s;",examKind)
                else: # yiju考试类型和科目查询
                    result = service.query("SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE subName = %s and kindName=%s;",examSubject,examKind)
        else:  # 当姓不为空值时
            if examKind == '全部':
                if examSubject == '全部': # 依据姓名
                    result = service.query(
                        "SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE stuName = %s;",
                        stuName)
                else: # 依据姓名和考试科目
                    result = service.query(
                        "SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE stuName = %s and subName=%s;",
                        stuName,examSubject)
            else:
                if examSubject == '全部': # 依据姓名和考试类型
                    result = service.query(
                        "SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE stuName = %s and kindName=%s;",
                        stuName, examKind)
                else: # 依据姓名和考试科目和考试类型、
                    result = service.query(
                        "SELECT stuID,stuName,CONCAT(gradeName,' ',className),kindName,subName,result FROM v_resultinfo WHERE stuName = %s and kindName=%s and subName=%s;",
                        stuName, examKind,examSubject)
        row = len(result)
        self.ui.tableWidget_8.setRowCount(row)
        self.ui.tableWidget_8.setColumnCount(6)
        self.ui.tableWidget_8.setHorizontalHeaderLabels(['学生编号','学生姓名','班级','考试类型','科目名称','成绩'])
        for i in range(row):
            for j in range(6):
                data = QTableWidgetItem(str(result[i][j]))
                self.ui.tableWidget_8.setItem(i, j, data)
        if row > 0:
            QMessageBox.information(self,'提示','数据查询成功!',QMessageBox.Ok)
        else:
            QMessageBox.information(self,'提示','没有考试信息！请确认考试信息后重试~',QMessageBox.Ok)

if __name__ == '__main__':
    app  = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())