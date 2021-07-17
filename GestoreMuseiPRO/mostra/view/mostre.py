
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Ui import logo_rc, back_rc

from Configurazione.StrutturaMuseo import StrutturaMuseo
from esposizione.controller.ControllerEsposizione import ControllerEsposizione
from mostra.controller.ControllerMostra import ControllerMostra
from opera.ControllerOpera.GestioneCatalogo import GestioneCatalogo

# classe di correlazione tra le funzionalità del controller e le scelte effettuate dall'utente tramite
# l'input/output dell'interfaccia grafica relativa alla visualizzazione delle schede di inserimento nuova
# mostra e filtraggio delle mostre nel database
class UiMostre(object):
    def __init__(self):
        self.controller = ControllerMostra()
        self.listaIdOpere = []
        self.controllerEsposizione = ControllerEsposizione()

    # metodo per caricare nelle combobox le sale del museo (per inserire nuove mostre o filtrare in funzione
    # di esse)
    def caricaSale(self):
        strutturaMuseo = StrutturaMuseo()
        listaSale = strutturaMuseo.getSale()
        self.salaComboBox_2.addItem("")
        for sala in listaSale:
            self.salaComboBox_1.addItem(sala)
            self.salaComboBox_2.addItem(sala)

    # metodo per caricare i nomi delle opere presenti nel catalogo in modo da poter essere selezionate
    # per una possibile nuova mostra
    def caricaOpere(self):
        try:
            controllerOpere = GestioneCatalogo()
            self.nomiMostre = controllerOpere.getOpereFiltrate()
            if self.nomiMostre:
                for opera in self.nomiMostre:
                    self.opereList.addItem(opera.titolo)
                    self.listaIdOpere.append(opera.codice)
        except Exception:
            raise

    # metodo per ottenere una lista delle mostre filtrate secondo le condizioni fornite dall'utente
    def getListaMostre(self):
        filtri = {}
        if self.titoloFilterLineEdit.text():
            filtri['titolo'] = self.titoloFilterLineEdit.text()
        if self.idFilterLineEdit.text():
            filtri['ID'] =  self.idFilterLineEdit.text()
        if self.salaComboBox_2.currentText():
            filtri['sala'] = self.salaComboBox_2.currentText()
        tupleAppoggio = [0,0]
        if self.edMinFilterLineEdit.text() or self.edMaxFilterLineEdit.text():
            tupleAppoggio[0] = self.edMinFilterLineEdit.text()
            tupleAppoggio[1] = self.edMaxFilterLineEdit.text()
            filtri['edizione'] = tuple(tupleAppoggio)
        tupleAppoggio = [0,0]
        if self.inizioMinButton.text() != 'Data Inizio MIN':
            tupleAppoggio[0] = self.inizioMinButton.text()
        if self.inizioMaxButton.text() != 'Data Inizio MAX':
            tupleAppoggio[1] = self.inizioMaxButton.text()
        if tupleAppoggio!=[0,0]:
            filtri['data_inizio'] = tuple(tupleAppoggio)
        tupleAppoggio = [0,0]
        if self.fineMinButton.text() != 'Data Fine MIN':
            tupleAppoggio[0] = self.fineMinButton.text()
        if self.fineMaxButton.text() != 'Data Fine MAX':
            tupleAppoggio[1] = self.fineMaxButton.text()
        if tupleAppoggio!=[0,0]:
            filtri['data_fine'] = tuple(tupleAppoggio)
        try:
            return self.controller.setListaMostre(filtri)
        except Exception:
            raise

    # metodo per salvare una mostra nel database
    def saveMostra(self):
        sala = self.salaComboBox_1.currentText()
        titolo = self.titoloLineEdit.text()
        edizione = self.edizioneLineEdit.text()
        prezzo = self.prezzoLineEdit.text()
        dataInizio = self.dataInizioButton.text()
        dataFine = self.dataFineButton.text()
        if sala and titolo and edizione and dataInizio and dataFine:
            try:
                prezzo = str(float(prezzo))
                idMostra = None
                self.controller.setModel(titolo, edizione, sala, dataInizio, dataFine, prezzo)
                try:
                    self.controller.saveMostra()
                    idMostra = self.controller.model.getID()
                    selIndexes = self.opereList.selectedIndexes()
                    for sel in selIndexes:
                        codiceOpera = self.nomiMostre[sel.row()].getCodice()
                        self.controllerEsposizione.setModel(dataInizio, codiceOpera, idMostra, dataFine)
                        self.controllerEsposizione.saveEsposizione()
                    self.nuovaLabel.setStyleSheet("color: rgb(33, 163, 21);")
                    self.nuovaLabel.setText("Mostra salvata")
                except Exception:
                    if not idMostra:
                        self.controller.eliminaMostra(idMostra)
                        self.controllerEsposizione.eliminaEsposizione(idMostra)
                    self.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
                    self.nuovaLabel.setText("Non è possibile inserire mostra nel database")
            except Exception:
                self.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.nuovaLabel.setText("Per favore inserisci il prezzo come richiesto")
        else:
            self.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.nuovaLabel.setText("Attenzione: inserisci tutti i dati!")


    def setupUi(self, uiMostre):
        uiMostre.setObjectName("UI_Mostre")
        uiMostre.resize(471, 612)
        uiMostre.setStyleSheet("background-color: rgb(242,233,216)")
        self.centralWidget = QtWidgets.QWidget(uiMostre)
        self.centralWidget.setObjectName("centralWidget")

        self.frame = QtWidgets.QFrame(self.centralWidget)
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
        self.titleLabel.setGeometry(QtCore.QRect(160, 10, 121, 16))
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

        self.inserisciWidget = QtWidgets.QWidget()
        self.inserisciWidget.setObjectName("inserisciNuova")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.inserisciWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 361, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.insDatiVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.insDatiVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.insDatiVerticalLayout.setObjectName("insDatiVerticalLayout")

        self.titoloLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titoloLineEdit.setFont(font)
        self.titoloLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                          "border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:10px;")
        self.titoloLineEdit.setText("")
        self.titoloLineEdit.setObjectName("titoloLineEdit")

        self.insDatiVerticalLayout.addWidget(self.titoloLineEdit)
        self.edizioneLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edizioneLineEdit.setFont(font)
        self.edizioneLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:2px solid rgba(0,0,0,0);\n"
                                            "color:rgb(3, 95, 144);\n"
                                            "border-bottom-color: rgb(3, 95, 144);\n"
                                            "padding-bottom:10px;")
        self.edizioneLineEdit.setText("")
        self.edizioneLineEdit.setObjectName("edizioneLineEdit")
        self.insDatiVerticalLayout.addWidget(self.edizioneLineEdit)

        self.prezzoLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prezzoLineEdit.setFont(font)
        self.prezzoLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                          "border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:10px;")
        self.prezzoLineEdit.setText("")
        self.prezzoLineEdit.setObjectName("prezzoLineEdit")
        self.insDatiVerticalLayout.addWidget(self.prezzoLineEdit)

        self.dataInizioButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
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
        self.insDatiVerticalLayout.addWidget(self.dataInizioButton)
        self.calendar_1.setMinimumDate(QDate.currentDate())
        self.calendar_1.clicked.connect(lambda: self.get_date(self.calendar_1, self.dataInizioButton))

        self.dataFineButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
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
        self.dataFineButton.setMenu(QtWidgets.QMenu(self.dataInizioButton))
        self.calendar_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_2.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataFineButton)
        action.setDefaultWidget(self.calendar_2)
        self.dataFineButton.menu().addAction(action)
        self.dataFineButton.setObjectName("dataFineButton")
        self.insDatiVerticalLayout.addWidget(self.dataFineButton)
        self.calendar_2.setMinimumDate(self.calendar_1.selectedDate())
        self.calendar_2.clicked.connect(lambda: self.get_date(self.calendar_2, self.dataFineButton))

        self.opereButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFineButton.sizePolicy().hasHeightForWidth())
        self.opereButton.setSizePolicy(sizePolicy)
        self.opereButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opereButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                          "border-radius:10px;\n"
                                          "color:rgb(242,233,216);")
        self.opereButton.setObjectName("opereButton")
        self.opereButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.opereButton.setMenu(QtWidgets.QMenu(self.opereButton))
        self.opereList = QtWidgets.QListWidget(self.frame)
        self.opereList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.opereList.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.opereButton)
        action.setDefaultWidget(self.opereList)
        self.opereButton.menu().addAction(action)
        self.opereButton.setObjectName("opereButton")
        self.insDatiVerticalLayout.addWidget(self.opereButton)

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
        self.nuovaLabel.setGeometry(QtCore.QRect(30, 10, 251, 21))
        self.nuovaLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.nuovaLabel.setObjectName("nuovaLabel")

        self.salaComboBox_1 = QtWidgets.QComboBox(self.inserisciWidget)
        self.salaComboBox_1.setGeometry(QtCore.QRect(90, 40, 291, 23))
        self.salaComboBox_1.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:1px;")
        self.salaComboBox_1.setObjectName("salaComboBox_1")

        self.salaLabel = QtWidgets.QLabel(self.inserisciWidget)
        self.salaLabel.setGeometry(QtCore.QRect(25, 40, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.salaLabel.setFont(font)
        self.salaLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.salaLabel.setObjectName("salaLabel")

        self.tab.addTab(self.inserisciWidget, "")

        self.visualizzaWidget = QtWidgets.QWidget()
        self.visualizzaWidget.setObjectName("visualizzaWidget")

        self.visualizzaButton = QtWidgets.QPushButton(self.visualizzaWidget)
        self.visualizzaButton.setGeometry(QtCore.QRect(200, 400, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.visualizzaButton.setFont(font)
        self.visualizzaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualizzaButton.setStyleSheet("background-color:rgb(229, 82, 2);\n"
                                            "border-radius:10px;\n"
                                            "color:rgb(242,233,216);")
        self.visualizzaButton.setObjectName("visualizzaButton")

        self.label_3 = QtWidgets.QLabel(self.visualizzaWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 221, 21))
        self.label_3.setStyleSheet("color:rgb(229, 82, 2);")
        self.label_3.setObjectName("label_3")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.visualizzaWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 361, 161))
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

        self.titoloFilterLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titoloFilterLineEdit.setFont(font)
        self.titoloFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                "border:2px solid rgba(0,0,0,0);\n"
                                                "color:rgb(3, 95, 144);\n"
                                                "border-bottom-color: rgb(3, 95, 144);\n"
                                                "padding-bottom:10px;")
        self.titoloFilterLineEdit.setText("")
        self.titoloFilterLineEdit.setObjectName("titoloFilterLineEdit")
        self.verticalLayout_2.addWidget(self.titoloFilterLineEdit)

        self.salaComboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.salaComboBox_2.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:1px;")
        self.salaComboBox_2.setObjectName("salaComboBox_2")
        self.verticalLayout_2.addWidget(self.salaComboBox_2)

        self.gridLayoutWidget = QtWidgets.QWidget(self.visualizzaWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 210, 401, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.edMinFilterLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edMinFilterLineEdit.setFont(font)
        self.edMinFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                               "border:2px solid rgba(0,0,0,0);\n"
                                               "color:rgb(3, 95, 144);\n"
                                               "border-bottom-color: rgb(3, 95, 144);\n"
                                               "padding-bottom:10px;")
        self.edMinFilterLineEdit.setText("")
        self.edMinFilterLineEdit.setObjectName("edMinFilterLineEdit")
        self.gridLayout.addWidget(self.edMinFilterLineEdit, 0, 0, 1, 1)

        self.edMaxFilterLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edMaxFilterLineEdit.setFont(font)
        self.edMaxFilterLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                               "border:2px solid rgba(0,0,0,0);\n"
                                               "color:rgb(3, 95, 144);\n"
                                               "border-bottom-color: rgb(3, 95, 144);\n"
                                               "padding-bottom:10px;")
        self.edMaxFilterLineEdit.setText("")
        self.edMaxFilterLineEdit.setObjectName("edMaxFilterLineEdit")
        self.gridLayout.addWidget(self.edMaxFilterLineEdit, 0, 1, 1, 1)

        self.inizioMinButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inizioMinButton.sizePolicy().hasHeightForWidth())
        self.inizioMinButton.setSizePolicy(sizePolicy)
        self.inizioMinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inizioMinButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                           "border-radius:10px;\n"
                                           "color:rgb(242,233,216);")
        self.inizioMinButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.inizioMinButton.setMenu(QtWidgets.QMenu(self.inizioMinButton))
        self.calendar_1_min = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_1_min.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.inizioMinButton)
        action.setDefaultWidget(self.calendar_1_min)
        self.inizioMinButton.menu().addAction(action)
        #self.calendar_1_min.setMinimumDate(QDate.currentDate())
        self.calendar_1_min.clicked.connect(lambda: self.get_date(self.calendar_1_min, self.inizioMinButton))
        self.inizioMinButton.setObjectName("inizioMinButton")
        self.gridLayout.addWidget(self.inizioMinButton, 1, 0, 1, 1)


        self.inizioMaxButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inizioMaxButton.sizePolicy().hasHeightForWidth())
        self.inizioMaxButton.setSizePolicy(sizePolicy)
        self.inizioMaxButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inizioMaxButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                           "border-radius:10px;\n"
                                           "color:rgb(242,233,216);")
        self.inizioMaxButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.inizioMaxButton.setMenu(QtWidgets.QMenu(self.inizioMaxButton))
        self.calendar_1_max = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_1_max.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.inizioMaxButton)
        action.setDefaultWidget(self.calendar_1_max)
        self.inizioMaxButton.menu().addAction(action)
        self.calendar_1_max.setMinimumDate(self.calendar_1_min.selectedDate())
        self.calendar_1_max.clicked.connect(lambda: self.get_date(self.calendar_1_max, self.inizioMaxButton))
        self.inizioMaxButton.setObjectName("inizioMaxButton")
        self.gridLayout.addWidget(self.inizioMaxButton, 1, 1, 1, 1)

        self.fineMinButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fineMinButton.sizePolicy().hasHeightForWidth())
        self.fineMinButton.setSizePolicy(sizePolicy)
        self.fineMinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fineMinButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                         "border-radius:10px;\n"
                                         "color:rgb(242,233,216);")
        self.fineMinButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.fineMinButton.setMenu(QtWidgets.QMenu(self.fineMinButton))
        self.calendar_2_min = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_2_min.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.fineMinButton)
        action.setDefaultWidget(self.calendar_2_min)
        self.fineMinButton.menu().addAction(action)
        self.calendar_2_min.clicked.connect(lambda: self.get_date(self.calendar_2_min, self.fineMinButton))
        self.fineMinButton.setObjectName("fineMinButton")
        self.gridLayout.addWidget(self.fineMinButton, 2, 0, 1, 1)

        self.fineMaxButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fineMaxButton.sizePolicy().hasHeightForWidth())
        self.fineMaxButton.setSizePolicy(sizePolicy)
        self.fineMaxButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fineMaxButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                         "border-radius:10px;\n"
                                         "color:rgb(242,233,216);")
        self.fineMaxButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.fineMaxButton.setMenu(QtWidgets.QMenu(self.fineMaxButton))
        self.calendar_2_max = QtWidgets.QCalendarWidget(self.frame)
        self.calendar_2_max.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.fineMaxButton)
        action.setDefaultWidget(self.calendar_2_max)
        self.fineMaxButton.menu().addAction(action)
        self.calendar_2_max.setMinimumDate(self.calendar_2_min.selectedDate())
        self.calendar_2_max.clicked.connect(lambda: self.get_date(self.calendar_2_max, self.fineMaxButton))
        self.fineMaxButton.setObjectName("fineMaxButton")
        self.gridLayout.addWidget(self.fineMaxButton, 2, 1, 1, 1)

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

        uiMostre.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(uiMostre)
        self.statusbar.setObjectName("statusbar")
        uiMostre.setStatusBar(self.statusbar)

        self.retranslateUi(uiMostre)
        self.tab.setCurrentIndex(0)
        self.accountMenu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(uiMostre)


    def retranslateUi(self, UI_Mostre):
        _translate = QtCore.QCoreApplication.translate
        UI_Mostre.setWindowTitle(_translate("UI_Mostre", "Mostre"))
        self.minimizeButton.setText(_translate("UI_Mostre", "-"))
        self.closeButton.setText(_translate("UI_Mostre", "X"))
        self.titleLabel.setText(_translate("UI_Mostre", "Gestione Mostre"))
        self.titoloLineEdit.setPlaceholderText(_translate("UI_Mostre", "Titolo"))
        self.edizioneLineEdit.setPlaceholderText(_translate("UI_Mostre", "Edizione"))
        self.prezzoLineEdit.setPlaceholderText(_translate("UI_Mostre", "Prezzo(Utilizzare il . per i decimali)"))
        self.dataInizioButton.setText(_translate("UI_Mostre", "Data Inizio"))
        self.dataFineButton.setText(_translate("UI_Mostre", "Data Fine"))
        self.opereButton.setText(_translate("UI_Mostre", "Seleziona Opere"))
        self.inserisciButton.setText(_translate("UI_Mostre", "Inserisci"))
        self.nuovaLabel.setText(_translate("UI_Mostre", ""))
        self.salaLabel.setText(_translate("UI_Mostre", "Sala: "))
        self.tab.setTabText(self.tab.indexOf(self.inserisciWidget), _translate("UI_Mostre", "Inserisci Nuova"))
        self.visualizzaButton.setText(_translate("UI_Mostre", "Visualizza elenco filtrato"))
        self.label_3.setText(_translate("UI_Mostre",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Inserimento filtri per la ricerca</span></p></body></html>"))
        self.idFilterLineEdit.setPlaceholderText(_translate("UI_Mostre", "ID"))
        self.titoloFilterLineEdit.setPlaceholderText(_translate("UI_Mostre", "Titolo"))
        self.edMinFilterLineEdit.setPlaceholderText(_translate("UI_Mostre", "Edizione Min"))
        self.edMaxFilterLineEdit.setPlaceholderText(_translate("UI_Mostre", "Edizione Max"))
        self.inizioMinButton.setText(_translate("UI_Mostre", "Data Inizio MIN"))
        self.inizioMaxButton.setText(_translate("UI_Mostre", "Data Inizio MAX"))
        self.fineMaxButton.setText(_translate("UI_Mostre", "Data Fine MAX"))
        self.fineMinButton.setText(_translate("UI_Mostre", "Data Fine MIN"))
        self.tab.setTabText(self.tab.indexOf(self.visualizzaWidget), _translate("UI_Mostre", "Visualizza elenco"))
        self.accountMenu.setItemText(0, _translate("UI_Mostre", "Home"))
        self.accountMenu.setItemText(1, _translate("UI_Mostre", "Logout"))
        self.utenteLabel.setText(_translate("UI_Mostre", "NOMEUTENTE"))

    # metodo per scrivere la data scelta sul calendar widget sopra il bottone passato come parametro
    def get_date(self, calendar, button):
        date = calendar.selectedDate()
        button.setText(date.toString("yyyy-MM-dd"))