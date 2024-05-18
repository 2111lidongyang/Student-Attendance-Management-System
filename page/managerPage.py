import pyodbc
from PyQt5.QtChart import QBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView, QBarSet
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPainter
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView, QVBoxLayout

from page.addPage import AddPage
from page.visualizationPage import Window
from ui.manager_page import Ui_Form
import pandas as pd


class ManagerPage(QWidget, Ui_Form):
    def __init__(self):
        super(ManagerPage, self).__init__()
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.tableView_2.setModel(self.model)
        self.init_students()
        self.table_name = ''
        self.init_slot()

    def init_slot(self):
        self.pushButton.clicked.connect(self.find)  # 学生基本信息查询槽函数
        self.pushButton_2.clicked.connect(self.output)  # 学生基本信息查询槽函数
        self.pushButton_3.clicked.connect(self.find_addent)  # 学生考勤查询槽函数
        self.pushButton_4.clicked.connect(self.del_addent)  # 学生考勤删除槽函数
        self.pushButton_5.clicked.connect(self.fix_addent)  # 学生考勤修改槽函数
        self.pushButton_6.clicked.connect(self.add_addent)  # 学生考勤增加槽函数
        self.pushButton_7.clicked.connect(self.out_ksh)  # 学生考勤平时分导出槽函数
        self.pushButton_8.clicked.connect(self.find_ksh)  # 学生考勤平时分数据导出

    def init_students(self):
        print('开始查询学生数据')
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
        cursor = conn.cursor()
        cursor.execute("SELECT student_id, student_name, college, class FROM students")
        row = cursor.fetchall()
        if row:
            print(row)
            # 创建模型
            model = QStandardItemModel(len(row), 4)  # 几行几列数据
            model.setHorizontalHeaderLabels(['学号', '姓名', '学院', '专业/班级'])
            # 将数据填充到模型中
            for row_index, row_data in enumerate(row):
                for col_index, data in enumerate(row_data):
                    print("col_index", col_index)
                    print("data", data)
                    # for col_index, data in enumerate(row_data):
                    item = QStandardItem(str(data).strip())  # 使用strip()去除可能存在的空白字符
                    model.setItem(row_index, col_index, item)
                # 假设您有一个QTableView的实例叫做self.tableView
            self.tableView.setModel(model)
            # 为了使表格视图适应其内容，可以调整列宽
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            print('无该用户信息')
            QMessageBox.warning(self, '登录失败', '无该用户信息！')

    def out_ksh(self):
        course_id = self.lineEdit_3.text()  # 获取用户输入的查询id
        student_id = self.lineEdit_2.text()  # 获取用户输入的查询id
        if student_id and course_id:
            print('开始导出考勤平时分数据')
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT attendance_sheet_name FROM teachers WHERE course_id = ?",
                               (course_id,))
                rows = cursor.fetchall()

                # 如果没有查询到数据，则不进行操作
                if not rows:
                    print("No data found for the given student ID.")
                    # 可以选择在这里做一些错误处理或提示用户
                else:
                    print(rows[0][0])
                    attendance_sheet_name = rows[0][0]
                    print('找到该学生的考勤平时分数据')
                    # cursor.execute("SELECT attendance_id, fkstudent_id, attendance_course, time, status, regular_grade "
                    #                "FROM attendance WHERE fkstudent_id = ?", (user_id,))
                    # 执行查询
                    sql_finv = "SELECT student_id, student_name, course_name, time, status, score FROM {} WHERE student_id = ?".format(str(attendance_sheet_name))
                    cursor.execute(sql_finv, (student_id, ))
                    rows = cursor.fetchall()
                    print(type(rows))

                    # 如果没有查询到数据，则不进行操作
                    if not rows:
                        print("没有找到该学生的考勤平时分数据。")
                        QMessageBox.warning(self, '修改失败', '有数据未填完整！')
                    else:
                        data = []
                        for row in rows:
                            data.append(list(row))

                        columns = ['attendance_id', 'fkstudent_id', 'attendance_course', 'formatted_time', 'status',
                                   'regular_grade']  # 你需要为每列数据提供一个合适的列名
                        df = pd.DataFrame(data, columns=columns)

                        # 将DataFrame导出为CSV文件
                        output_filename = 'output_data.csv'  # 你希望保存的CSV文件名
                        df.to_csv(output_filename, index=False,
                                  encoding='utf-8-sig')  # index=False表示不导出行索引，encoding='utf-8-sig'确保在Excel中正确显示中文

                        print(f'数据已导出到文件：{output_filename}')
                        QMessageBox.information(self, '数据导出成功', f'数据已导出到文件：{output_filename}')
            finally:
                cursor.close()
                conn.close()

        else:
            print('请你输入你要导出数据的id')
            QMessageBox.information(self, '数据导出失败', '请你输入你要导出数据的id')

    def find_ksh(self):
        print('开始数据开始------------')
        course_id = self.lineEdit_3.text()  # 获取用户输入的查询id
        student_id = self.lineEdit_2.text()  # 获取用户输入的查询id
        if course_id and student_id:
            print('开始查询考勤平时分数据')
            try:

                conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
                cursor = conn.cursor()
                sql_ksh = "SELECT teacher_name, punctual_number, leave_early_number, absence_number, attendance_score FROM {} WHERE course_id = ?".format(str(student_id))
                cursor.execute(sql_ksh, (course_id,))
                rows = cursor.fetchall()
                # 如果没有查询到数据，则不进行操作
                if not rows:
                    print("No data found for the given student ID.")
                    # 可以选择在这里做一些错误处理或提示用户
                else:
                    print('rows', rows)
                    teacher_name = rows[0][0]  # 获取教师名字
                    punctual_number = rows[0][1]  # 准时次数
                    leave_early_number = rows[0][2]  # 早退次数
                    absence_number = rows[0][3]  # 缺勤次数
                    attendance_score = rows[0][4]  # 考勤分
                    sql_find_student = "SELECT student_name FROM students WHERE student_id = ?"
                    cursor.execute(sql_find_student, (student_id,))
                    user_names = cursor.fetchone()
                    print(user_names)
                    if user_names:
                        print(user_names)
                        user_name = user_names[0]  # 获取用户的名称
                        sql_course_name = "SELECT course_name FROM courses WHERE course_id = ?"
                        cursor.execute(sql_course_name, (course_id, ))
                        course_names = cursor.fetchone()
                        if course_names:
                            print(course_names)
                            # print('course_id', course_names[0])
                            course_name = course_names[0]  # 获取用户的课程名字
                            self.page = Window(user_name=user_name, course_name=course_name, punctual_number=punctual_number, absence_number=absence_number, attendance_score=attendance_score, leave_early_number=leave_early_number, teacher_name=teacher_name)
                            self.page.show()
                        else:
                            print('该课程不存在')
                            QMessageBox.warning(self, '查看失败', '无该课程信息！')
                    else:
                        print('用户不存在')
                        QMessageBox.warning(self, '查看失败', '无该用户信息！')
            except BaseException as e:
                pass
        else:
            print('请输入完整的数据信息')
            QMessageBox.warning(self, '查看失败', '无该用户信息！')






    def find(self):
        user_id = self.lineEdit.text()  # 获取用户输入的学生id
        if not user_id:
            print('请输入要查询的学生id')
            QMessageBox.critical(self, "信息不全", "请输入要查询的学生id")
            return
        print('开始查询学生数据')
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤管理系统数据库;UID=sa;PWD=120099')
        cursor = conn.cursor()
        cursor.execute("SELECT student_id, student_name, college, class FROM students WHERE student_id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            # 创建模型
            model = QStandardItemModel(1, 1)  # 几行几列数据
            model.setHorizontalHeaderLabels(['学号', '姓名', '学院', '专业/班级'])
            # 将数据填充到模型中
            for row_index, row_data in enumerate(row):
                print("row_index", row_index)
                print("row_data", row_data)
                # for col_index, data in enumerate(row_data):
                item = QStandardItem(str(row_data).strip())  # 使用strip()去除可能存在的空白字符
                model.setItem(0, row_index, item)
                # 假设您有一个QTableView的实例叫做self.tableView
            self.tableView.setModel(model)
            # 为了使表格视图适应其内容，可以调整列宽
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            print('无该用户信息')
            QMessageBox.warning(self, '登录失败', '无该用户信息！')

    def output(self):
        user_id = self.lineEdit.text()  # 获取用户输入的学生id
        if not user_id:
            print('请输入要查询的学生id')
            QMessageBox.critical(self, "信息不全", "请输入要查询的学生id")
            return
        print('开始查询学生数据')
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤管理系统;UID=sa;PWD=120099')
        cursor = conn.cursor()

        cursor.execute("SELECT student_id, name, college, major FROM student WHERE student_id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            # 创建模型
            model = QStandardItemModel(1, 1)
            model.setHorizontalHeaderLabels(['学号', '姓名', '学院', '专业/班级'])
            #
            # # 将数据填充到模型中
            # for row_index, row_data in enumerate(all_res):
            #     for col_index, data in enumerate(row_data):
            #         item = QStandardItem(str(data).strip())  # 使用strip()去除可能存在的空白字符
            #         model.setItem(row_index, col_index, item)

            for row_index, row_data in enumerate(row):
                item = QStandardItem(str(row_data).strip())  # 使用strip()去除可能存在的空白字符
                model.setItem(1, row_index, item)
            # 假设您有一个QTableView的实例叫做self.tableView
            self.tableView.setModel(model)
            # 为了使表格视图适应其内容，可以调整列宽
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            # 提取QStandardItemModel中的数据
            data = []
            for row in range(model.rowCount()):
                row_data = []
                for col in range(model.columnCount()):
                    item = model.item(row, col)
                    row_data.append(item.text() if item is not None else '')
                data.append(row_data)

                # 提取列标题
            column_labels = [model.horizontalHeaderItem(i).text() for i in range(model.columnCount())]

            # 将数据转换为pandas DataFrame
            df = pd.DataFrame(data, columns=column_labels)

            # 导出到CSV文件
            df.to_csv('table_data.csv', index=False, encoding='utf-8-sig')
            QMessageBox.information(self, '数据导出', '学生数据导出成功，保存地址：{}！'.format('table_data.csv'))
        else:
            print('无该用户信息')
            QMessageBox.warning(self, '登录失败', '无该用户信息！')
        conn.close()

    def find_addent(self):
        user_id = self.lineEdit_2.text()  # 获取用户输入的学生id
        course_id = self.lineEdit_3.text()  # 获取用户输入的课程id
        if not user_id:
            print('请输入要查询的学生id')
            QMessageBox.critical(self, "信息不全", "请输入要查询的学生id")
            return
        if not course_id:
            print('开始查询学生考勤数据')
            conn = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
            cursor = conn.cursor()

            query = "SELECT * FROM " + str(user_id)  # 在"FROM"和表名之间添加空格
            cursor.execute(query)
            rows = cursor.fetchall()
            # 如果没有查询到数据，则不进行操作
            if not rows:
                print("No data found for the given student ID.")
                # 可以选择在这里做一些错误处理或提示用户
                QMessageBox.warning(self, '查询失败', '该用户存在')
            else:
                # 创建模型
                self.model = QStandardItemModel(1, 1)  # 几行几列数据
                self.model.setHorizontalHeaderLabels(['课程编号', '教师名称', '准时次数', '早退次数', '缺勤次数', '考勤总分', '课程考勤表'])
                # 将数据填充到模型中
                for row_index, row_data in enumerate(rows):
                    print("row_index", row_index)
                    print("row_data", row_data)
                    for col_index, data in enumerate(row_data):
                        item = QStandardItem(str(data).strip())  # 使用strip()去除可能存在的空白字符
                        self.model.setItem(row_index, col_index, item)
                    # 假设您有一个QTableView的实例叫做self.tableView
                self.tableView_2.setModel(self.model)
                # 为了使表格视图适应其内容，可以调整列宽
                self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                # # 创建一个QStandardItemModel
                # model = QStandardItemModel()
                # self.model.clear()
                # # 设置列标题
                # column_names = [description[0] for description in cursor.description]
                # self.model.setHorizontalHeaderLabels(column_names)
                #
                # # 将查询结果填充到模型中
                # for row_data in rows:
                #     items = [QStandardItem(str(value)) for value in row_data]
                #     self.model.appendRow(items)
                #
                #     # 将模型设置为tableView_2的模型
                # self.tableView_2.setModel(self.model)
                #
                # # 为了使表格视图适应其内容，可以调整列宽
                # self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if course_id:
            print('开始查询该学生考勤记录')
            conn = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
            cursor = conn.cursor()
            cursor.execute("SELECT attendance_sheet_name FROM teachers WHERE course_id = ?", (course_id,))
            rows = cursor.fetchone()

            # 如果没有查询到数据，则不进行操作
            if not rows:
                print("No data found for the given student ID.")
                QMessageBox.warning(self, '查询失败', '用户不存在')
                # 可以选择在这里做一些错误处理或提示用户
            else:
                attendance_sheet_name = str(rows[0])
                print(attendance_sheet_name)
                self.table_name = attendance_sheet_name.rstrip()  # 获取用户的考勤表名，用于删除、修改考勤信息
                query = "SELECT student_id, time, student_name, status, score FROM " + attendance_sheet_name
                try:
                    cursor.execute(query)

                    rows = cursor.fetchall()
                    my_list = []
                    for row in rows:
                        print('user_id:', row[0])
                        print('my_user_id', user_id)
                        if str(row[0]).rstrip() == str(user_id):
                            my_list.append(row)
                    print(my_list)
                    # 创建模型
                    self.model_2 = QStandardItemModel(1, 1)  # 几行几列数据
                    self.model_2.setHorizontalHeaderLabels(['学号', '日期', '姓名', '考勤状态', '考勤分数'])
                    # 将数据填充到模型中
                    for row_index, row_data in enumerate(my_list):
                        print("row_index", row_index)
                        print("row_data", row_data)
                        for col_index, data in enumerate(row_data):
                            item = QStandardItem(str(data).strip())  # 使用strip()去除可能存在的空白字符
                            self.model_2.setItem(row_index, col_index, item)
                        # 假设您有一个QTableView的实例叫做self.tableView
                    self.tableView_2.setModel(self.model_2)
                    # 为了使表格视图适应其内容，可以调整列宽
                    self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                except BaseException as e:
                    print('无该课程数据')
                    self.table_name = ""
                    QMessageBox.warning(self, '查询失败', '无该课程数据')

    def del_addent(self):
        # 获取选中的行索引
        print('开设删除数据')
        selected_indexes = self.tableView_2.selectionModel().selectedRows()
        if selected_indexes:
            # 获取第一个选中的行索引
            row_index = selected_indexes[0]
            print(row_index)
            row_number = row_index.row()
            print(row_number)
            # 获取这一行的第二列内容
            # 注意：索引是从0开始的，所以第二列的索引是1
            item = self.model_2.item(row_number, 0)  # 修改为第二列的索引
            item_time = self.model_2.item(row_number, 1)  # 修改为第四列的索引
            item_status = self.model_2.item(row_number, 3)  # 修改为第四列的索引
            # 提取值
            print(item)
            print(item_status)
            print(item_status)
            if item is not None and item_status is not None and item_status is not None:
                value_to_delete = item.text()  # 获取学号
                print('学号：', len(value_to_delete))
                print('学号：', value_to_delete)
                value_to_time = item_time.text()  # 获取日期
                print('日期：', len(value_to_time))
                print('日期：', value_to_time)
                value_to_status = item_status.text()  # 获取状态
                print('状态：', value_to_status)
                print('状态：', value_to_status)
                # 建立数据库连接
                conn = pyodbc.connect(
                    'DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
                cursor = conn.cursor()
                try:
                    # 构建SQL删除语句
                    # 根据实际情况调整下面的SQL语句，确保fkstudent_id是你要匹配的正确字段
                    sql_attendance = "DELETE FROM " + self.table_name + " WHERE student_id = ? AND time = ?"

                    # 执行删除操作
                    # 注意：对于pyodbc，需要为每个占位符提供一个参数值
                    cursor.execute(sql_attendance, (value_to_delete, value_to_time))

                    # 提交事务
                    conn.commit()
                    # 构建SQL查询语句
                    sql_select = "SELECT attendance_score, punctual_number, leave_early_number, absence_number FROM " + value_to_delete + " WHERE attendance_table_name = ?"  # 加上空格，确保语句正确
                    cursor.execute(sql_select, (self.table_name,))
                    attendance_score = cursor.fetchall()
                    print('开始查询数据')
                    if attendance_score:
                        score = str(attendance_score[0][0]).rstrip()  # 获取用户的考勤分数
                        punctual_number = str(attendance_score[0][1]).rstrip()  # 获取用户准时次数
                        leave_early_number = str(attendance_score[0][2]).rstrip()  # 获取用户早退次数
                        absence_number = str(attendance_score[0][3]).rstrip()  # 获取用户缺勤次数

                        if str(value_to_status).rstrip() == "准时":
                            print('准时')
                            score = str(int(score) - 5)
                            punctual_number = str(int(punctual_number) - 1)
                            sql_update = "UPDATE " + value_to_delete + " SET punctual_number = ?, attendance_score = ? WHERE attendance_table_name = ?"  # 加上空格，确保语句正确
                            cursor.execute(sql_update, (punctual_number, score, self.table_name))
                            conn.commit()
                            print('数据更新成功')
                            self.model_2.removeRow(row_number)
                            QMessageBox.information(self, '删除成功', '数据删除成功')

                        elif str(value_to_status).rstrip() == "早退":
                            print('早退')
                            score = str(int(score) - 3)
                            leave_early_number = str(int(leave_early_number) - 1)
                            sql_update = "UPDATE " + value_to_delete + " SET punctual_number = ?, attendance_score = ? WHERE attendance_table_name = ?"  # 加上空格，确保语句正确
                            cursor.execute(sql_update, (leave_early_number, score, self.table_name))
                            conn.commit()
                            self.model_2.removeRow(row_number)
                            QMessageBox.information(self, '删除成功', '数据删除成功')

                        elif str(value_to_status).rstrip() == "缺勤":
                            print('缺勤')
                            score = str(int(score) - 0)
                            absence_number = str(int(absence_number) - 1)
                            sql_update = "UPDATE " + value_to_delete + " SET punctual_number = ?, attendance_score = ? WHERE attendance_table_name = ?"  # 加上空格，确保语句正确
                            cursor.execute(sql_update, (absence_number, score, self.table_name))
                            conn.commit()
                            self.model_2.removeRow(row_number)
                            QMessageBox.information(self, '删除成功', '数据删除成功')
                    else:
                        QMessageBox.warning(self, '删除失败', '出现未知错误，请重试！！！')
                except pyodbc.Error as e:
                    # 错误处理
                    print("数据删除失败:", e)
                    QMessageBox.warning(self, '删除失败', '数据删除失败')
                finally:
                    # 关闭数据库连接
                    cursor.close()
                    conn.close()
            else:
                print("无数据")
                QMessageBox.warning(self, '删除失败', '无数据')
        else:
            print("没有选中任何行。")
            QMessageBox.warning(self, '删除失败', '没有选中任何行！')

    def add_addent(self):
        self.page = AddPage()
        self.page.show()

    def fix_addent(self):
        selected_indexes = self.tableView_2.selectionModel().selectedRows()
        selected_rows = [index.row() for index in selected_indexes]
        print("selected_rows", selected_rows)

        # print("selected_indexes",selected_indexes)
        if selected_indexes:
            # 获取第一个选中的行索引
            row_index = selected_indexes[0]
            row_number = row_index.row()

            # 获取这一行的第二列内容
            # 注意：索引是从0开始的，所以第二列的索引是1
            item1 = self.model_2.item(row_number, 0)
            item2 = self.model_2.item(row_number, 1)
            item3 = self.model_2.item(row_number, 2)
            item4 = self.model_2.item(row_number, 3)
            item5 = self.model_2.item(row_number, 4)
            #
            # if item1 and item2 and item3 and item4 and item5:
            # 提取值
            student_id = self.lineEdit_2.text()  # 获取用户输入的student_id
            course_id = self.lineEdit_3.text()  # 获取用户输入的课程id
            # 建立数据库连接
            time = item2.text()  # 获取用户的课程id
            student_name = item3.text()  # 获取用户输入的教师名字
            status = item4.text()  # 获取用户输入的早退次数
            score = item5.text()  # 获取用户输入的缺勤次数
            conn = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
            cursor = conn.cursor()
            sql_find = "SELECT attendance_table_name FROM {} WHERE course_id = ?".format(student_id)

            print("开始查询表名")
            try:
                cursor.execute(sql_find, (course_id,))
                # 这里继续处理查询结果
                attendance_table_name = cursor.fetchone()
                if attendance_table_name:
                    print('attendance_table_name', attendance_table_name[0])
                    attendance_table_name = attendance_table_name[0]

                    # 构建SQL更新语句
                    sql_update = "UPDATE {} SET status = ?, score = ? WHERE student_id = ? AND time = ?".format(
                        attendance_table_name)

                    # 执行更新操作
                    # 注意：参数顺序应与SQL语句中的问号顺序一致
                    cursor.execute(sql_update, (
                        status,
                        score,
                        student_id,
                        time
                    ))

                    # 提交事务
                    conn.commit()
                    sql_find = "SELECT punctual_number, leave_early_number, absence_number, attendance_score FROM {} WHERE course_id = ?".format(
                        str(student_id))
                    cursor.execute(sql_find, (course_id))
                    datas = cursor.fetchall()
                    print('datas', datas)
                    if datas:
                        punctual_number = int(datas[0][0])
                        leave_early_number = int(datas[0][1])
                        absence_number = int(datas[0][2])
                        attendance_score = int(datas[0][3])
                    if str(status) == "准时":
                        print('准时')
                        punctual_number = int(punctual_number + 1)
                        if type(int(attendance_score) / 5) == type(int):
                            attendance_score = int(attendance_score) + 5
                            sql_update_score = "UPDATE {} SET punctual_number = ?, attendance_score = ? WHERE course_id = ?".format(
                                str(student_id))
                            cursor.execute(sql_update_score, (punctual_number, attendance_score, course_id))
                            conn.commit()
                            print('数据更新成功')
                            # 提示用户更新成功
                            QMessageBox.information(self, '更新成功', '数据更新成功')
                            # 如果需要，更新模型中的显示（这里可能需要您自定义逻辑来刷新模型视图）
                        else:
                            attendance_score = int(attendance_score) + 2
                            sql_update_score = "UPDATE {} SET punctual_number = ?, attendance_score = ? WHERE course_id = ?".format(
                                str(student_id))
                            cursor.execute(sql_update_score, (punctual_number, attendance_score, course_id))
                            conn.commit()
                            print('数据更新成功')
                            # 提示用户更新成功
                            QMessageBox.information(self, '更新成功', '数据更新成功')
                            # 如果需要，更新模型中的显示（这里可能需要您自定义逻辑来刷新模型视图）
                    elif str(status) == "早退":
                        leave_early_number = int(leave_early_number + 1)
                        if type(int(attendance_score) / 5) == type(int):
                            attendance_score = int(attendance_score) + 3
                            sql_update_score = "UPDATE {} SET leave_early_number = ?, attendance_score = ? WHERE course_id = ?".format(
                                str(student_id))
                            cursor.execute(sql_update_score, (leave_early_number, attendance_score, course_id))
                            conn.commit()
                            print('数据更新成功')
                            # 提示用户更新成功
                            QMessageBox.information(self, '更新成功', '数据更新成功')
                            # 如果需要，更新模型中的显示（这里可能需要您自定义逻辑来刷新模型视图）
                        else:
                            attendance_score = int(attendance_score) + 0
                            sql_update_score = "UPDATE {} SET leave_early_number = ?, attendance_score = ? WHERE course_id = ?".format(
                                str(student_id))
                            cursor.execute(sql_update_score, (leave_early_number, attendance_score, course_id))
                            conn.commit()
                            print('数据更新成功')
                            # 提示用户更新成功
                            QMessageBox.information(self, '更新成功', '数据更新成功')
                            # 如果需要，更新模型中的显示（这里可能需要您自定义逻辑来刷新模型视图）
                    elif str(status) == "缺勤":
                        print('缺勤')
                        absence_number = int(absence_number + 1)
                        if type(int(attendance_score) / 5) == type(int):
                            attendance_score = int(attendance_score) - 5
                            sql_update_score = "UPDATE {} SET absence_number = ?, attendance_score = ? WHERE course_id = ?".format(
                                str(student_id))
                            cursor.execute(sql_update_score, (absence_number, attendance_score, course_id))
                            conn.commit()
                            print('数据更新成功')
                            # 提示用户更新成功
                            QMessageBox.information(self, '更新成功', '数据更新成功')
                            # 如果需要，更新模型中的显示（这里可能需要您自定义逻辑来刷新模型视图）
                        else:
                            attendance_score = int(attendance_score) + 0
                            sql_update_score = "UPDATE {} SET absence_number = ?, attendance_score = ? WHERE course_id = ?".format(
                                str(student_id))
                            cursor.execute(sql_update_score, (absence_number, attendance_score, course_id))
                            conn.commit()
                            print('数据更新成功')
                            # 提示用户更新成功
                            QMessageBox.information(self, '更新成功', '数据更新成功')
                            # 如果需要，更新模型中的显示（这里可能需要您自定义逻辑来刷新模型视图）
            except pyodbc.Error as e:
                # 错误处理
                print("数据更新失败:", e)
                QMessageBox.warning(self, '更新失败', '数据更新失败：' + str(e))
            finally:
                # 关闭数据库连接
                cursor.close()
                conn.close()
            # else:
            #     print('有数据未填完整')
            #     QMessageBox.warning(self, '修改失败', '有数据未填完整！')
        else:
            print('未选中行')
            QMessageBox.warning(self, '修改失败', '未选中行！')
