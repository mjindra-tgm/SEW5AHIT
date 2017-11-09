# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rest.ui'
#
# Created: Thu Nov  9 17:21:06 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 309)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.submit = QtGui.QPushButton(Form)
        self.submit.setObjectName("submit")
        self.verticalLayout_6.addWidget(self.submit)
        self.reset = QtGui.QPushButton(Form)
        self.reset.setObjectName("reset")
        self.verticalLayout_6.addWidget(self.reset)
        self.close = QtGui.QPushButton(Form)
        self.close.setObjectName("close")
        self.verticalLayout_6.addWidget(self.close)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.ergebnis = QtGui.QTextBrowser(Form)
        self.ergebnis.setText("")
        self.ergebnis.setObjectName("ergebnis")
        self.verticalLayout.addWidget(self.ergebnis)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.submit, QtCore.SIGNAL("clicked()"), Form.submit)
        QtCore.QObject.connect(self.reset, QtCore.SIGNAL("clicked()"), Form.reset)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Ziel", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.reset.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    u = Ui_Form()