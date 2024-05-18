# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\manager_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 677)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("font: 63 14pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setContentsMargins(0, 18, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setStyleSheet(".QGroupBox#groupBox{\n"
"font: 63 14pt \"阿里妈妈方圆体 VF SemiBold\";\n"
"border: 2px solid black;\n"
"border-radius: 20;\n"
"    background-color: rgba(0, 0, 0, 155);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setStyleSheet(".QGroupBox{font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";\n"
"    border: 0px;\n"
"    border-top-left-radius: 0px;     \n"
"    border-top-right-radius: 0px;\n"
"     border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setStyleSheet(" background-color: transparent;  \n"
"      border: none; \n"
"                border-bottom: 2px solid rgb(255, 255, 255);\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: lightblue;\n"
"\n"
"            }  ")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_2.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: lightblue;\n"
"\n"
"            }  ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_8.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setContentsMargins(0, 18, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setStyleSheet(".QGroupBox#groupBox_2{\n"
"font: 63 14pt \"阿里妈妈方圆体 VF SemiBold\";\n"
"border: 2px solid black;\n"
"border-radius: 20;\n"
"    background-color: rgba(0, 0, 0, 155);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableView_2 = QtWidgets.QTableView(self.groupBox_2)
        self.tableView_2.setStyleSheet("font: 63 9pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_5.addWidget(self.tableView_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setStyleSheet(".QGroupBox{font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";\n"
"    border: 0px;\n"
"    border-top-left-radius: 0px;     \n"
"    border-top-right-radius: 0px;\n"
"     border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setStyleSheet(" background-color: transparent;  \n"
"      border: none; \n"
"                border-bottom: 2px solid rgb(255, 255, 255);\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setStyleSheet(" background-color: transparent;  \n"
"      border: none; \n"
"                border-bottom: 2px solid rgb(255, 255, 255);\n"
"")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(120, 35))
        self.pushButton_3.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: lightblue;\n"
"\n"
"            }  ")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_2.setMinimumSize(QtCore.QSize(100, 30))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_6.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: lightblue;\n"
"\n"
"            }  ")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        spacerItem10 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_5.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: lightblue;\n"
"\n"
"            }  ")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        spacerItem11 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_4.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: #c8583b;\n"
"\n"
"            }  ")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        spacerItem12 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_7.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: lightblue;\n"
"\n"
"            }  ")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        spacerItem13 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_8.setStyleSheet("\n"
" .QPushButton {  \n"
"font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";\n"
" background-color: white; \n"
"border-radius:5;\n"
"          \n"
"            }  \n"
"            .QPushButton:hover {  \n"
"                background-color: lightblue;\n"
"\n"
"            }  ")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        spacerItem14 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "学生基本信息"))
        self.groupBox_3.setTitle(_translate("Form", "请输入查询学生的学号"))
        self.label_3.setText(_translate("Form", "学生ID："))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "导出数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "学生管理模块"))
        self.groupBox_2.setTitle(_translate("Form", "学生考勤信息"))
        self.groupBox_5.setTitle(_translate("Form", "选择操作"))
        self.label.setText(_translate("Form", "学生id："))
        self.label_2.setText(_translate("Form", "课程id："))
        self.pushButton_3.setText(_translate("Form", "查询考勤"))
        self.pushButton_6.setText(_translate("Form", "增加"))
        self.pushButton_5.setText(_translate("Form", "修改"))
        self.pushButton_4.setText(_translate("Form", "删除"))
        self.pushButton_7.setText(_translate("Form", "导出数据"))
        self.pushButton_8.setText(_translate("Form", "数据可视化"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "考勤管理模块"))
