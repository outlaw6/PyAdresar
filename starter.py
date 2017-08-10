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
	self.pushButton_3.clicked.connect(self.dumpBaze)

    def ucitaj(self):
	tekst = self.lineEdit.text()
	self.connection = sqlite3.connect('adresar.db')
        self.c = self.connection.cursor()	
	print tekst
	
	if self.radioButton.text() == "NAZIV":
        	if self.radioButton.isChecked() == True:
	       		print self.radioButton.text()+" is selected"
			result = self.c.execute(" SELECT * FROM ADRESAR where ime LIKE ?", ('%' + str(tekst) + '%',))
			#rows = self.c.fetchall()
			print result
			self.tableWidget.setRowCount(1)
			self.tableWidget.setColumnCount(5)
	
			# Podesi sirinu kolona
			self.tableWidget.setColumnWidth(0,20)
			self.tableWidget.setColumnWidth(1,200)
			self.tableWidget.setColumnWidth(2,200)
			self.tableWidget.setColumnWidth(3,200)
			self.tableWidget.setColumnWidth(4,200)
		

			for row_num, row_data in enumerate(result):
				#self.tableWidget.insertRow(row_num)
				for col_number, data in enumerate(row_data):
					self.tableWidget.setItem(row_num, col_number, \
					QtGui.QTableWidgetItem(str(data)))

        if self.radioButton_2.text() == "GRAD":
        	if self.radioButton_2.isChecked() == True:
            		print self.radioButton_2.text()+" is selected"
			result = self.c.execute(" SELECT * FROM ADRESAR where grad LIKE ?", ('%' + str(tekst) + '%',))
			print result
			self.tableWidget.setRowCount(1)
			self.tableWidget.setColumnCount(5)

			# Podesi sirinu kolona
			self.tableWidget.setColumnWidth(0,20)
			self.tableWidget.setColumnWidth(1,200)
			self.tableWidget.setColumnWidth(2,200)
			self.tableWidget.setColumnWidth(3,200)
			self.tableWidget.setColumnWidth(4,200)
		

			for row_num, row_data in enumerate(result):
				#self.tableWidget.insertRow(row_num)
				for col_number, data in enumerate(row_data):
					self.tableWidget.setItem(row_num, col_number, \
					QtGui.QTableWidgetItem(str(data)))




    def dumpBaze(self):
	self.connection = sqlite3.connect('adresar.db')
        self.c = self.connection.cursor()
        result = self.c.execute(''' SELECT * FROM ADRESAR ''')
        rows = self.c.fetchall()
	self.tableWidget.setRowCount(1)
	self.tableWidget.setColumnCount(5)
	
	# Podesi sirinu kolona
	self.tableWidget.setColumnWidth(0,20)
	self.tableWidget.setColumnWidth(1,200)
	self.tableWidget.setColumnWidth(2,200)
	self.tableWidget.setColumnWidth(3,200)
	self.tableWidget.setColumnWidth(4,200)
        

	for row_num, row_data in enumerate(rows):
		self.tableWidget.insertRow(row_num)
		for col_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_num, col_number, \
			QtGui.QTableWidgetItem(str(data)))
         

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
