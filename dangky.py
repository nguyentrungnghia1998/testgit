# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dangky.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dangky(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 576)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 240, 171, 41))
        self.label.setObjectName("label")
        self.BACK = QtWidgets.QPushButton(Form)
        self.BACK.setGeometry(QtCore.QRect(100, 50, 93, 28))
        self.BACK.setObjectName("BACK")
        self.DANGNHAP = QtWidgets.QPushButton(Form)
        self.DANGNHAP.setGeometry(QtCore.QRect(360, 500, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DANGNHAP.setFont(font)
        self.DANGNHAP.setObjectName("DANGNHAP")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 330, 111, 41))
        self.label_3.setObjectName("label_3")
        self.Password = QtWidgets.QLineEdit(Form)
        self.Password.setGeometry(QtCore.QRect(380, 330, 381, 31))
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 491, 61))
        self.label_2.setObjectName("label_2")
        self.Account = QtWidgets.QLineEdit(Form)
        self.Account.setGeometry(QtCore.QRect(380, 240, 381, 31))
        self.Account.setText("")
        self.Account.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Account.setObjectName("Account")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 420, 251, 41))
        self.label_4.setObjectName("label_4")
        self.Password2 = QtWidgets.QLineEdit(Form)
        self.Password2.setGeometry(QtCore.QRect(380, 420, 381, 31))
        self.Password2.setText("")
        self.Password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password2.setObjectName("Password2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">TÊN ĐĂNG NHẬP:</span></p></body></html>"))
        self.BACK.setText(_translate("Form", "BACK"))
        self.DANGNHAP.setText(_translate("Form", "ĐĂNG KÝ"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">MẬT KHẨU:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">ĐĂNG KÝ TÀI KHOẢN BẠN ĐỌC</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">XÁC NHẬN LẠI MẬT KHẨU:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
