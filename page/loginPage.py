import pyodbc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox

from page.managerPage import ManagerPage
from ui.login_page import Ui_Form


class LoginPage(QWidget, Ui_Form):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)
        self.init_slot()  # 初始化槽函数

    def init_slot(self):
        self.pushButton.clicked.connect(self.login)

    def login(self):
        user_id = self.idlineEdit.text()  # 获取用户输入的id
        user_pwd = self.pwdlineEdit.text()  # H 获取用户输入的密码
        if not user_id or not user_pwd:
            print('请输入完整的用户信息')
            QMessageBox.warning(self, '信息不全', '请输入完整的用户信息！')
            return

            # 连接到本地的SQL Server数据库
        print('开始登录')
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LIDONYANG;DATABASE=学生考勤系统;UID=sa;PWD=120099')
        cursor = conn.cursor()

        # 查询数据库中是否存在匹配的用户
        cursor.execute("SELECT * FROM teachers WHERE teacher_id = ? AND pwd = ?", (user_id, user_pwd))
        row = cursor.fetchone()

        if row:
            print('登录成功')
            QMessageBox.information(self, '登录成功', '登录成功！')
            self.page = ManagerPage()
            self.page.show()
            self.hide()
            conn.close()
            return
        else:
            print('登录失败')
            QMessageBox.warning(self, '登录失败', '用户名或密码错误！')

        conn.close()
