# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 545)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet(".QFrame#frame{border-image: url(:/img/img/Desktop_-_1.png);}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("font: 63 14pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(230, 410, 161, 41))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 430, 51, 21))
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.idlineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.idlineEdit.setGeometry(QtCore.QRect(190, 255, 241, 41))
        self.idlineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.idlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.idlineEdit.setObjectName("idlineEdit")
        self.pwdlineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.pwdlineEdit.setGeometry(QtCore.QRect(190, 330, 241, 41))
        self.pwdlineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.pwdlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pwdlineEdit.setObjectName("pwdlineEdit")
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "学生考勤管理系统"))
import ui.imglogin
