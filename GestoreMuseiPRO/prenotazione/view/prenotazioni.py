from datetime import date

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap

from Qr.GestioneQr import GestioneQr
from View.PopUp import PopUp
from mostra.controller.ControllerMostra import ControllerMostra
from prenotazione.controller.ControllerPrenotazione import ControllerPrenotazione

# classe di correlazione tra le funzionalità del controller e le scelte effettuate dall'utente tramite
# l'input/output dell'interfaccia grafica relativa alla visualizzazione della finestra di aggiunta prenotazione
# e quella di filtraggio delle prenotazioni presenti nel database

class Ui_Prenotazione(object):
    def __init__(self):
        self.controller = ControllerPrenotazione()
        self.listaIdMostre = []

    # metodo per caricare le mostre attive (sia per l'aggiunta di una nuova prenotazione corrispondente
    # che per filtrare tra le prenotazioni presenti in funzione di esse)
    def caricaMostre(self):
        try:
            controllerMostre = ControllerMostra()
            listaMostre = controllerMostre.mostreInCorso()
            self.mostraFilterComboBox.addItem("")
            if listaMostre:
                for mostra in listaMostre:
                    self.mostraComboBox.addItem(mostra.titolo)
                    self.mostraFilterComboBox.addItem(mostra.titolo)
                    self.listaIdMostre.append(mostra.ID)
        except Exception:
            raise

    # metodo per salvare una nuova prenotazione
    def savePrenotazione(self):
        idMostra = self.listaIdMostre[self.mostraComboBox.currentIndex()]
        dataPrenotazione = date.today().strftime('%Y-%m-%d')
        dataVisita = self.dataButton.text()
        nominativo = self.nominativoLineEdit.text()
        telefono = self.telefonoLineEdit.text()
        if dataVisita != 'Data visita' and nominativo and telefono:
            try:
                self.controller.setModel(None, dataPrenotazione, dataVisita, nominativo, telefono, idMostra)
                self.controller.savePrenotazione()
                if self.controller.model.checkPrenotazioneExists():
                    self.qrPopup = PopUp()
                    self.qrFrame = QtWidgets.QFrame(self.qrPopup)
                    self.qrLabel = QtWidgets.QLabel(self.qrFrame)
                    pixmap = QPixmap(GestioneQr.generateQr(str(self.controller.getCodice())))
                    self.qrLabel.setPixmap(pixmap)
                    self.qrLabel.setGeometry(QtCore.QRect(10, 10, pixmap.width(), pixmap.height()))
                    self.qrPopup.resize(pixmap.width() + 20, pixmap.height() + 60)
                    self.qrPopup.setStyleSheet("background-color: rgb(242,233,216)")
                    self.qrCloseButton = QtWidgets.QPushButton(self.qrFrame)
                    self.qrCloseButton.setStyleSheet("background-color: rgb(229, 82, 2); \n"
                                                     "border-radius:10px;")
                    self.qrCloseButton.setGeometry(QtCore.QRect(10, 20 + pixmap.height(), pixmap.width(), 30))
                    self.qrCloseButton.setText("Chiudi Popup")
                    self.qrCloseButton.clicked.connect(self.qrPopup.close)
                    self.qrPopup.show()

            except Exception as e:
                self.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.nuovaLabel.setText(e.args[0])
        else:
            self.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.nuovaLabel.setText('Per favore inserisci tutti i dati!')

    # metodo che restituisce la lista delle prenotazioni filtrate secondo i criteri forniti dall'utente
    def getListaPrenotazioni(self):
        filtri = {}
        if self.idFilterLineEdit.text():
            filtri['codice'] = self.idFilterLineEdit.text()
        if self.nominativoFilterLineEdit.text():
            filtri['nominativo'] = self.nominativoFilterLineEdit.text()
        if self.telefonoFilterLineEdit.text():
            filtri['telefono'] = self.telefonoFilterLineEdit.text()
        if self.mostraFilterComboBox.currentIndex():
            filtri['ID_mostra'] = self.listaIdMostre[self.mostraFilterComboBox.currentIndex() - 1]
        tupleAppoggio = ["", ""]

        if self.dataMinButton.text() != 'Data Visita Min':
            tupleAppoggio[0] = self.dataMinButton.text()
        if self.dataMaxButton.text() != 'Data Visita Max':
            tupleAppoggio[1] = self.dataMaxButton.text()
        if tupleAppoggio != ["", ""]:
            filtri['data_visita'] = tuple(tupleAppoggio)
        tupleAppoggio = ["", ""]
        if self.prenotazioneMinButton.text() != 'Data Prenotazione Min':
            tupleAppoggio[0] = self.prenotazioneMinButton.text()
        if self.prenotazioneMaxButton.text() != 'Data Prenotazione Max':
            tupleAppoggio[1] = self.prenotazioneMaxButton.text()
        if tupleAppoggio != ["", ""]:
            filtri['data_prenotazione'] = tuple(tupleAppoggio)
        try:
            return self.controller.getPrenotazioneByFields(filtri)
        except Exception:
            raise

    # metodo che restituisce all'utente la prenotazione corrispondente al codice QR fornito
    def getPrenotazioneQr(self, codice):
        codice = GestioneQr.readQr(codice)
        try:
            return self.controller.getPrenotazioneByFields({'codice': codice})
        except Exception:
            raise

    def setupUi(self, UI_Prenotazione):
        UI_Prenotazione.setObjectName("UI_Prenotazione")
        UI_Prenotazione.resize(480, 606)
        UI_Prenotazione.setStyleSheet("background-color: rgb(242,233,216)")

        self.centralwidget = QtWidgets.QWidget(UI_Prenotazione)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 571))
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
        self.closeButton.setObjectName("closeButton")

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(150, 10, 161, 16))
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

        self.tab = QtWidgets.QTabWidget(self.frame)
        self.tab.setGeometry(QtCore.QRect(10, 90, 431, 481))
        self.tab.setStyleSheet("color:rgb(3, 95, 144);")
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab.setObjectName("tab")

        self.inserisciWidget = QtWidgets.QWidget()
        self.inserisciWidget.setObjectName("inserisciWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.inserisciWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 361, 370))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.inserisciLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.inserisciLayout.setContentsMargins(0, 0, 0, 0)
        self.inserisciLayout.setObjectName("inserisciLayout")

        self.dataButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataButton.sizePolicy().hasHeightForWidth())
        self.dataButton.setSizePolicy(sizePolicy)
        self.dataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                      "border-radius:10px;\n"
                                      "color:rgb(242,233,216);")
        self.dataButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataButton.setMenu(QtWidgets.QMenu(self.dataButton))
        self.calendar = QtWidgets.QCalendarWidget(self.frame)
        self.calendar.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataButton)
        action.setDefaultWidget(self.calendar)
        self.dataButton.menu().addAction(action)
        self.calendar.setMinimumDate(QDate.currentDate())
        self.calendar.clicked.connect(lambda: self.get_date(self.calendar, self.dataButton))
        self.dataButton.setObjectName("dataButton")
        self.inserisciLayout.addWidget(self.dataButton)

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
        self.inserisciLayout.addWidget(self.nominativoLineEdit)

        self.telefonoLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.telefonoLineEdit.setFont(font)
        self.telefonoLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:2px solid rgba(0,0,0,0);\n"
                                            "color:rgb(3, 95, 144);\n"
                                            "border-bottom-color: rgb(3, 95, 144);\n"
                                            "padding-bottom:10px;")
        self.telefonoLineEdit.setText("")
        self.telefonoLineEdit.setObjectName("telefonoLineEdit")
        self.inserisciLayout.addWidget(self.telefonoLineEdit)

        self.mostraComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.mostraComboBox.setObjectName("mostraComboBox")
        self.mostraComboBox.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:1px;")
        self.inserisciLayout.addWidget(self.mostraComboBox)
        self.mostraComboBox.setCurrentIndex(0)

        self.inserisciButton = QtWidgets.QPushButton(self.inserisciWidget)
        self.inserisciButton.setGeometry(QtCore.QRect(300, 410, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inserisciButton.setFont(font)
        self.inserisciButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inserisciButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                            "border-radius:10px;\n"
                                            "color:rgb(242,233,216);")
        self.inserisciButton.setObjectName("inserisciButton")

        self.nuovaLabel = QtWidgets.QLabel(self.inserisciWidget)
        self.nuovaLabel.setGeometry(QtCore.QRect(60, 10, 340, 21))
        self.nuovaLabel.setStyleSheet("color: rgb(85,66,26)")
        self.nuovaLabel.setObjectName("nuovaLabel")
        self.tab.addTab(self.inserisciWidget, "")

        self.visualizzaWidget = QtWidgets.QWidget()
        self.visualizzaWidget.setObjectName("visualizzaWidget")

        self.visualizzaButton = QtWidgets.QPushButton(self.visualizzaWidget)
        self.visualizzaButton.setGeometry(QtCore.QRect(210, 410, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.visualizzaButton.setFont(font)
        self.visualizzaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualizzaButton.setStyleSheet("background-color: rgb(229, 82, 2);\n"
                                            "border-radius:10px;\n"
                                            "color:rgb(242,233,216);")
        self.visualizzaButton.setObjectName("visualizzaButton")

        self.visualizzaLabel = QtWidgets.QLabel(self.visualizzaWidget)
        self.visualizzaLabel.setGeometry(QtCore.QRect(10, 0, 221, 21))
        self.visualizzaLabel.setStyleSheet("")
        self.visualizzaLabel.setObjectName("visualizzaLabel")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.visualizzaWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 361, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.idFilterLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.idFilterLineEdit.setFont(font)
        self.idFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:2px solid rgba(0,0,0,0);\n"
                                            "color:rgb(3, 95, 144);\n"
                                            "border-bottom-color: rgb(3, 95, 144);\n"
                                            "padding-bottom:10px;")
        self.idFilterLineEdit.setText("")
        self.idFilterLineEdit.setObjectName("idFilterLineEdit")
        self.verticalLayout_2.addWidget(self.idFilterLineEdit)

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

        self.mostraFilterComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.mostraFilterComboBox.setObjectName("mostraFilterComboBox")
        self.mostraFilterComboBox.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                                "color:rgb(3, 95, 144);\n"
                                                "border-bottom-color: rgb(3, 95, 144);\n"
                                                "padding-bottom:1px;")
        self.verticalLayout_2.addWidget(self.mostraFilterComboBox)
        self.mostraFilterComboBox.setCurrentIndex(0)

        self.telefonoFilterLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.telefonoFilterLineEdit.setFont(font)
        self.telefonoFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                  "border:2px solid rgba(0,0,0,0);\n"
                                                  "color:rgb(3, 95, 144);\n"
                                                  "border-bottom-color: rgb(3, 95, 144);\n"
                                                  "padding-bottom:10px;")
        self.telefonoFilterLineEdit.setText("")
        self.telefonoFilterLineEdit.setObjectName("telefonoFilterLineEdit")
        self.verticalLayout_2.addWidget(self.telefonoFilterLineEdit)

        self.gridLayoutWidget = QtWidgets.QWidget(self.visualizzaWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 240, 401, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.dataMinButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataMinButton.sizePolicy().hasHeightForWidth())
        self.dataMinButton.setSizePolicy(sizePolicy)
        self.dataMinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataMinButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                         "border-radius:10px;\n"
                                         "color:rgb(242,233,216);")
        self.dataMinButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataMinButton.setMenu(QtWidgets.QMenu(self.dataMinButton))
        self.calendar_1 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_1.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataMinButton)
        action.setDefaultWidget(self.calendar_1)
        self.dataMinButton.menu().addAction(action)
        self.calendar_1.setMinimumDate(QDate.currentDate())
        self.calendar_1.clicked.connect(lambda: self.get_date(self.calendar_1, self.dataMinButton))
        self.gridLayout.addWidget(self.dataMinButton, 0, 0, 1, 1)
        self.dataMinButton.setObjectName("dataMinButton")

        self.dataMaxButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataMaxButton.sizePolicy().hasHeightForWidth())
        self.dataMaxButton.setSizePolicy(sizePolicy)
        self.dataMaxButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataMaxButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                         "border-radius:10px;\n"
                                         "color:rgb(242,233,216);")
        self.dataMaxButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataMaxButton.setMenu(QtWidgets.QMenu(self.dataMaxButton))
        self.calendar_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_2.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataMaxButton)
        action.setDefaultWidget(self.calendar_2)
        self.dataMaxButton.menu().addAction(action)
        self.calendar_2.setMinimumDate(self.calendar_1.selectedDate())
        self.calendar_2.clicked.connect(lambda: self.get_date(self.calendar_2, self.dataMaxButton))
        self.dataMaxButton.setObjectName("dataMaxButton")
        self.gridLayout.addWidget(self.dataMaxButton, 0, 1, 1, 1)

        self.prenotazioneMinButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prenotazioneMinButton.sizePolicy().hasHeightForWidth())
        self.prenotazioneMinButton.setSizePolicy(sizePolicy)
        self.prenotazioneMinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prenotazioneMinButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                                 "border-radius:10px;\n"
                                                 "color:rgb(242,233,216);")
        self.prenotazioneMinButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.prenotazioneMinButton.setMenu(QtWidgets.QMenu(self.prenotazioneMinButton))
        self.calendar_3 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_3.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.prenotazioneMinButton)
        action.setDefaultWidget(self.calendar_3)
        self.prenotazioneMinButton.menu().addAction(action)
        self.calendar_3.setMinimumDate(QDate.currentDate())
        self.calendar_3.clicked.connect(lambda: self.get_date(self.calendar_3, self.prenotazioneMinButton))
        self.gridLayout.addWidget(self.prenotazioneMinButton, 0, 0, 2, 1)
        self.prenotazioneMinButton.setObjectName("prenotazioneMinButton")

        self.prenotazioneMaxButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prenotazioneMaxButton.sizePolicy().hasHeightForWidth())
        self.prenotazioneMaxButton.setSizePolicy(sizePolicy)
        self.prenotazioneMaxButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prenotazioneMaxButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                                 "border-radius:10px;\n"
                                                 "color:rgb(242,233,216);")
        self.prenotazioneMaxButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.prenotazioneMaxButton.setMenu(QtWidgets.QMenu(self.prenotazioneMaxButton))
        self.calendar_4 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_4.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.prenotazioneMaxButton)
        action.setDefaultWidget(self.calendar_4)
        self.prenotazioneMaxButton.menu().addAction(action)
        self.calendar_4.setMinimumDate(self.calendar_3.selectedDate())
        self.calendar_4.clicked.connect(lambda: self.get_date(self.calendar_4, self.prenotazioneMaxButton))
        self.prenotazioneMaxButton.setObjectName("prenotazioneMaxButton")
        self.gridLayout.addWidget(self.prenotazioneMaxButton, 0, 1, 2, 2)

        self.qrButton = QtWidgets.QPushButton(self.visualizzaWidget)
        self.qrButton.setGeometry(QtCore.QRect(10, 410, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.qrButton.setFont(font)
        self.qrButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.qrButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                    "border-radius:10px;\n"
                                    "color:rgb(242,233,216);")
        self.qrButton.setObjectName("qrButton")

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
        self.utenteLabel.setStyleSheet("color: rgb(229, 82, 2);")
        self.utenteLabel.setObjectName("utenteLabel")

        self.logoLabel = QtWidgets.QLabel(self.frame)
        self.logoLabel.setGeometry(QtCore.QRect(380, 40, 61, 61))
        self.logoLabel.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logoLabel.setText("")
        #self.logoLabel.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")

        UI_Prenotazione.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UI_Prenotazione)
        self.statusbar.setObjectName("statusbar")
        UI_Prenotazione.setStatusBar(self.statusbar)

        self.retranslateUi(UI_Prenotazione)
        self.tab.setCurrentIndex(1)
        self.accountMenu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(UI_Prenotazione)

    def retranslateUi(self, UI_Prenotazione):
        _translate = QtCore.QCoreApplication.translate
        UI_Prenotazione.setWindowTitle(_translate("UI_Prenotazione", "Prenotazioni"))
        self.minimizeButton.setText(_translate("UI_Prenotazione", "-"))
        self.closeButton.setText(_translate("UI_Prenotazione", "X"))
        self.titleLabel.setText(_translate("UI_Prenotazione", "Gestione Prenotazioni"))
        self.dataButton.setText(_translate("UI_Prenotazione", "Data visita"))
        self.nominativoLineEdit.setPlaceholderText(_translate("UI_Prenotazione", "Nominativo"))
        self.telefonoLineEdit.setPlaceholderText(_translate("UI_Prenotazione", "Telefono"))
        self.inserisciButton.setText(_translate("UI_Prenotazione", "Inserisci"))
        self.nuovaLabel.setText(_translate("UI_Prenotazione",
                                           "<html><head/><body><p><span style=\" font-weight:600; color:#e55202;\">Inserisci prenotazione #ID</span></p></body></html>"))
        self.tab.setTabText(self.tab.indexOf(self.inserisciWidget), _translate("UI_Prenotazione", "Inserisci Nuova"))
        self.visualizzaButton.setText(_translate("UI_Prenotazione", "Visualizza elenco filtrato"))
        self.visualizzaLabel.setText(_translate("UI_Prenotazione",
                                                "<html><head/><body><p><span style=\" font-weight:600; color:#e55202;\">Inserimento filtri per la ricerca</span></p></body></html>"))
        self.idFilterLineEdit.setPlaceholderText(_translate("UI_Prenotazione", "ID"))
        self.nominativoFilterLineEdit.setPlaceholderText(_translate("UI_Prenotazione", "Nominativo"))
        self.telefonoFilterLineEdit.setPlaceholderText(_translate("UI_Prenotazione", "Telefono"))
        self.dataMaxButton.setText(_translate("UI_Prenotazione", "Data Visita Max"))
        self.dataMinButton.setText(_translate("UI_Prenotazione", "Data Visita Min"))
        self.prenotazioneMaxButton.setText(_translate("UI_Prenotazione", "Data Prenotazione Max"))
        self.prenotazioneMinButton.setText(_translate("UI_Prenotazione", "Data Prenotazione Min"))
        self.qrButton.setText(_translate("UI_Prenotazione", "Cerca tramite QR code"))
        self.tab.setTabText(self.tab.indexOf(self.visualizzaWidget),
                            _translate("UI_Prenotazione", "Visualizza elenco"))
        self.accountMenu.setItemText(0, _translate("UI_Prenotazione", "Home"))
        self.accountMenu.setItemText(1, _translate("UI_Prenotazione", "Logout"))
        self.utenteLabel.setText(_translate("UI_Prenotazione", "NOMEUTENTE"))

    # metodo per scrivere la data scelta sul calendar widget sopra il bottone passato come parametro
    def get_date(self, calendar, button):
        date = calendar.selectedDate()
        button.setText(date.toString("yyyy-MM-dd"))