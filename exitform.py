# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exit_Form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Exit_form(object):
    def setupUi(self, Exit_form):
        Exit_form.setObjectName("Exit_form")
        Exit_form.resize(341, 173)
        self.pushButton = QtWidgets.QPushButton(Exit_form)
        self.pushButton.setGeometry(QtCore.QRect(40, 60, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Exit_form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 60, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Exit_form)
        QtCore.QMetaObject.connectSlotsByName(Exit_form)

    def retranslateUi(self, Exit_form):
        _translate = QtCore.QCoreApplication.translate
        Exit_form.setWindowTitle(_translate("Exit_form", "Form"))
        self.pushButton.setText(_translate("Exit_form", "Вернуться"))
        self.pushButton_2.setText(_translate("Exit_form", "Выйти"))

