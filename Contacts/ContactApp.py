import sys
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QPushButton
from Contacts.contactsFunctions import *


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("contacts.ui", self)
        style = "::section {""background-color: rgb(68,114,196; }"
        self.tableWidget.horizontalHeader().setStyleSheet(style)
        self.tableWidget.verticalHeader().setStyleSheet(style)
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 50)

        self.btnSearchContact.setIcon(QIcon('search_icon.png'))
        self.btnSearchContact.clicked.connect(self.SearchContact)
        self.btnAddNewContact.clicked.connect(self.AddClicked)
        self.SetVisibility(False)
        self.btnAddContact.setVisible(False)
        self.btnUpdateContact.setVisible(False)
        self.ErrorLbl.setVisible(False)
        self.loadData()

    def loadData(self):
        contacts = displayAllContactsApp()
        row = 0
        if contacts == "no contacts in DB":
            self.tableWidget.setRowCount(0)
        else:
            self.tableWidget.setRowCount(len(contacts))
            for person in contacts:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["firstName"]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["lastName"])))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person["phoneNumber"]))

                editButton = QPushButton(self)
                editButton.clicked.connect(self.editClicked)
                editButton.setIcon(QIcon('edit.tif'))

                deleteButton = QtWidgets.QPushButton(self)
                deleteButton.clicked.connect(self.deleteClicked)
                deleteButton.setIcon(QIcon('delete.tif'))
                self.tableWidget.setCellWidget(row, 3, editButton)
                self.tableWidget.setCellWidget(row, 4, deleteButton)

                row = row + 1

    def loadSearchData(self, contact):
        row = 0
        self.tableWidget.setRowCount(1)

        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(contact["firstName"]))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(contact["lastName"])))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(contact["phoneNumber"]))
        editButton = QPushButton(self)
        editButton.clicked.connect(self.editClicked)
        editButton.setIcon(QIcon('edit.tif'))
        deleteButton = QtWidgets.QPushButton(self)
        deleteButton.clicked.connect(self.deleteClicked)
        deleteButton.setIcon(QIcon('delete.tif'))
        self.tableWidget.setCellWidget(row, 3, editButton)
        self.tableWidget.setCellWidget(row, 4, deleteButton)

    def ClearData(self):
        self.firstNameInp.setText("")
        self.lastNameInp.setText("")
        self.phoneNumberInp.setText("")

    def SetVisibility(self, show):
        self.FirstNameLbl.setVisible(show)
        self.lastNameLbl.setVisible(show)
        self.phoneNumberLbl.setVisible(show)
        self.firstNameInp.setVisible(show)
        self.lastNameInp.setVisible(show)
        self.phoneNumberInp.setVisible(show)

    def AddClicked(self):
        self.SetVisibility(True)
        self.ClearData()
        self.btnAddContact.setVisible(True)
        self.btnAddContact.setIcon(QIcon('save_icon.png'))
        self.btnAddContact.clicked.connect(self.AddNewContact)

    def AddNewContact(self):
        firstName = self.firstNameInp.toPlainText()
        lastName = self.lastNameInp.toPlainText()
        phoneNumber = self.phoneNumberInp.toPlainText()
        if firstName != "" and lastName != "" and phoneNumber != "":
            contactToAdd = Contact(firstName, lastName, phoneNumber)
            addContact(contactToAdd)
            self.loadData()
            self.btnAddContact.setVisible(False)
            self.SetVisibility(False)
            self.ClearData()

    def SearchContact(self):
        Name = self.nameToSearchInp.toPlainText()
        contact = search1(Name)
        if contact:
            self.loadSearchData(contact)
        else:
            self.nameToSearchInp.setText("No data was found for the input value")
            self.loadData()

    def editClicked(self):
        button = self.sender()
        if button:
            row = self.tableWidget.currentRow()
            g.firstName = self.tableWidget.item(row, 0).text()
            g.lastName = self.tableWidget.item(row, 1).text()
            g.phoneNumber = self.tableWidget.item(row, 2).text()
            self.firstNameInp.setText(g.firstName)
            self.lastNameInp.setText(g.lastName)
            self.phoneNumberInp.setText(g.phoneNumber)
            self.SetVisibility(True)
            self.btnUpdateContact.setVisible(True)
            self.btnUpdateContact.setIcon(QIcon('save_icon.png'))
            self.btnUpdateContact.clicked.connect(self.UpdateContact)

    def UpdateContact(self):
        firstName = self.firstNameInp.toPlainText()
        lastName = self.lastNameInp.toPlainText()
        phoneNumber = self.phoneNumberInp.toPlainText()
        if firstName != g.firstName:
            updateContact("firstName", g.firstName, firstName)
        if lastName != g.lastName:
            updateContact("lastName", g.lastName, lastName)
        if phoneNumber != g.phoneNumber:
            updateContact("phoneNumber", g.phoneNumber, phoneNumber)
        g.firstName = firstName
        g.lastName = lastName
        g.phoneNumber = phoneNumber
        self.SetVisibility(False)
        self.btnUpdateContact.setVisible(False)
        self.loadData()

    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.tableWidget.currentRow()
            Name = self.tableWidget.item(row, 0).text()
            deleteContact(Name)
            self.loadData()


app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedHeight(500)
widget.setFixedWidth(490)
widget.show()

app.exec()
