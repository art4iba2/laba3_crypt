import sys
from PyQt5 import QtCore, QtWidgets
from accformv1 import Ui_AccForn
from des import Ui_Login
from exitform import Ui_Exit_form
from md5 import *
from textwrap import wrap

#####################################################################
def Exit_acc():
    global Exit_acc
    Exit_acc = QtWidgets.QDialog()
    ui = Ui_Exit_form()
    ui.setupUi(Exit_acc)
    AccForn.hide()
    Exit_acc.show()

    def buttonEX():
        Exit_acc.close()

    def buttonRET():
        Exit_acc.hide()
        AccForn.show()

    ui.pushButton.clicked.connect(buttonRET)
    ui.pushButton_2.clicked.connect(buttonEX)
#####################################################################################################
def openAccForn():
    global AccForn
    AccForn = QtWidgets.QDialog()
    ui = Ui_AccForn()
    ui.setupUi(AccForn)
    formF.hide()
    AccForn.show()

    # Функция вывода зашифрованного текста в файл
    def record():
        text = ui.lineEdit.text()
        text = text.replace(" ", "_")
        text = wrap(text, 10)
        for i in range(len(text)):
            text[i] = MD5(bytes(text[i],encoding='utf-8'))
        text = "".join(text)
        with open('user_DB.txt', 'r+', -1, 'utf-8') as file:
            file.write(text)
            ui.lineEdit_2.setText("")
        file.close()

    # Функция вывода текста в форму
    def translate():
        with open('user_DB.txt', 'r+', -1, 'utf-8') as file:
            text = file.readlines()[0]
            text = wrap(text, 10)
            for i in range(len(text)):
                text[i] = MD5(bytes(text[i],encoding='utf-8'))
            text = "".join(text)
            text = text.replace("_", " ")
            ui.lineEdit_2.setText(text)
            file.truncate()
        file.close()


    ui.pushButton_2.clicked.connect(record)

    ui.pushButton_3.clicked.connect(translate)

    ui.pushButton.clicked.connect(Exit_acc)
#####################################################################################################

# Функция входа
def login(username, password, signal):
    global user_data
    with open('users.txt', 'r+') as file:
        flag = False
        for line in file:
            line = line.split('<-[Username]:[Password]->')
            line[1] = line[1][:len(line[1])-1]
            if line[0] == MD5(bytes(username, encoding='utf-8')) and line[1] == MD5(bytes(password, encoding='utf-8')):
                flag = True
                user_data = r"data_D.txt"
                user_data = user_data.replace('D', username)
                openAccForn()
        if not flag:
            signal.emit('Проверьте правильность ввода данных!')
    file.close()


# Функция регистрации
def register(username, password, signal):
    flag2 = False
    with open('users.txt', 'r+') as file:
        for line in file:
            line = line.split('<-[Username]:[Password]->')
            line[1] = line[1][:len(line[1]) - 1]
            if line[0] == MD5(bytes(username, encoding='utf-8')):
                flag2 = True
                signal.emit('Такой ник уже используется!')
        if username == '' or password == '':
            flag2 = True
            signal.emit('Не оставляйте поля пустыми!')
        if not flag2:
            file.write(MD5(bytes(username, encoding='utf-8')))
            file.write('<-[Username]:[Password]->')
            file.write(MD5(bytes(password, encoding='utf-8')))
            file.write('\n')
            signal.emit('Вы успешно зарегистрированы!')
    file.close()

#####################################################################################################
class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, name, passw):
        login(name, passw, self.mysignal)

    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)
#####################################################################################################

#####################################################################################################
class Interface(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)



    # Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)

    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, passw)


app = QtWidgets.QApplication(sys.argv)
formF = Interface()
formF.show()
app.exec_()