import sys, sqlite3
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "adresar.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
	self.pushButton.clicked.connect(self.ucitaj)

    def ucitaj(self):
	'''
        self.connection = sqlite3.connect('adresar.db')
        self.c = self.connection.cursor()
        
        #rows = self.c.fetchall()
	self.tableWidget.setRowCount(1)
	self.tableWidget.setColumnCount(5)
	
        #print rows

	for row_num, row_data in enumerate(result):
		#self.tableWidget.insertRow(row_num)
		for col_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_num, col_number, \
			QtGui.QTableWidgetItem(str(data)))

	'''
	if self.radioButton.text() == "NAZIV":
        	if self.radioButton.isChecked() == True:
	       		print self.radioButton.text()+" is selected"
        if self.radioButton_2.text() == "GRAD":
        	if self.radioButton_2.isChecked() == True:
            		print self.radioButton_2.text()+" is selected"
         

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
