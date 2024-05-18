from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHBoxLayout, QWidget, QSplitter, \
    QVBoxLayout, QHeaderView
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import random
from PyQt5.QtGui import QColor


class Window(QMainWindow):
    def __init__(self, user_name, course_name, punctual_number, leave_early_number, absence_number, attendance_score, teacher_name):
        super().__init__()
        self.setWindowTitle("学生考勤可视化界面")
        self.setGeometry(100, 100, 1080, 640)
        self.teacher_name = teacher_name
        self.user_name = user_name  # 用户名字
        self.course_name = course_name  # 获取教师名字
        self.punctual_number = punctual_number  # 准时次数
        self.leave_early_number = leave_early_number  # 早退次数
        self.absence_number = absence_number  # 缺勤次数
        self.attendance_score = attendance_score  # 考勤分

        self.create_piechart()
        self.create_tableview()
        self.layout_widgets()
        self.show()

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = QColor(r, g, b)
        return color

    def create_piechart(self):
        self.series = QPieSeries()
        total = int(self.punctual_number) + int(self.absence_number) + int(self.leave_early_number)
        pun = (self.punctual_number / total) * 100
        abs = (self.absence_number / total) * 100
        lea = (self.leave_early_number / total) * 100
        print(pun)
        print(abs)
        print(lea)
        self.series.append("准时次数占比{}%".format(str(pun)[:4]), pun)
        self.series.append("早退次数占比{}%".format(str(lea)[:4]), lea)
        self.series.append("缺勤次数占比{}%".format(str(abs)[:4]), abs)
        # adding slice
        self.lice0 = QPieSlice()
        self.slice0 = self.series.slices()[0]
        self.slice0.setLabelVisible(True)
        self.slice0.setBrush(self.get_random_color())
        self.slice1 = QPieSlice()
        self.slice1 = self.series.slices()[1]
        self.slice1.setLabelVisible(True)
        self.slice0.setBrush(self.get_random_color())
        self.slice2 = QPieSlice()
        self.slice2 = self.series.slices()[2]
        self.slice2.setLabelVisible(True)
        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("{}的{}具体考勤情况".format(str(self.user_name), str(self.course_name)))
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        # self.setCentralWidget(self.chartview)

    def create_tableview(self):
        self.table = QTableWidget(2, 7)  # 创建一个3行2列的表格
        self.table.setHorizontalHeaderLabels(['学生名称', '课程名称', '教师名称', '准时次数', '早退次数', '缺勤次数', '考勤总分'])  # 设置表头
        self.table.setItem(1, 0, QTableWidgetItem(str(self.user_name)))
        self.table.setItem(1, 1, QTableWidgetItem(str(self.course_name)))
        self.table.setItem(1, 2, QTableWidgetItem(str(self.teacher_name)))
        self.table.setItem(1, 3, QTableWidgetItem(str(self.punctual_number)))
        self.table.setItem(1, 4, QTableWidgetItem(str(self.leave_early_number)))
        self.table.setItem(1, 5, QTableWidgetItem(str(self.absence_number)))
        self.table.setItem(1, 6, QTableWidgetItem(str(self.attendance_score)))
        self.table.resizeColumnsToContents()  # 根据内容调整列宽
        self.table.resizeRowsToContents()  # 根据内容调整行高

    def layout_widgets(self):
        # self.hbox = QHBoxLayout()
        # # 创建分割器
        # self.splitter = QSplitter(Qt.Horizontal)
        # # 将图表视图添加到分割器中
        # self.splitter.addWidget(self.chartview)
        # # 将表格视图添加到分割器中
        # self.splitter.addWidget(self.table)
        # # 设置分割器的初始大小比例为2:1
        # self.splitter.setSizes([200, 100])
        # # 将分割器添加到水平布局中
        # self.hbox.addWidget(self.splitter)
        # # 创建中心部件并设置布局
        # self.central_widget = QWidget()
        # self.central_widget.setLayout(self.hbox)
        # # 设置中心部件
        # self.setCentralWidget(self.central_widget)
        # 创建垂直布局
        # 创建垂直布局
        self.vbox = QVBoxLayout()

        # 创建分割器
        self.splitter = QSplitter(Qt.Vertical)

        # 将图表视图添加到分割器中
        self.splitter.addWidget(self.chartview)

        # 将表格视图添加到分割器中
        self.splitter.addWidget(self.table)

        # 设置分割器的初始大小比例为2:1
        self.splitter.setSizes([500, 100])

        # 将分割器添加到垂直布局中
        self.vbox.addWidget(self.splitter)

        # 创建中心部件并设置布局
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.vbox)

        # 设置中心部件
        self.setCentralWidget(self.central_widget)

        # 设置表格视图的水平表头拉伸模式为自适应
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
