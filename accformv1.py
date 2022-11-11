# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accformv2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccForn(object):
    def setupUi(self, AccForn):
        AccForn.setObjectName("AccForn")
        AccForn.resize(424, 242)
        self.lineEdit = QtWidgets.QLineEdit(AccForn)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 151, 20))
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(AccForn)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(AccForn)
        self.pushButton.setGeometry(QtCore.QRect(330, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AccForn)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(AccForn)
        self.pushButton_3.setGeometry(QtCore.QRect(54, 100, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(AccForn)
        QtCore.QMetaObject.connectSlotsByName(AccForn)

    def retranslateUi(self, AccForn):
        _translate = QtCore.QCoreApplication.translate
        AccForn.setWindowTitle(_translate("AccForn", "Form"))
        self.lineEdit.setPlaceholderText(_translate("AccForn", "Iput..."))
        self.pushButton.setText(_translate("AccForn", "Exit"))
        self.pushButton_2.setText(_translate("AccForn", "Отправить"))
        self.pushButton_3.setText(_translate("AccForn", "Вывести"))

