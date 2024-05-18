import pyodbc
from PyQt5.QtWidgets import QWidget, QMessageBox
from ui.add_page import Ui_Form


class AddPage(QWidget, Ui_Form):
    def __init__(self):
        super(AddPage, self).__init__()
        self.setupUi(self)
        self.init_slot()  # 初始化槽函数

    def init_slot(self):
        self.pushButton.clicked.connect(self.add)

    def add(self):
        teacher_name = self.lineEdit_10.text()
        student_id = self.lineEdit_12.text()
        student_name = self.lineEdit_11.text()
        time = self.lineEdit_6.text()  # 假设这是时间字符串，可能需要转换为datetime对象
        status = self.lineEdit_8.text()  # 获取用户输入的考勤状态
        score = self.lineEdit_9.text()  # 获取用户输入的分数

        # 验证数据完整性
        if not all([teacher_name, student_id, student_name, time, status, score]):
            QMessageBox.warning(self, '添加失败', '有数据未填完整！')
            return

        # 建立数据库连接
        conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=LIDONYANG;'
            r'DATABASE=学生考勤系统;'
            r'UID=sa;'
            r'PWD=120099'
        )
        conn = pyodbc.connect(conn_str)
        try:
            with conn.cursor() as cursor:
                sql_1 = "SELECT attendance_sheet_name, course_id FROM teachers WHERE teacher_name = ?"
                cursor.execute(sql_1, (teacher_name,))
                table_names = cursor.fetchall()
                print(table_names)
                if table_names:
                    table_name = table_names[0][0]
                    course_id = table_names[0][1]
                    print("table_name", table_name)
                    print("course_id", course_id)
                    sql_course_name = "SELECT course_name FROM courses WHERE course_id = ?"
                    cursor.execute(sql_course_name, (course_id,))
                    course_name = cursor.fetchone()
                    print("course_name", course_name)
                    if course_name:
                        course_name = course_name[0]
                        # 构建SQL插入语句，使用参数化查询
                        sql_insert = "INSERT INTO " + table_name + " (student_id, student_name, course_name, time, status, score) VALUES (?, ?, ?, ?, ?, ?)"
                        # 执行插入操作
                        cursor.execute(sql_insert, (student_id,  student_name, course_name, time, status, int(score)))
                        # 提交事务
                        conn.commit()
                        print('考勤信息上传成功')
                        sql_select = "SELECT attendance_score, punctual_number, leave_early_number, absence_number FROM " + student_id + " WHERE course_id = ?"  # 加上空格，确保语句正确
                        cursor.execute(sql_select, (course_id,))
                        attendance_score = cursor.fetchall()
                        print("------------------")
                        print(attendance_score[0][0])
                        if attendance_score:
                            attendance_scores = int(attendance_score[0][0])  # 获取考勤总分
                            punctual_number = int(attendance_score[0][1])  # 获取准时的次数
                            leave_early_number = int(attendance_score[0][2])  # 获取早退的次数
                            absence_number = int(attendance_score[0][3])  # 获取缺勤的次数

                            if status == "准时":
                                print('准时')
                                punctual_number = int(punctual_number) + 1  # 准时次数加一
                                attendance_scores = int(attendance_scores) + 5  # 考勤分数加5
                                sql_update = "UPDATE " + student_id + " SET punctual_number = ?, attendance_score = ? WHERE course_id = ?"
                                cursor.execute(sql_update, (punctual_number, attendance_scores, course_id))
                                conn.commit()
                                # 提示用户更新成功
                                QMessageBox.information(self, '更新成功', '数据更新成功')

                                # print('准时')
                                # punctual_number = int(punctual_number) + 1  # 准时次数加一
                                # attendance_scores = int(attendance_scores) + 5  # 考勤分数加5
                                # sql_update = "UPDATE SET " + student_id + " punctual_number = ?, attendance_score = ? WHERE course_id = ?"
                                # cursor.execute(sql_update, (punctual_number, attendance_scores))
                                # conn.commit()
                                # # 提示用户更新成功
                                # QMessageBox.information(self, '添加成功', '数据添加成功')
                            elif status == "早退":
                                print('早退')
                                leave_early_number = int(leave_early_number) + 1  # 早退次数加一
                                attendance_scores = int(attendance_scores) + 3 # 考勤分数加3
                                sql_update = "UPDATE " + student_id + " SET leave_early_number = ?, attendance_score = ? WHERE course_id = ?"
                                cursor.execute(sql_update, (leave_early_number, attendance_scores, course_id))
                                conn.commit()
                                # 提示用户更新成功
                                QMessageBox.information(self, '添加成功', '数据添加成功')
                            elif status == "缺勤":
                                print('缺勤')
                                absence_number = int(absence_number) + 1  # 早退次数加一
                                attendance_scores = int(attendance_scores) + 0  # 考勤分数加3
                                sql_update = "UPDATE " + student_id + " SET absence_number = ?, attendance_score = ? WHERE course_id = ?"
                                cursor.execute(sql_update, (absence_number, attendance_scores, course_id))
                                conn.commit()
                                # 提示用户更新成功
                                QMessageBox.information(self, '添加成功', '数据添加成功')
                        else:
                            print('遇到网络问题，数据回滚')
                            conn.rollback()
        except pyodbc.Error as e:
            # 错误处理
            conn.rollback()
            QMessageBox.warning(self, '添加失败', '数据添加失败：' + str(e))
        finally:
            # 关闭数据库连接
            conn.close()

