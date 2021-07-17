import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from mostra.controller.ControllerMostra import ControllerMostra
from qr.GestioneQr import GestioneQr
from visita.controller.ControllerVisita import ControllerVisita


class Ui_Visite(object):
    def __init__(self):
        self.controller = ControllerVisita()


    def caricaMostre(self):
        try:
            controllerMostre = ControllerMostra()
            listaMostre = controllerMostre.mostreInCorso()
            listaIdMostre = []
            if listaMostre:
                for mostra in listaMostre:
                    self.mostraComboBox.addItem(mostra.titolo)
                    listaIdMostre.append(mostra.ID)
            return listaIdMostre
        except Exception:
            raise


    def prenotazioneToVisitaQr(self, qrPath):
        tariffa = self.tariffaComboBox_2.currentText()
        orario = self.orarioComboBox_2.currentText()
        codice = None
        try:
            codice = GestioneQr.readQr(qrPath)
            if tariffa and orario and codice:
                try:
                    self.controller.converti_prenotazione(codice, tariffa, orario)
                    self.prenotazioneLabel.setStyleSheet("color: rgb(34, 177, 76)")
                    self.prenotazioneLabel.setText("Visita salvata")
                except Exception as e:
                    self.prenotazioneLabel.setStyleSheet("color: rgb(237, 28, 36)")
                    self.prenotazioneLabel.setText(e.args[0])
            else:
                self.prenotazioneLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.prenotazioneLabel.setText("Attenzione: inserisci tutti i dati!")
        except Exception as e:
            self.prenotazioneLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.prenotazioneLabel.setText(e.args[0])

    def prenotazioneToVisitaCodice(self):
        tariffa = self.tariffaComboBox_2.currentText()
        orario = self.orarioComboBox_2.currentText()
        codice = self.codiceTextEdit.text()
        if tariffa and orario and codice:
            try:
                self.controller.converti_prenotazione(codice, tariffa, orario)
                self.prenotazioneLabel.setStyleSheet("color: rgb(34, 177, 76)")
                self.prenotazioneLabel.setText("Visita salvata")
            except Exception as e:
                self.prenotazioneLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.prenotazioneLabel.setText(e.args[0])
        else:
            self.prenotazioneLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.prenotazioneLabel.setText("Attenzione: inserisci tutti i dati!")

    def saveVisita(self, listaIdMostre):
        data = datetime.date.today().strftime("%d-%m-%Y")
        ora = self.orarioComboBox.currentText()
        tariffa = self.tariffaComboBox_1.currentText()
        nominativo = self.nomeTextEdit.text()
        telefono = self.telefonoTextEdit.text()
        ID_mostra = listaIdMostre[self.mostraComboBox.currentIndex()]
        if data and ora and tariffa and nominativo and telefono and ID_mostra:
            try:
                self.controller.save_visita(
                    data, ora, tariffa, nominativo, telefono, ID_mostra
                )
                self.nuovaLabel.setStyleSheet("color: rgb(34, 177, 76)")
                self.nuovaLabel.setText("Visita salvata")
            except Exception as e:
                self.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.nuovaLabel.setText(e.args[0])
        else:
            self.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.nuovaLabel.setText("Attenzione: inserisci tutti i dati!")

    def setupUi(self, UI_Visite):
        UI_Visite.setObjectName("UI_Visite")
        UI_Visite.resize(480, 640)
        UI_Visite.setStyleSheet("background-color: rgb(242,233,216)")

        self.centralwidget = QtWidgets.QWidget(UI_Visite)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.Minimize = QtWidgets.QPushButton(self.frame)
        self.Minimize.setGeometry(QtCore.QRect(400, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Minimize.setFont(font)
        self.Minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Minimize.setMouseTracking(True)
        self.Minimize.setStyleSheet("color:rgb(3, 95, 144);")
        self.Minimize.setFlat(True)
        self.Minimize.setObjectName("Minimize")

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(160, 10, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color:rgb(229, 82, 2);")
        self.Title.setObjectName("Title")

        self.Back = QtWidgets.QPushButton(self.frame)
        self.Back.setGeometry(QtCore.QRect(10, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Back.setFont(font)
        self.Back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back.setMouseTracking(True)
        self.Back.setStyleSheet("color:rgb(3, 95, 144);")
        self.Back.setFlat(True)
        self.Back.setObjectName("Back")

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 141, 22))
        self.comboBox.setStyleSheet("color: rgb(65, 65, 65);")
        self.comboBox.setCurrentText("")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.User = QtWidgets.QLabel(self.frame)
        self.User.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.User.setFont(font)
        self.User.setStyleSheet("color:rgb(3, 95, 144);")
        self.User.setObjectName("User")

        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 431, 471))
        self.tabWidget.setStyleSheet("color:rgb(3, 95, 144);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")

        self.nuovaWidget = QtWidgets.QWidget()
        self.nuovaWidget.setObjectName("nuovaWidget")

        self.telefonoTextEdit = QtWidgets.QLineEdit(self.nuovaWidget)
        self.telefonoTextEdit.setGeometry(QtCore.QRect(10, 60, 300, 34))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.telefonoTextEdit.setFont(font)
        self.telefonoTextEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:2px solid rgba(0,0,0,0);\n"
                                            "color:rgb(3, 95, 144);\n"
                                            "border-bottom-color: rgb(3, 95, 144);\n"
                                            "padding-bottom:10px;")
        self.telefonoTextEdit.setText("")
        self.telefonoTextEdit.setObjectName("telefonoTextEdit")

        self.nomeTextEdit = QtWidgets.QLineEdit(self.nuovaWidget)
        self.nomeTextEdit.setGeometry(QtCore.QRect(10, 120, 300, 34))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nomeTextEdit.setFont(font)
        self.nomeTextEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "border:2px solid rgba(0,0,0,0);\n"
                                        "color:rgb(3, 95, 144);\n"
                                        "border-bottom-color: rgb(3, 95, 144);\n"
                                        "padding-bottom:10px;")
        self.nomeTextEdit.setText("")
        self.nomeTextEdit.setObjectName("nomeTextEdit")

        self.tariffaLabel_1 = QtWidgets.QLabel(self.nuovaWidget)
        self.tariffaLabel_1.setText("Tariffa: ")
        self.tariffaLabel_1.setGeometry(QtCore.QRect(10, 180, 100, 34))

        self.tariffaComboBox_1 = QtWidgets.QComboBox(self.nuovaWidget)
        self.tariffaComboBox_1.setGeometry(QtCore.QRect(60, 180, 200, 34))
        self.tariffaComboBox_1.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                             "color:rgb(3, 95, 144);\n"
                                             "border-bottom-color: rgb(3, 95, 144);\n"
                                             "padding-bottom:1px;")
        self.tariffaComboBox_1.setObjectName("tariffaComboBox_1")
        self.tariffaComboBox_1.addItem("")
        self.tariffaComboBox_1.addItem("")
        self.tariffaComboBox_1.addItem("")
        # self.verticalLayout.addWidget(self.tariffaComboBox_1)

        self.orarioLabel = QtWidgets.QLabel(self.nuovaWidget)
        self.orarioLabel.setText("Orario: ")
        self.orarioLabel.setGeometry(QtCore.QRect(10, 240, 100, 34))

        self.orarioComboBox = QtWidgets.QComboBox(self.nuovaWidget)
        self.orarioComboBox.setGeometry(QtCore.QRect(60, 240, 200, 34))
        self.orarioComboBox.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:1px;")
        self.orarioComboBox.setFrame(True)
        self.orarioComboBox.setObjectName("orarioComboBox")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        self.orarioComboBox.addItem("")
        # self.verticalLayout.addWidget(self.orarioComboBox)

        self.mostraLabel = QtWidgets.QLabel(self.nuovaWidget)
        self.mostraLabel.setText("Mostra: ")
        self.mostraLabel.setGeometry(QtCore.QRect(10, 300, 100, 34))

        self.mostraComboBox = QtWidgets.QComboBox(self.nuovaWidget)
        self.mostraComboBox.setGeometry(QtCore.QRect(60, 300, 200, 34))
        self.mostraComboBox.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:1px;")
        self.mostraComboBox.setObjectName("mostraComboBox")

        self.inserisciButton = QtWidgets.QPushButton(self.nuovaWidget)
        self.inserisciButton.setGeometry(QtCore.QRect(300, 400, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inserisciButton.setFont(font)
        self.inserisciButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inserisciButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                           "border-radius:10px;color:rgb(242,233,216);")
        self.inserisciButton.setObjectName("inserisciButton")

        self.nuovaLabel = QtWidgets.QLabel(self.nuovaWidget)
        self.nuovaLabel.setGeometry(QtCore.QRect(20, 10, 351, 31))
        self.nuovaLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.nuovaLabel.setObjectName("nuovaLabel")
        self.tabWidget.addTab(self.nuovaWidget, "")

        self.prenotazioneWidget = QtWidgets.QWidget()
        self.prenotazioneWidget.setObjectName("prenotazioneWidget")
        self.prenotazioneLabel = QtWidgets.QLabel(self.prenotazioneWidget)
        self.prenotazioneLabel.setGeometry(QtCore.QRect(10, 0, 351, 21))
        self.prenotazioneLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.prenotazioneLabel.setObjectName("prenotazioneLabel")

        self.tariffaLabel_2 = QtWidgets.QLabel(self.prenotazioneWidget)
        self.tariffaLabel_2.setText("Tariffa: ")
        self.tariffaLabel_2.setGeometry(QtCore.QRect(10, 30, 100, 34))

        self.tariffaComboBox_2 = QtWidgets.QComboBox(self.prenotazioneWidget)
        self.tariffaComboBox_2.setGeometry(QtCore.QRect(60, 30, 200, 34))
        self.tariffaComboBox_2.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                             "color:rgb(3, 95, 144);\n"
                                             "border-bottom-color: rgb(3, 95, 144);\n"
                                             "padding-bottom:1px;")
        self.tariffaComboBox_2.setObjectName("tariffaComboBox_2")
        self.tariffaComboBox_2.addItem("")
        self.tariffaComboBox_2.addItem("")
        self.tariffaComboBox_2.addItem("")

        self.orarioLabel_2 = QtWidgets.QLabel(self.prenotazioneWidget)
        self.orarioLabel_2.setText("Orario: ")
        self.orarioLabel_2.setGeometry(QtCore.QRect(10, 70, 100, 34))

        self.orarioComboBox_2 = QtWidgets.QComboBox(self.prenotazioneWidget)
        self.orarioComboBox_2.setGeometry(QtCore.QRect(60, 70, 200, 34))
        self.orarioComboBox_2.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                            "color:rgb(3, 95, 144);\n"
                                            "border-bottom-color: rgb(3, 95, 144);\n"
                                            "padding-bottom:1px;")
        self.orarioComboBox_2.setFrame(True)
        self.orarioComboBox_2.setObjectName("orarioComboBox_2")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")
        self.orarioComboBox_2.addItem("")

        self.qrButton = QtWidgets.QPushButton(self.prenotazioneWidget)
        self.qrButton.setGeometry(QtCore.QRect(110, 210, 201, 31))
        self.qrButton.setText("Ottieni da QR code")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.qrButton.setFont(font)
        self.qrButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.qrButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                    "border-radius:10px;\n"
                                    "color:rgb(242,233,216);")

        self.codiceTextEdit = QtWidgets.QLineEdit(self.prenotazioneWidget)
        self.codiceTextEdit.setGeometry(QtCore.QRect(110, 270, 201, 34))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codiceTextEdit.setFont(font)
        self.codiceTextEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                          "border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:10px;")
        self.codiceTextEdit.setText("")
        self.codiceTextEdit.setObjectName("codiceTextEdit")

        self.insCodiceButton = QtWidgets.QPushButton(self.prenotazioneWidget)
        self.insCodiceButton.setGeometry(QtCore.QRect(110, 310, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.insCodiceButton.setFont(font)
        self.insCodiceButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insCodiceButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                           "border-radius:10px;\n"
                                           "color:rgb(242,233,216);")
        self.insCodiceButton.setObjectName("insCodiceButton")

        self.errorLabel = QtWidgets.QLabel(self.prenotazioneWidget)
        self.errorLabel.setGeometry(QtCore.QRect(120, 110, 171, 20))
        self.errorLabel.setStyleSheet("color: rgb(247, 8, 8);")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")

        self.tabWidget.addTab(self.prenotazioneWidget, "")

        self.logo_label = QtWidgets.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(380, 40, 61, 61))
        self.logo_label.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("media/luigi/ubuntu/VM condivisa/../Porojecto/View/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")

        self.Exit = QtWidgets.QPushButton(self.frame)
        self.Exit.setGeometry(QtCore.QRect(420, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Exit.setFont(font)
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit.setStyleSheet("background-color: rgb(229, 82, 2); \n"
                                "border-radius:10px;\n"
                                "color:rgb(3, 95, 144);")
        self.Exit.setFlat(True)
        self.Exit.setObjectName("Exit")
        UI_Visite.setCentralWidget(self.centralwidget)

        self.retranslateUi(UI_Visite)
        self.comboBox.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(0)
        self.orarioComboBox.setCurrentIndex(-1)
        self.orarioComboBox_2.setCurrentIndex(-1)
        self.tariffaComboBox_1.setCurrentIndex(-1)
        self.tariffaComboBox_2.setCurrentIndex(-1)
        self.mostraComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UI_Visite)

    def retranslateUi(self, UI_Visite):
        _translate = QtCore.QCoreApplication.translate
        UI_Visite.setWindowTitle(_translate("UI_Visite", "MainWindow"))
        self.Minimize.setText(_translate("UI_Visite", "-"))
        self.Title.setText(_translate("UI_Visite", "Gestione Visite"))
        self.Back.setText(_translate("UI_Visite", "<-"))
        self.comboBox.setItemText(0, _translate("UI_Visite", "Modifica Password"))
        self.comboBox.setItemText(1, _translate("UI_Visite", "Logout"))
        self.User.setText(_translate("UI_Visite", "NOMEUTENTE"))
        self.tariffaComboBox_1.setItemText(0, _translate("UI_Visite", "intero"))
        self.tariffaComboBox_1.setItemText(1, _translate("UI_Visite", "ridotto"))
        self.tariffaComboBox_1.setItemText(2, _translate("UI_Visite", "gratuito"))
        self.telefonoTextEdit.setPlaceholderText(_translate("UI_Visite", "Numero di Telefono"))
        self.nomeTextEdit.setPlaceholderText(_translate("UI_Visite", "Nominativo"))
        self.tariffaComboBox_2.setItemText(0, _translate("UI_Visite", "intero"))
        self.tariffaComboBox_2.setItemText(1, _translate("UI_Visite", "ridotto"))
        self.tariffaComboBox_2.setItemText(2, _translate("UI_Visite", "gratuito"))
        self.nomeTextEdit.setPlaceholderText(_translate("UI_Visite", "Nominativo"))
        self.codiceTextEdit.setPlaceholderText(_translate("UI_Visite", "Codice"))
        self.orarioComboBox.setItemText(0, _translate("UI_Visite", "9:00"))
        self.orarioComboBox.setItemText(1, _translate("UI_Visite", "9:30"))
        self.orarioComboBox.setItemText(2, _translate("UI_Visite", "10:00"))
        self.orarioComboBox.setItemText(3, _translate("UI_Visite", "10:30"))
        self.orarioComboBox.setItemText(4, _translate("UI_Visite", "11:00"))
        self.orarioComboBox.setItemText(5, _translate("UI_Visite", "11:30"))
        self.orarioComboBox.setItemText(6, _translate("UI_Visite", "12:00"))
        self.orarioComboBox.setItemText(7, _translate("UI_Visite", "12:30"))
        self.orarioComboBox.setItemText(8, _translate("UI_Visite", "13:00"))
        self.orarioComboBox.setItemText(9, _translate("UI_Visite", "13:30"))
        self.orarioComboBox.setItemText(10, _translate("UI_Visite", "14:00"))
        self.orarioComboBox.setItemText(11, _translate("UI_Visite", "14:30"))
        self.orarioComboBox.setItemText(12, _translate("UI_Visite", "15:00"))
        self.orarioComboBox.setItemText(13, _translate("UI_Visite", "15:30"))
        self.orarioComboBox.setItemText(14, _translate("UI_Visite", "16:00"))
        self.orarioComboBox.setItemText(15, _translate("UI_Visite", "16:30"))
        self.orarioComboBox.setItemText(16, _translate("UI_Visite", "17:00"))
        self.orarioComboBox.setItemText(17, _translate("UI_Visite", "17:30"))
        self.orarioComboBox.setItemText(18, _translate("UI_Visite", "18:00"))
        self.orarioComboBox.setItemText(19, _translate("UI_Visite", "18:30"))
        self.inserisciButton.setText(_translate("UI_Visite", "Inserisci"))
        self.nuovaLabel.setText(_translate("UI_Visite", ""))
        self.orarioComboBox_2.setCurrentText(_translate("UI_Visite", "9:00"))
        self.orarioComboBox_2.setItemText(0, _translate("UI_Visite", "9:00"))
        self.orarioComboBox_2.setItemText(1, _translate("UI_Visite", "9:30"))
        self.orarioComboBox_2.setItemText(2, _translate("UI_Visite", "10:00"))
        self.orarioComboBox_2.setItemText(3, _translate("UI_Visite", "10:30"))
        self.orarioComboBox_2.setItemText(4, _translate("UI_Visite", "11:00"))
        self.orarioComboBox_2.setItemText(5, _translate("UI_Visite", "11:30"))
        self.orarioComboBox_2.setItemText(6, _translate("UI_Visite", "12:00"))
        self.orarioComboBox_2.setItemText(7, _translate("UI_Visite", "12:30"))
        self.orarioComboBox_2.setItemText(8, _translate("UI_Visite", "13:00"))
        self.orarioComboBox_2.setItemText(9, _translate("UI_Visite", "13:30"))
        self.orarioComboBox_2.setItemText(10, _translate("UI_Visite", "14:00"))
        self.orarioComboBox_2.setItemText(11, _translate("UI_Visite", "14:30"))
        self.orarioComboBox_2.setItemText(12, _translate("UI_Visite", "15:00"))
        self.orarioComboBox_2.setItemText(13, _translate("UI_Visite", "15:30"))
        self.orarioComboBox_2.setItemText(14, _translate("UI_Visite", "16:00"))
        self.orarioComboBox_2.setItemText(15, _translate("UI_Visite", "16:30"))
        self.orarioComboBox_2.setItemText(16, _translate("UI_Visite", "17:00"))
        self.orarioComboBox_2.setItemText(17, _translate("UI_Visite", "17:30"))
        self.orarioComboBox_2.setItemText(18, _translate("UI_Visite", "18:00"))
        self.orarioComboBox_2.setItemText(19, _translate("UI_Visite", "18:30"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nuovaWidget), _translate("UI_Visite", "Inserisci Nuova"))
        self.prenotazioneLabel.setText(_translate("UI_Visite", ""))
        self.insCodiceButton.setText(_translate("UI_Visite", "Inserisci Codice"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prenotazioneWidget),
                                  _translate("UI_Visite", "Visita Prenotata"))
        self.Exit.setText(_translate("UI_Visite", "X"))
