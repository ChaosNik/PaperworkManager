from PyQt5 import QtWidgets, uic
from . import config
import sys
from pdf2image import convert_from_path
import os

class GlavniProzor(QtWidgets.QMainWindow):
    def __init__(self):
        super(GlavniProzor, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('GlavniProzor.ui', self) # Load the .ui file

        self.txtKategorijeDokumenta = self.findChild(QtWidgets.QPushButton, 'txtKategorijeDokumenta')  # Find the button
        self.txtKategorijeDokumenta.clicked.connect(
            self.txtKategorijeDokumentaClick)  # Remember to pass the definition/method, not the return value!

        self.btnNoviDokument = self.findChild(QtWidgets.QPushButton, 'btnNoviDokument')  # Find the button
        self.btnNoviDokument.clicked.connect(
            self.btnNoviDokumentClick)  # Remember to pass the definition/method, not the return value!

        self.btnStampajDokument = self.findChild(QtWidgets.QPushButton, 'btnStampajDokument')  # Find the button
        self.btnStampajDokument.clicked.connect(
            self.btnStampajDokumentClick)  # Remember to pass the definition/method, not the return value!

        self.btnSacuvajDokument = self.findChild(QtWidgets.QPushButton, 'btnSacuvajDokument')  # Find the button
        self.btnSacuvajDokument.clicked.connect(
            self.btnSacuvajDokumentClick)  # Remember to pass the definition/method, not the return value!

        self.btnStampajKategoriju = self.findChild(QtWidgets.QPushButton, 'btnStampajKategoriju')  # Find the button
        self.btnStampajKategoriju.clicked.connect(
            self.btnStampajKategorijuClick)  # Remember to pass the definition/method, not the return value!

        self.btnSacuvajKategoriju = self.findChild(QtWidgets.QPushButton, 'btnSacuvajKategoriju')  # Find the button
        self.btnSacuvajKategoriju.clicked.connect(
            self.btnSacuvajKategorijuClick)  # Remember to pass the definition/method, not the return value!

        self.btnPretraga = self.findChild(QtWidgets.QPushButton, 'btnPretraga')  # Find the button
        self.btnPretraga.clicked.connect(
            self.btnPretragaClick)  # Remember to pass the definition/method, not the return value!

        PDF_file = config.documentFolderPath + "2014-08-29 000342 21-46-952-1-1-1831-2014 POSJEDOVNI LIST ZA ZEMLJU IZA CVJETKA TRIVUNČEVIĆA"
        pages = convert_from_path(PDF_file, poppler_path=config.popplerPath)
        image_counter = 1
        for page in pages:
            filename = "page_" + str(image_counter) + ".jpg"
            page.save(filename, 'JPEG')
            image_counter = image_counter + 1
        filelimit = image_counter - 1

        self.dialogs = list()

        self.show()  # Show the GUI

    def txtKategorijeDokumentaClick(self):
        dialog = IzborKategorija(self)
        self.dialogs.append(dialog)
        dialog.show()
    def btnNoviDokumentClick(self):
        dialog = DodavanjeDokumenta(self)
        self.dialogs.append(dialog)
        dialog.show()
    def btnStampajDokumentClick(self):
        print('printButtonPressed')
    def btnSacuvajDokumentClick(self):
        print('printButtonPressed')
    def btnStampajKategorijuClick(self):
        print('printButtonPressed')
    def btnSacuvajKategorijuClick(self):
        print('printButtonPressed')
    def btnPretragaClick(self):
        print('printButtonPressed')

class DodavanjeDokumenta(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(DodavanjeDokumenta, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('DodavanjeDokumenta.ui', self)  # Load the .ui file

        self.show()  # Show the GUI

class IzborKategorija(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(IzborKategorija, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('IzborKategorija.ui', self)  # Load the .ui file

        self.show()  # Show the GUI

app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = GlavniProzor()  # Create an instance of our class
app.exec_()  # Start the application