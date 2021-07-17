import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from mostra.controller.ControllerMostra import ControllerMostra
from prenotazione.controller.ControllerPrenotazione import ControllerPrenotazione


# classe di correlazione tra le funzionalità del controller e le scelte effettuate dall'utente tramite
# l'input/output dell'interfaccia grafica relativa alla visualizzazione della scheda completa della prenotazione
class UiPrenotazioneComplete(object):
    def __init__(self, idPrenotazione):
        self.controllerPrenotazione = ControllerPrenotazione()
        self.controllerPrenotazione.model = \
        self.controllerPrenotazione.getPrenotazioneByFields({'codice': idPrenotazione})[0]
        self.controllerPrenotazione.model.checkPrenotazioneExists()  # assegno l'attributo ID
        self.listaIdMostre = []

    # metodo per il caricamento delle mostre attive in caso di eventuale modifica della prenotazione
    def caricaMostre(self):
        try:
            controllerMostre = ControllerMostra()
            listaMostre = controllerMostre.mostreInCorso()
            if listaMostre:
                for mostra in listaMostre:
                    self.mostraComboBox.addItem(mostra.titolo)
                    self.listaIdMostre.append(mostra.ID)
        except Exception:
            raise

    # metodo per impostare le label dell'interfaccia con gli attuali valori della prenotazione presa in esame
    def setLabels(self):
        self.nomeLabel.setText(self.controllerPrenotazione.model.getNominativo())
        self.codiceLabel.setText(str(self.controllerPrenotazione.model.getCodice()))
        self.telefonoLabel.setText(str(self.controllerPrenotazione.model.getTelefono()))
        if not self.controllerPrenotazione.model.getValidita():
            self.validitaLabel.setText("Non valida")
        idMostra = self.controllerPrenotazione.getIDMostra()
        for mostra in self.listaIdMostre:
            if mostra == idMostra:
                self.mostraComboBox.setCurrentIndex(self.listaIdMostre.index(mostra))
        self.dataVisitaButton.setText(self.controllerPrenotazione.model.getDataVisita())
        self.dataPrenotazioneButton.setText(self.controllerPrenotazione.model.getDataPrenotazione())

    # metodo per eliminare la prenotazione dal database
    def eliminaFunction(self):
        try:
            self.controllerPrenotazione.deletePrenotazione()
            self.msgLabel.setStyleSheet("color: rgb(34, 177, 76)")
            self.msgLabel.setText("Prenotazione aggiornata con successo")
        except Exception as e:
            self.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.msgLabel.setText(e.args[0])

    # metodo per modificare la mostra nel database
    def modificaFunction(self):
        if self.nomeLabel.text() and self.telefonoLabel.text():
            idMostra = self.listaIdMostre[self.mostraComboBox.currentIndex()]
            dati = {
                'nominativo': self.nomeLabel.text(),
                'telefono': self.telefonoLabel.text(),
                'ID_mostra': idMostra,
                'data_prenotazione': self.dataPrenotazioneButton.text(),
                'data_visita': self.dataVisitaButton.text()
            }
            try:
                self.controllerPrenotazione.updatePrenotazioneByFields(self.controllerPrenotazione.model.getCodice(),
                                                                       dati)
                self.msgLabel.setStyleSheet("color: rgb(34, 177, 76)")
                self.msgLabel.setText("Prenotazione aggiornata con successo")
            except Exception as e:
                self.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.msgLabel.setText(e.args[0])
        else:
            self.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.msgLabel.setText('Inserisci tutti i dati')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background-color: rgb(242,233,216)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
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
        self.closeButton.setObjectName("Exit")

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(110, 10, 230, 16))
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
        self.msgLabel.setGeometry(20, 80, 300, 20)

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

        self.mostraComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mostraComboBox.setFont(font)
        self.mostraComboBox.setStyleSheet("color:rgb(3, 95, 144);")
        self.mostraComboBox.setObjectName("mostraComboBox")
        self.gridLayout.addWidget(self.mostraComboBox, 2, 1, 1, 1)

        self.telefonoLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.telefonoLabel.setFont(font)
        self.telefonoLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.telefonoLabel.setObjectName("telefonoLabel")
        self.gridLayout.addWidget(self.telefonoLabel, 2, 0, 1, 1)

        self.dataPrenotazioneButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataPrenotazioneButton.sizePolicy().hasHeightForWidth())
        self.dataPrenotazioneButton.setSizePolicy(sizePolicy)
        self.dataPrenotazioneButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataPrenotazioneButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                                  "border-radius:10px;\n"
                                                  "color:rgb(242,233,216);")
        self.dataPrenotazioneButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataPrenotazioneButton.setMenu(QtWidgets.QMenu(self.dataPrenotazioneButton))
        self.calendar_1 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_1.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataPrenotazioneButton)
        action.setDefaultWidget(self.calendar_1)
        self.dataPrenotazioneButton.menu().addAction(action)
        self.dataPrenotazioneButton.setObjectName("dataPrenotazioneButton")
        self.gridLayout.addWidget(self.dataPrenotazioneButton, 1, 0, 1, 1)
        self.calendar_1.clicked.connect(lambda: self.get_date(self.calendar_1, self.dataPrenotazioneButton))

        self.dataVisitaButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataVisitaButton.sizePolicy().hasHeightForWidth())
        self.dataVisitaButton.setSizePolicy(sizePolicy)
        self.dataVisitaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataVisitaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                            "border-radius:10px;\n"
                                            "color:rgb(242,233,216);")
        self.dataVisitaButton.setObjectName("dataFineButton")
        self.dataVisitaButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataVisitaButton.setMenu(QtWidgets.QMenu(self.dataVisitaButton))
        self.calendar_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_2.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataVisitaButton)
        action.setDefaultWidget(self.calendar_2)
        self.dataVisitaButton.menu().addAction(action)
        self.dataVisitaButton.setObjectName("dataVisitaButton")
        self.gridLayout.addWidget(self.dataVisitaButton, 1, 1, 1, 1)
        oggi = datetime.date.today().strftime('%Y-%m-%d')
        self.calendar_2.setMinimumDate(self.calendar_1.selectedDate())
        self.calendar_2.clicked.connect(lambda: self.get_date(self.calendar_2, self.dataVisitaButton))

        self.nomeLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nomeLabel.setFont(font)
        self.nomeLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.nomeLabel.setObjectName("nomeLabel")
        self.gridLayout.addWidget(self.nomeLabel, 0, 0, 1, 1)
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

        self.validitaLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.validitaLabel.setFont(font)
        self.validitaLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.validitaLabel.setObjectName("validitaLabel")
        self.verticalLayout.addWidget(self.validitaLabel)
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

        MainWindow.setCentralWidget(self.centralwidget)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Prenotazione"))
        self.minimizeButton.setText(_translate("MainWindow", "-"))
        self.closeButton.setText(_translate("MainWindow", "X"))
        self.titleLabel.setText(_translate("MainWindow", "Visualizza Scheda Prenotazione"))
        self.accountMenu.setItemText(0, _translate("MainWindow", "Home"))
        self.accountMenu.setItemText(1, _translate("MainWindow", "Logout"))
        self.userLabel.setText(_translate("MainWindow", "NOMEUTENTE"))
        self.telefonoLabel.setText(_translate("MainWindow", "Telefono"))
        self.dataVisitaButton.setText(_translate("MainWindow", "Data Visita"))
        self.dataPrenotazioneButton.setText(_translate("MainWindow", "Data Prenotazione"))
        self.nomeLabel.setText(_translate("MainWindow", "NOMINATIVO"))
        self.codiceLabel.setText(_translate("MainWindow", "Codice"))
        self.validitaLabel.setText(_translate("MainWindow", "Valida"))
        self.modificaButton.setText(_translate("MainWindow", "Modifica Prenotazione"))
        self.eliminaButton.setText(_translate("MainWindow", "Termina Prenotazione"))

    # metodo per scrivere la data scelta sul calendar widget sopra il bottone passato come parametro
    def get_date(self, calendar, button):
        date = calendar.selectedDate()
        button.setText(date.toString("yyyy-MM-dd"))
