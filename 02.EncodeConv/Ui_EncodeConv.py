# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncodeConv.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyForm(object):
    def setupUi(self, MyForm):
        MyForm.setObjectName("MyForm")
        MyForm.resize(647, 341)
        self.label = QtWidgets.QLabel(MyForm)
        self.label.setGeometry(QtCore.QRect(20, 10, 31, 16))
        self.label.setObjectName("label")
        self.TransferButton = QtWidgets.QPushButton(MyForm)
        self.TransferButton.setGeometry(QtCore.QRect(540, 40, 91, 31))
        self.TransferButton.setObjectName("TransferButton")
        self.lineEdit = QtWidgets.QLineEdit(MyForm)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 561, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(MyForm)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 80, 621, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(MyForm)
        self.label_2.setGeometry(QtCore.QRect(298, 41, 36, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_split = QtWidgets.QComboBox(MyForm)
        self.comboBox_split.setGeometry(QtCore.QRect(340, 41, 62, 20))
        self.comboBox_split.setObjectName("comboBox_split")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.label_3 = QtWidgets.QLabel(MyForm)
        self.label_3.setGeometry(QtCore.QRect(16, 41, 48, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_ori = QtWidgets.QComboBox(MyForm)
        self.comboBox_ori.setGeometry(QtCore.QRect(70, 41, 81, 20))
        self.comboBox_ori.setObjectName("comboBox_ori")
        self.comboBox_ori.addItem("")
        self.comboBox_ori.addItem("")
        self.comboBox_ori.addItem("")
        self.comboBox_ori.addItem("")
        self.comboBox_ori.addItem("")
        self.comboBox_ori.addItem("")
        self.comboBox_ori.addItem("")
        self.label_4 = QtWidgets.QLabel(MyForm)
        self.label_4.setGeometry(QtCore.QRect(157, 41, 48, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_new = QtWidgets.QComboBox(MyForm)
        self.comboBox_new.setGeometry(QtCore.QRect(211, 41, 81, 20))
        self.comboBox_new.setObjectName("comboBox_new")
        self.comboBox_new.addItem("")
        self.comboBox_new.addItem("")
        self.comboBox_new.addItem("")
        self.comboBox_new.addItem("")
        self.comboBox_new.addItem("")
        self.comboBox_new.addItem("")
        self.DetectButton = QtWidgets.QPushButton(MyForm)
        self.DetectButton.setGeometry(QtCore.QRect(430, 40, 81, 31))
        self.DetectButton.setObjectName("DetectButton")

        self.retranslateUi(MyForm)
        QtCore.QMetaObject.connectSlotsByName(MyForm)

    def retranslateUi(self, MyForm):
        _translate = QtCore.QCoreApplication.translate
        MyForm.setWindowTitle(_translate("MyForm", "编码格式批量转换"))
        self.label.setText(_translate("MyForm", "路径："))
        self.TransferButton.setToolTip(_translate("MyForm", "按制定格式进行转换！"))
        self.TransferButton.setText(_translate("MyForm", "执行转换"))
        self.lineEdit.setWhatsThis(_translate("MyForm", "请输入路径"))
        self.lineEdit.setText(_translate("MyForm", "g:\\test"))
        self.label_2.setText(_translate("MyForm", "过滤："))
        self.comboBox_split.setToolTip(_translate("MyForm", "默认过滤：.zip\\.rar\\.tar"))
        self.comboBox_split.setItemText(0, _translate("MyForm", ".svn"))
        self.comboBox_split.setItemText(1, _translate("MyForm", ".cache"))
        self.label_3.setText(_translate("MyForm", "源格式："))
        self.comboBox_ori.setItemText(0, _translate("MyForm", "utf-8"))
        self.comboBox_ori.setItemText(1, _translate("MyForm", "GB2312"))
        self.comboBox_ori.setItemText(2, _translate("MyForm", "ascii"))
        self.comboBox_ori.setItemText(3, _translate("MyForm", "utf_8_sig"))
        self.comboBox_ori.setItemText(4, _translate("MyForm", "gbk"))
        self.comboBox_ori.setItemText(5, _translate("MyForm", "windows-1252"))
        self.comboBox_ori.setItemText(6, _translate("MyForm", "*"))
        self.label_4.setText(_translate("MyForm", "新格式："))
        self.comboBox_new.setItemText(0, _translate("MyForm", "GB2312"))
        self.comboBox_new.setItemText(1, _translate("MyForm", "ascii"))
        self.comboBox_new.setItemText(2, _translate("MyForm", "utf-8"))
        self.comboBox_new.setItemText(3, _translate("MyForm", "utf_8_sig"))
        self.comboBox_new.setItemText(4, _translate("MyForm", "gbk"))
        self.comboBox_new.setItemText(5, _translate("MyForm", "windows-1252"))
        self.DetectButton.setToolTip(_translate("MyForm", "检测路径下所有文件类型"))
        self.DetectButton.setText(_translate("MyForm", "检测类型"))

