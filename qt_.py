# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import ctypes
myappid = '' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r''))

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_print_ham = QtGui.QPushButton(Form)
        self.btn_print_ham.setObjectName(_fromUtf8("btn_print_ham"))
        self.verticalLayout.addWidget(self.btn_print_ham)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", 'Encore', None))
        self.btn_print_ham.setText(_translate("Form", "Print Ham", None))
        self.btn_print_ham.clicked.connect(self.printHam)

    def printHam(self):
        print('ham')


App = QtGui.QApplication(sys.argv)
ex = Ui_Form()
ex.show()
sys.exit(App.exec_())
