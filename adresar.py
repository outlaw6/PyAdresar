# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adresar.ui'
#
# Created: Wed Jul 26 17:50:54 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(864, 488)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 861, 461))
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 521, 27))
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 271, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.ucitaj)
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 420, 321, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.radioButton = QtGui.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 71, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 60, 71, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 60, 271, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tableWidget = QtGui.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 841, 321))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lineEdit.setText(_translate("MainWindow", "Unesite tekst", None))
        self.pushButton.setText(_translate("MainWindow", "TRAZI", None))
        self.radioButton.setText(_translate("MainWindow", "NAZIV", None))
        self.radioButton_2.setText(_translate("MainWindow", "GRAD", None))
        self.pushButton_3.setText(_translate("MainWindow", "UCITAJ SVE", None))

    def ucitaj(self):

        self.connection = sqlite3.connect('ADRESAR.db')
        self.c = connection.cursor()
        self.c.execute(''' SELECT * FROM ADRESAR ''')
        rows = self.c.fetchall()

        print rows

if __name__ == '__main__':

    obj = Ui_MainWindow()
    obj.show()
