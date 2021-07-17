import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

from Configurazione.StrutturaMuseo import StrutturaMuseo
from esposizione.controller.ControllerEsposizione import ControllerEsposizione
from esposizione.model.Esposizione import Esposizione
from mostra.controller.ControllerMostra import ControllerMostra
from opera.ControllerOpera.GestioneCatalogo import GestioneCatalogo

# classe di correlazione tra le funzionalità del controller e le scelte effettuate dall'utente tramite
# l'input/output dell'interfaccia grafica relativa alla visualizzazione di una singola scheda mostra completa
class UiMostraComplete(object):
    def __init__(self, idMostra):
        self.listaIdOpere = []
        self.controllerMostra = ControllerMostra()
        self.controllerEsposizione = ControllerEsposizione()
        self.controllerOpera = GestioneCatalogo()
        self.controllerMostra.model = self.controllerMostra.setListaMostre({'ID': idMostra})[0]
        self.controllerMostra.model.checkMostraExists()       #assegno l'attributo ID

    # metodo per la configurazione delle label mediante i valori della mostra presa in esame
    def setLabels(self):
        self.titoloLabel.setText(self.controllerMostra.model.getTitolo())
        self.codiceLabel.setText(str(self.controllerMostra.model.getID()))
        self.edizioneLabel.setText(str(self.controllerMostra.model.getEdizione()))
        self.salaLabel.setCurrentText(self.controllerMostra.model.getSala())
        self.prezzoLabel.setText(str(self.controllerMostra.model.getPrezzo()))
        self.dataInizioButton.setText(self.controllerMostra.model.getDataInizio())
        self.dataFineButton.setText(self.controllerMostra.model.getDataFine())
        listaExp = self.controllerEsposizione.getEsposizioneByFields({'ID_mostra': self.controllerMostra.model.getID()})

        for esposizione in listaExp:
            for i in range(0,len(self.listaIdOpere)):
                if esposizione.codiceOpera is self.listaIdOpere[i]:
                    self.operaList.item(i).setSelected(True)



    # metodo per caricare nelle combobox le sale del museo (per inserire nuove mostre o filtrare in funzione
    # di esse)
    def caricaSale(self):
        strutturaMuseo = StrutturaMuseo()
        listaSale = strutturaMuseo.getSale()
        for sala in listaSale:
            self.salaLabel.addItem(sala)

    # metodo per caricare i nomi delle opere presenti nel catalogo in modo da poter essere selezionate
    # per una possibile nuova mostra
    def caricaOpere(self):
        try:
            self.nomiOpere = self.controllerOpera.getOpereFiltrate()
            if self.nomiOpere:
                for opera in self.nomiOpere:
                    self.operaList.addItem(opera.titolo)
                    self.listaIdOpere.append(opera.codice)
        except Exception:
            raise


    # metodo per terminare una mostra
    def terminaFunction(self):
        oggi = datetime.date.today().strftime("%Y-%m-%d")
        try:
            self.controllerMostra.modificaDatoMostra('data_fine', oggi)
            expDaTerminare = self.controllerEsposizione.getEsposizioneByFields({'ID_mostra': self.controllerMostra.model.getID()})
            for exp in expDaTerminare:
                self.controllerEsposizione.model = exp
                self.controllerEsposizione.modificaFineEsposizione(oggi)
            self.controllerEsposizione.model= Esposizione()
            self.msgLabel.setStyleSheet("color: rgb(34, 177, 76)")
            self.msgLabel.setText("Mostra terminata con successo")
        except Exception as e:
            self.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.msgLabel.setText(e.args[0])

    # metodo per modificare i campi di una mostra
    def modificaFunction(self):
        if self.titoloLabel.text() and self.edizioneLabel.text() and self.salaLabel.currentText() and self.prezzoLabel.text():
            dati = {
                'titolo': self.titoloLabel.text(),
                'edizione': self.edizioneLabel.text(),
                'sala': self.salaLabel.currentText(),
                'prezzo': self.prezzoLabel.text(),
                'data_inizio': self.dataInizioButton.text(),
                'data_fine': self.dataFineButton.text()
            }
            oldDati= {
                'titolo': self.controllerMostra.model.getTitolo(),
                'edizione': self.controllerMostra.model.getEdizione(),
                'sala': self.controllerMostra.model.getSala(),
                'prezzo': self.controllerMostra.model.getPrezzo(),
                'data_inizio': self.controllerMostra.model.getDataInizio(),
                'data_fine': self.controllerMostra.model.getDataFine()
            }
            idMostra = self.codiceLabel.text()
            selIndexes = self.operaList.selectedIndexes()

            try:
                self.controllerMostra.modificaMostra(self.controllerMostra.model.getID(), dati)
                self.controllerEsposizione.eliminaEsposizione(self.controllerMostra.model.getID())
                expDaTerminare = self.controllerEsposizione.getEsposizioneByFields(
                    {'ID_mostra': self.controllerMostra.model.getID()})
                for sel in selIndexes:
                    codiceOpera = self.nomiOpere[sel.row()].getCodice()
                    self.controllerEsposizione.setModel(dati['data_inizio'], codiceOpera, idMostra,dati['data_fine'])

                    self.controllerEsposizione.saveEsposizione()

                self.msgLabel.setStyleSheet("color: rgb(33, 163, 21);")
                self.msgLabel.setText("Mostra modificata")
                oldDateFine = []
                try:
                    for exp in expDaTerminare:
                        self.controllerEsposizione.model = exp
                        oldDateFine.append(exp.dataFine)
                        self.controllerEsposizione.modificaFineEsposizione(self.dataFineButton.text())
                    self.controllerEsposizione.model = Esposizione()
                    self.msgLabel.setStyleSheet("color: rgb(34, 177, 76)")
                    self.msgLabel.setText("Mostra aggiornata con successo")
                except Exception as e:
                    self.controllerEsposizione.eliminaEsposizione(idMostra)
                    self.controllerMostra.modificaMostra(self.controllerMostra.model.getID(), oldDati)
                    for exp, data in zip(expDaTerminare,oldDateFine):
                        self.controllerEsposizione = exp
                        self.controllerEsposizione.saveEsposizione()
                    self.controllerEsposizione.model = Esposizione()
                    self.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
                    self.msgLabel.setText(e.args[0])
            except Exception as e:
                self.controllerMostra.modificaMostra(self.controllerMostra.model.getID(), oldDati)
                self.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.msgLabel.setText(e.args[0])
        else:
            self.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.msgLabel.setText('Inserisci tutti i dati')


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background-color: rgb(242,233,216)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)

        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 581))
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
        self.titleLabel.setGeometry(QtCore.QRect(140, 10, 190, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.titleLabel.setObjectName("titleLabel")

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

        self.accountMenu = QtWidgets.QComboBox(self.frame)
        self.accountMenu.setGeometry(QtCore.QRect(10, 60, 141, 22))
        self.accountMenu.setStyleSheet("color: rgb(65, 65, 65);")
        self.accountMenu.setCurrentText("")
        self.accountMenu.setFrame(True)
        self.accountMenu.setObjectName("accountMenu")
        self.accountMenu.addItem("")
        self.accountMenu.addItem("")

        self.userLabel = QtWidgets.QLabel(self.frame)
        self.userLabel.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.userLabel.setObjectName("userLabel")

        self.logoLabel = QtWidgets.QLabel(self.frame)
        self.logoLabel.setGeometry(QtCore.QRect(380, 40, 61, 61))
        self.logoLabel.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logoLabel.setText("")
        #self.logoLabel.setPixmap(QtGui.QPixmap("../../PycharmProjects/pythonProject/Porojecto/View/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")

        self.msgLabel = QtWidgets.QLabel(self.frame)
        self.msgLabel.setGeometry(20, 80, 241, 20)

        self.schedaFrame = QtWidgets.QFrame(self.frame)
        self.schedaFrame.setGeometry(QtCore.QRect(10, 100, 431, 471))
        self.schedaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedaFrame.setObjectName("schedaFrame")

        self.imgLabel = QtWidgets.QLabel(self.schedaFrame)
        self.imgLabel.setGeometry(QtCore.QRect(10, 0, 221, 111))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")

        self.gridLayoutWidget = QtWidgets.QWidget(self.schedaFrame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 9, 411, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.prezzoLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prezzoLabel.setFont(font)
        self.prezzoLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.prezzoLabel.setObjectName("prezzoLabel")
        self.gridLayout.addWidget(self.prezzoLabel, 2, 1, 1, 1)

        self.edizioneLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edizioneLabel.setFont(font)
        self.edizioneLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.edizioneLabel.setObjectName("edizioneLabel")
        self.gridLayout.addWidget(self.edizioneLabel, 2, 0, 1, 1)

        self.dataInizioButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataInizioButton.sizePolicy().hasHeightForWidth())
        self.dataInizioButton.setSizePolicy(sizePolicy)
        self.dataInizioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataInizioButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                            "border-radius:10px;\n"
                                            "color:rgb(242,233,216);")
        self.dataInizioButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataInizioButton.setMenu(QtWidgets.QMenu(self.dataInizioButton))
        self.calendar_1 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_1.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataInizioButton)
        action.setDefaultWidget(self.calendar_1)
        self.dataInizioButton.menu().addAction(action)
        self.dataInizioButton.setObjectName("dataInizioButton")
        self.gridLayout.addWidget(self.dataInizioButton, 1, 0, 1, 1)
        self.calendar_1.clicked.connect(lambda: self.get_date(self.calendar_1, self.dataInizioButton))

        self.dataFineButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFineButton.sizePolicy().hasHeightForWidth())
        self.dataFineButton.setSizePolicy(sizePolicy)
        self.dataFineButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataFineButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                          "border-radius:10px;\n"
                                          "color:rgb(242,233,216);")
        self.dataFineButton.setObjectName("dataFineButton")
        self.dataFineButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataFineButton.setMenu(QtWidgets.QMenu(self.dataFineButton))
        self.calendar_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_2.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataFineButton)
        action.setDefaultWidget(self.calendar_2)
        self.dataFineButton.menu().addAction(action)
        self.dataFineButton.setObjectName("dataFineButton")
        self.gridLayout.addWidget(self.dataFineButton, 1, 1, 1, 1)
        oggi = datetime.date.today().strftime('%Y-%m-%d')
        if self.dataInizioButton.text() >= oggi:
            self.calendar_2.setMinimumDate(self.calendar_1.selectedDate())
        else:
            self.calendar_2.setMinimumDate(QDate.currentDate())
        self.calendar_2.clicked.connect(lambda: self.get_date(self.calendar_2, self.dataFineButton))

        self.titoloLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titoloLabel.setFont(font)
        self.titoloLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.titoloLabel.setObjectName("titoloLabel")
        self.gridLayout.addWidget(self.titoloLabel, 0, 0, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.codiceLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.codiceLabel.setFont(font)
        self.codiceLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.codiceLabel.setObjectName("codiceLabel")
        self.verticalLayout.addWidget(self.codiceLabel)

        self.salaLabel = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.salaLabel.setFont(font)
        self.salaLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.salaLabel.setObjectName("salaLabel")
        self.verticalLayout.addWidget(self.salaLabel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.modificaButton = QtWidgets.QPushButton(self.schedaFrame)
        self.modificaButton.setGeometry(QtCore.QRect(10, 430, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.modificaButton.setFont(font)
        self.modificaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                          "border-radius:10px;\n"
                                          "color:rgb(242,233,216);")
        self.modificaButton.setObjectName("modificaButton")

        self.eliminaButton = QtWidgets.QPushButton(self.schedaFrame)
        self.eliminaButton.setGeometry(QtCore.QRect(220, 430, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.eliminaButton.setFont(font)
        self.eliminaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminaButton.setStyleSheet("background-color:rgb(229, 82, 2);\n"
                                         "border-radius:10px;\n"
                                         "color:rgb(242,233,216);")
        self.eliminaButton.setObjectName("eliminaButton")

        self.operaList = QtWidgets.QListWidget(self.schedaFrame)
        self.operaList.setGeometry(QtCore.QRect(10, 260, 411, 161))
        self.operaList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.operaList.setStyleSheet("color: rgb(3, 95, 144);")
        self.operaList.setObjectName("operaList")

        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.accountMenu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mostra"))
        self.minimizeButton.setText(_translate("MainWindow", "-"))
        self.closeButton.setText(_translate("MainWindow", "X"))
        self.titleLabel.setText(_translate("MainWindow", "Visualizza Scheda Mostra"))
        self.accountMenu.setItemText(0, _translate("MainWindow", "Modifica Password"))
        self.accountMenu.setItemText(1, _translate("MainWindow", "Logout"))
        self.userLabel.setText(_translate("MainWindow", "NOMEUTENTE"))
        self.prezzoLabel.setText(_translate("MainWindow", "Prezzo"))
        self.edizioneLabel.setText(_translate("MainWindow", "Edizione"))
        self.dataFineButton.setText(_translate("MainWindow", "Data Fine"))
        self.dataInizioButton.setText(_translate("MainWindow", "Data Inizio"))
        self.titoloLabel.setText(_translate("MainWindow", "TITOLO"))
        self.codiceLabel.setText(_translate("MainWindow", "Codice"))
        self.salaLabel.setPlaceholderText(_translate("MainWindow", "Sala"))
        self.modificaButton.setText(_translate("MainWindow", "Modifica Mostra"))
        self.eliminaButton.setText(_translate("MainWindow", "Termina Mostra"))


    # metodo per scrivere la data scelta sul calendar widget sul bottone passato come parametro
    def get_date(self, calendar, button):
        date = calendar.selectedDate()
        button.setText(str(date.year()) + "-" + str(date.month()) + "-" + str(date.day()))
