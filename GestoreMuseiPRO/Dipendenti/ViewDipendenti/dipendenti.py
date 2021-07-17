# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dipendenti.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from Dipendenti.ControllerDipendenti.ControllerDipendente import ControllerDipendente
from Ui import logo_rc, back_rc


# classe di correlazione tra le funzionalità del controller e le scelte effettuate dall'utente tramite
# l'input/output dell'interfaccia grafica relativa alla visualizzazione della finestra di aggiunta dipendente
# e quella di filtraggio dei dipendenti presenti nel database
class Ui_Dipendenti(object):
    def __init__(self):
        self.controllerDipendenti = ControllerDipendente()

    # metodo per la configurazione, tramite l'input dell'utente, della lista filtrata dei dipendenti
    # presenti nel database
    def listaDipendenti(self):
        self.controllerDipendenti.setListaDipendenti(self.usernameFilterLineEdit.text(), self.cfFilterLineEdit.text(),
                                                     self.nominativoFilterLineEdit.text(), self.ruoloFilterLineEdit.text())
        return self.controllerDipendenti.getListaDipendenti()

    # metodo per l'aggiunta nel database di un nuovo dipendente
    def nuovoDipendente(self):
        try:
            try:
                if self.controllerDipendenti.aggiungiDipendente(self.accountLineEdit.text(), self.cfLineEdit.text(),
                                                                self.nominativoLineEdit.text(), self.ruoloLineEdit.text()):
                    self.clearLabels()
                    self.errorLabel.setStyleSheet("color: rgb(33, 163, 21);")
                    self.errorLabel.setText("Dipendente aggiunto con successo!")

            except sqlite3.Error:
                self.errorLabel.setStyleSheet("color: rgb(247, 8, 8);")
                self.errorLabel.setText("Dipendente già presente!")
        except Exception:
            self.errorLabel.setStyleSheet("color: rgb(247, 8, 8);")
            self.errorLabel.setText("Oops, campi vuoti o errati!")

    # metodo per il reset delle labels di input
    def clearLabels(self):
        self.accountLineEdit.clear()
        self.cfLineEdit.clear()
        self.nominativoLineEdit.clear()
        self.ruoloLineEdit.clear()

    def setupUi(self, UI_dipendenti):
        UI_dipendenti.setObjectName("UI_dipendenti")
        UI_dipendenti.resize(470, 611)
        UI_dipendenti.setStyleSheet("background-color: rgb(242,233,216)")

        self.centralwidget = QtWidgets.QWidget(UI_dipendenti)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 571))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.minimizeButton = QtWidgets.QPushButton(self.frame)
        self.minimizeButton.setGeometry(QtCore.QRect(400, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeButton.setMouseTracking(True)
        self.minimizeButton.setStyleSheet("color:rgb(3, 95, 144);")
        self.minimizeButton.setFlat(True)
        self.minimizeButton.setObjectName("minimizeButton")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(420, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("background-color: rgb(229, 82, 2); \n"
                                      "border-radius:10px;\n"
                                      "color:rgb(3, 95, 144);")
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(160, 10, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.titleLabel.setObjectName("titleLabel")

        self.tab = QtWidgets.QTabWidget(self.frame)
        self.tab.setGeometry(QtCore.QRect(10, 90, 431, 481))
        self.tab.setStyleSheet("color:rgb(3, 95, 144);")
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab.setObjectName("tab")

        self.inserisciWidget = QtWidgets.QWidget()
        self.inserisciWidget.setObjectName("inserisciWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.inserisciWidget)

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.insDatiVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.insDatiVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.insDatiVerticalLayout.setObjectName("insDatiVerticalLayout")

        self.accountLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.accountLineEdit.setFont(font)
        self.accountLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                           "border:2px solid rgba(0,0,0,0);\n"
                                           "color:rgb(3, 95, 144);\n"
                                           "border-bottom-color: rgb(3, 95, 144);\n"
                                           "padding-bottom:10px;")
        self.accountLineEdit.setText("")
        self.accountLineEdit.setObjectName("usernameLineEdit")
        self.insDatiVerticalLayout.addWidget(self.accountLineEdit)

        self.cfLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cfLineEdit.setFont(font)
        self.cfLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                              "border:2px solid rgba(0,0,0,0);\n"
                              "color:rgb(3, 95, 144);\n"
                              "border-bottom-color: rgb(3, 95, 144);\n"
                              "padding-bottom:10px;")
        self.cfLineEdit.setText("")
        self.cfLineEdit.setObjectName("cfLineEdit")
        self.insDatiVerticalLayout.addWidget(self.cfLineEdit)

        self.nominativoLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nominativoLineEdit.setFont(font)
        self.nominativoLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:2px solid rgba(0,0,0,0);\n"
                                      "color:rgb(3, 95, 144);\n"
                                      "border-bottom-color: rgb(3, 95, 144);\n"
                                      "padding-bottom:10px;")
        self.nominativoLineEdit.setText("")
        self.nominativoLineEdit.setObjectName("nominativoLineEdit")
        self.insDatiVerticalLayout.addWidget(self.nominativoLineEdit)

        self.ruoloLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ruoloLineEdit.setFont(font)
        self.ruoloLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                 "border:2px solid rgba(0,0,0,0);\n"
                                 "color:rgb(3, 95, 144);\n"
                                 "border-bottom-color: rgb(3, 95, 144);\n"
                                 "padding-bottom:10px;")
        self.ruoloLineEdit.setText("")
        self.ruoloLineEdit.setObjectName("ruoloLineEdit")
        self.insDatiVerticalLayout.addWidget(self.ruoloLineEdit)

        self.inserisciButton = QtWidgets.QPushButton(self.inserisciWidget)
        self.inserisciButton.setGeometry(QtCore.QRect(310, 400, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inserisciButton.setFont(font)
        self.inserisciButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inserisciButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                              "border-radius:10px;\n"
                                              "color:rgb(242,233,216);")
        self.inserisciButton.setObjectName("inserisciButton")

        self.label_2 = QtWidgets.QLabel(self.inserisciWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label_2.setStyleSheet("color:rgb(229, 82, 2);")
        self.label_2.setObjectName("label_2")

        self.errorLabel = QtWidgets.QLabel(self.inserisciWidget)
        self.errorLabel.setGeometry(QtCore.QRect(40, 410, 251, 20))
        self.errorLabel.setStyleSheet("color: rgb(247, 8, 8);")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")

        self.tab.addTab(self.inserisciWidget, "")
        self.visualizzaWidget = QtWidgets.QWidget()
        self.visualizzaWidget.setObjectName("visualizzaWidget")

        self.visualizzaButton = QtWidgets.QPushButton(self.visualizzaWidget)
        self.visualizzaButton.setGeometry(QtCore.QRect(210, 380, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.visualizzaButton.setFont(font)
        self.visualizzaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualizzaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                            "border-radius:10px;\n"
                                            "color:rgb(242,233,216);")
        self.visualizzaButton.setObjectName("visualizzaButton")

        self.label_3 = QtWidgets.QLabel(self.visualizzaWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 221, 21))
        self.label_3.setStyleSheet("color:rgb(3, 95, 144);")
        self.label_3.setObjectName("label_3")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.visualizzaWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 80, 361, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.usernameFilterLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.usernameFilterLineEdit.setFont(font)
        self.usernameFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                          "border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:10px;")
        self.usernameFilterLineEdit.setText("")
        self.usernameFilterLineEdit.setObjectName("usernameFilterLineEdit")
        self.verticalLayout_2.addWidget(self.usernameFilterLineEdit)

        self.cfFilterLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cfFilterLineEdit.setFont(font)
        self.cfFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                    "border:2px solid rgba(0,0,0,0);\n"
                                    "color:rgb(3, 95, 144);\n"
                                    "border-bottom-color: rgb(3, 95, 144);\n"
                                    "padding-bottom:10px;")
        self.cfFilterLineEdit.setText("")
        self.cfFilterLineEdit.setObjectName("cfFilterLineEdit")
        self.verticalLayout_2.addWidget(self.cfFilterLineEdit)

        self.nominativoFilterLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nominativoFilterLineEdit.setFont(font)
        self.nominativoFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:2px solid rgba(0,0,0,0);\n"
                                            "color:rgb(3, 95, 144);\n"
                                            "border-bottom-color: rgb(3, 95, 144);\n"
                                            "padding-bottom:10px;")
        self.nominativoFilterLineEdit.setText("")
        self.nominativoFilterLineEdit.setObjectName("nominativoFilterLineEdit")
        self.verticalLayout_2.addWidget(self.nominativoFilterLineEdit)

        self.ruoloFilterLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ruoloFilterLineEdit.setFont(font)
        self.ruoloFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                       "border:2px solid rgba(0,0,0,0);\n"
                                       "color:rgb(3, 95, 144);\n"
                                       "border-bottom-color: rgb(3, 95, 144);\n"
                                       "padding-bottom:10px;")
        self.ruoloFilterLineEdit.setText("")
        self.ruoloFilterLineEdit.setObjectName("ruoloFilterLineEdit")
        self.verticalLayout_2.addWidget(self.ruoloFilterLineEdit)

        self.usernameFilterLineEdit.raise_()
        self.nominativoFilterLineEdit.raise_()
        self.ruoloFilterLineEdit.raise_()
        self.cfFilterLineEdit.raise_()
        self.tab.addTab(self.visualizzaWidget, "")
        self.accountMenu = QtWidgets.QComboBox(self.frame)
        self.accountMenu.setGeometry(QtCore.QRect(10, 60, 141, 22))
        self.accountMenu.setStyleSheet("color: rgb(65, 65, 65);")
        self.accountMenu.setCurrentText("")
        self.accountMenu.setFrame(True)
        self.accountMenu.setObjectName("accountMenu")
        self.accountMenu.addItem("")
        self.accountMenu.addItem("")

        self.utenteLabel = QtWidgets.QLabel(self.frame)
        self.utenteLabel.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.utenteLabel.setFont(font)
        self.utenteLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.utenteLabel.setObjectName("utenteLabel")

        self.logoLabel = QtWidgets.QLabel(self.frame)
        self.logoLabel.setGeometry(QtCore.QRect(380, 40, 61, 61))
        self.logoLabel.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logoLabel.setText("")
        #self.logoLabel.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")

        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setMouseTracking(True)
        self.backButton.setStyleSheet("border-image: url(:/newPrefix/back_button.png);")
        self.backButton.setText("")
        self.backButton.setFlat(True)
        self.backButton.setObjectName("Back")
        UI_dipendenti.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UI_dipendenti)
        self.statusbar.setObjectName("statusbar")
        UI_dipendenti.setStatusBar(self.statusbar)

        self.retranslateUi(UI_dipendenti)
        self.tab.setCurrentIndex(0)
        self.accountMenu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(UI_dipendenti)


    def retranslateUi(self, UI_dipendenti):
        _translate = QtCore.QCoreApplication.translate
        UI_dipendenti.setWindowTitle(_translate("UI_dipendenti", "Personale"))
        self.minimizeButton.setText(_translate("UI_dipendenti", "-"))
        self.closeButton.setText(_translate("UI_dipendenti", "X"))
        self.titleLabel.setText(_translate("UI_dipendenti", "Gestione Dipendenti"))
        self.accountLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Username"))
        self.cfLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Codice Fiscale"))
        self.nominativoLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Nominativo"))
        self.ruoloLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Ruolo"))
        self.inserisciButton.setText(_translate("UI_dipendenti", "Inserisci"))
        self.label_2.setToolTip(_translate("UI_dipendenti", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setWhatsThis(_translate("UI_dipendenti", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("UI_dipendenti",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Inserisci dipendente</span></p></body></html>"))
        self.tab.setTabText(self.tab.indexOf(self.inserisciWidget), _translate("UI_dipendenti", "Inserisci Nuovo"))
        self.visualizzaButton.setText(_translate("UI_dipendenti", "Visualizza elenco filtrato"))
        self.label_3.setText(_translate("UI_dipendenti",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#e55202;\">Inserimento filtri per la ricerca</span></p></body></html>"))
        self.usernameFilterLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Username"))
        self.cfFilterLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Codice Fiscale"))
        self.nominativoFilterLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Nominativo"))
        self.ruoloFilterLineEdit.setPlaceholderText(_translate("UI_dipendenti", "Ruolo"))
        self.tab.setTabText(self.tab.indexOf(self.visualizzaWidget), _translate("UI_dipendenti", "Visualizza elenco"))
        self.accountMenu.setItemText(0, _translate("UI_dipendenti", "Home"))
        self.accountMenu.setItemText(1, _translate("UI_dipendenti", "Logout"))
        self.utenteLabel.setText(_translate("UI_dipendenti", "NOMEUTENTE"))
