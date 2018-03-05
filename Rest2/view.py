# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Wed Dec 20 09:08:49 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.start = QtGui.QLineEdit(Form)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.ziel = QtGui.QLineEdit(Form)
        self.ziel.setObjectName("ziel")
        self.horizontalLayout_2.addWidget(self.ziel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.submit = QtGui.QPushButton(Form)
        self.submit.setObjectName("submit")
        self.horizontalLayout_3.addWidget(self.submit)
        self.reset = QtGui.QPushButton(Form)
        self.reset.setObjectName("reset")
        self.horizontalLayout_3.addWidget(self.reset)
        self.close = QtGui.QPushButton(Form)
        self.close.setObjectName("close")
        self.horizontalLayout_3.addWidget(self.close)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.submit, QtCore.SIGNAL("clicked()"), Form.submit)
        QtCore.QObject.connect(self.reset, QtCore.SIGNAL("clicked()"), Form.reset)
        QtCore.QObject.connect(self.start, QtCore.SIGNAL("returnPressed()"), self.ziel.setFocus)
        QtCore.QObject.connect(self.ziel, QtCore.SIGNAL("returnPressed()"), Form.submit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Google Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Ziel:", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("Form", "submit", None, QtGui.QApplication.UnicodeUTF8))
        self.reset.setText(QtGui.QApplication.translate("Form", "reset", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("Form", "close", None, QtGui.QApplication.UnicodeUTF8))

