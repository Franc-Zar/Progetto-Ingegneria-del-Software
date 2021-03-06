from PyQt5 import QtCore, QtGui, QtWidgets

# classe di utility che permette di implementare, in visualizzazione, liste a scorrimento di varie tipologie di oggetti
# (prenotazioni,dipendenti,opere) ciascuno a sua volta visionabile individualmente
class UiLista(object):
    def setButton(self, button):
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        button.setFont(font)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setFlat(True)

    def setupUi(self, UI_Lista, lista, tipo):
        UI_Lista.setObjectName("UI_Lista")
        UI_Lista.resize(471, 612)
        UI_Lista.setStyleSheet("background-color: rgb(242,233,216)")

        self.centralwidget = QtWidgets.QWidget(UI_Lista)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 571))
        self.frame.setObjectName("frame")

        self.minimizeButton = QtWidgets.QPushButton(self.frame)
        self.minimizeButton.setGeometry(QtCore.QRect(400, 10, 21, 21))
        self.minimizeButton.setMouseTracking(True)
        self.minimizeButton.setStyleSheet("color:rgb(3, 95, 144);")
        self.setButton(self.minimizeButton)
        self.minimizeButton.setObjectName("minimizeButton")

        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(420, 10, 21, 21))
        self.closeButton.setStyleSheet("background-color: rgb(229, 82, 2); \n"
                                        "border-radius:10px;\n"
                                        "color:rgb(3, 95, 144);")
        self.setButton(self.closeButton)
        self.closeButton.setObjectName("closeButton")

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(160, 10, 160, 16))
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setWeight(75)
        # self.frame_name.setFont(font)
        self.titleLabel.setStyleSheet("color:rgb(229, 82, 2);font-weight:bold;")
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
        self.backButton.setObjectName("backButton")

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
#        self.logoLabel.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")

        self.scroll = QtWidgets.QScrollArea(self.frame)
        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.visualizza_completo = []

        if tipo == "opere":
            self.titleLabel.setText("Gestione Catalogo")
            for opera in lista:
                    object = QtWidgets.QFrame()
                    titoloLabel = QtWidgets.QLabel(object)
                    titoloLabel.setGeometry(QtCore.QRect(10, 0, 379, 31))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    titoloLabel.setFont(font)
                    titoloLabel.setStyleSheet("color:rgb(229, 82, 2);")
                    titoloLabel.setText(opera.getTitolo())
                    nomeLabel = QtWidgets.QLabel(object)
                    nomeLabel.setGeometry(QtCore.QRect(10, 30, 195, 36))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    nomeLabel.setFont(font)
                    nomeLabel.setStyleSheet("color:rgb(3, 95, 144);")
                    nomeLabel.setText(opera.getAutore())
                    tipoLabel = QtWidgets.QLabel(object)
                    tipoLabel.setGeometry(QtCore.QRect(200, 30, 195, 36))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    tipoLabel.setFont(font)
                    tipoLabel.setStyleSheet("color:rgb(3, 95, 144);")
                    tipoLabel.setText(opera.getTipologia())
                    codiceLabel = QtWidgets.QLabel(object)
                    codiceLabel.setGeometry(QtCore.QRect(10, 60, 195, 36))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    codiceLabel.setFont(font)
                    codiceLabel.setStyleSheet("color:rgb(3, 95, 144);")
                    codiceLabel.setText(str(opera.getCodice()))
                    visualizzaButton = QtWidgets.QPushButton(object)
                    visualizzaButton.setCheckable(True)
                    visualizzaButton.setGeometry(QtCore.QRect(180, 60, 201, 31))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    visualizzaButton.setFont(font)
                    visualizzaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    visualizzaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                                   "border-radius:10px;\n"
                                                   "color:rgb(242,233,216);")
                    visualizzaButton.setText("Visualizza Scheda Opera")
                    self.visualizza_completo.append(visualizzaButton)
                    object.setFixedSize(383, 111)
                    self.vbox.addWidget(object)
        if tipo == "dipendenti":
            self.titleLabel.setText("Gestione Dipendenti")
            for dipendente in lista:
                    object = QtWidgets.QFrame()
                    titoloLabel = QtWidgets.QLabel(object)
                    titoloLabel.setGeometry(QtCore.QRect(10, 0, 379, 31))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    titoloLabel.setFont(font)
                    titoloLabel.setStyleSheet("color:rgb(229, 82, 2);")
                    titoloLabel.setText(dipendente.getUsername())
                    nomeLabel = QtWidgets.QLabel(object)
                    nomeLabel.setGeometry(QtCore.QRect(10, 30, 195, 36))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    nomeLabel.setFont(font)
                    nomeLabel.setStyleSheet("color:rgb(3, 95, 144);")
                    nomeLabel.setText(dipendente.getNominativo())
                    tipoLabel = QtWidgets.QLabel(object)
                    tipoLabel.setGeometry(QtCore.QRect(200, 30, 195, 36))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    tipoLabel.setFont(font)
                    tipoLabel.setStyleSheet("color:rgb(3, 95, 144);")
                    tipoLabel.setText(dipendente.getRuolo())
                    codiceLabel = QtWidgets.QLabel(object)
                    codiceLabel.setGeometry(QtCore.QRect(10, 60, 195, 36))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    codiceLabel.setFont(font)
                    codiceLabel.setStyleSheet("color:rgb(3, 95, 144);")
                    codiceLabel.setText(str(dipendente.getCf()))
                    visualizzaButton = QtWidgets.QPushButton(object)
                    visualizzaButton.setCheckable(True)
                    visualizzaButton.setGeometry(QtCore.QRect(180, 60, 201, 31))
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    visualizzaButton.setFont(font)
                    visualizzaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    visualizzaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                                   "border-radius:10px;\n"
                                                   "color:rgb(242,233,216);")
                    visualizzaButton.setText("Visualizza Dipendente")
                    self.visualizza_completo.append(visualizzaButton)
                    object.setFixedSize(383, 111)
                    self.vbox.addWidget(object)

        if tipo == "mostre":
            for mostra in lista:
                object = QtWidgets.QFrame()
                titoloLabel = QtWidgets.QLabel(object)
                titoloLabel.setGeometry(QtCore.QRect(10, 0, 379, 31))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                titoloLabel.setFont(font)
                titoloLabel.setStyleSheet("color:rgb(229, 82, 2);")
                titoloLabel.setText(mostra.getTitolo())
                dataInizioLabel = QtWidgets.QLabel(object)
                dataInizioLabel.setGeometry(QtCore.QRect(10, 30, 195, 36))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                dataInizioLabel.setFont(font)
                dataInizioLabel.setStyleSheet("color:rgb(3, 95, 144);")
                dataInizioLabel.setText(mostra.getDataInizio())
                dataFineLabel = QtWidgets.QLabel(object)
                dataFineLabel.setGeometry(QtCore.QRect(200, 30, 195, 36))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                dataFineLabel.setFont(font)
                dataFineLabel.setStyleSheet("color:rgb(3, 95, 144);")
                dataFineLabel.setText(mostra.getDataFine())
                idLabel = QtWidgets.QLabel(object)
                idLabel.setGeometry(QtCore.QRect(10, 60, 195, 36))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                idLabel.setFont(font)
                idLabel.setStyleSheet("color:rgb(3, 95, 144);")
                mostra.checkMostraExists()
                idLabel.setText(str(mostra.getID()))
                visualizzaButton = QtWidgets.QPushButton(object)
                visualizzaButton.setCheckable(True)
                visualizzaButton.setGeometry(QtCore.QRect(180, 60, 201, 31))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                visualizzaButton.setFont(font)
                visualizzaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                visualizzaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                               "border-radius:10px;\n"
                                               "color:rgb(242,233,216);")
                visualizzaButton.setText("Visualizza Scheda Mostra")
                self.visualizza_completo.append(visualizzaButton)
                object.setFixedSize(383, 111)
                self.vbox.addWidget(object)

        if tipo == 'prenotazione':
            for prenotazione in lista:
                object = QtWidgets.QFrame()
                nomeLabel = QtWidgets.QLabel(object)
                nomeLabel.setGeometry(QtCore.QRect(10, 0, 379, 31))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                nomeLabel.setFont(font)
                nomeLabel.setStyleSheet("color:rgb(229, 82, 2);")
                nomeLabel.setText(prenotazione.getNominativo())
                dataPrenotazioneLabel = QtWidgets.QLabel(object)
                dataPrenotazioneLabel.setGeometry(QtCore.QRect(10, 30, 195, 36))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                dataPrenotazioneLabel.setFont(font)
                dataPrenotazioneLabel.setStyleSheet("color:rgb(3, 95, 144);")
                dataPrenotazioneLabel.setText('Prenotata: ' + prenotazione.getDataPrenotazione())
                dataVisitaLabel = QtWidgets.QLabel(object)
                dataVisitaLabel.setGeometry(QtCore.QRect(200, 30, 195, 36))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                dataVisitaLabel.setFont(font)
                dataVisitaLabel.setStyleSheet("color:rgb(3, 95, 144);")
                dataVisitaLabel.setText('Visita: ' + prenotazione.getDataVisita())
                idLabel = QtWidgets.QLabel(object)
                idLabel.setGeometry(QtCore.QRect(10, 60, 195, 36))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                idLabel.setFont(font)
                idLabel.setStyleSheet("color:rgb(3, 95, 144);")
                prenotazione.checkPrenotazioneExists()
                idLabel.setText(str(prenotazione.getCodice()))
                visualizzaButton = QtWidgets.QPushButton(object)
                visualizzaButton.setCheckable(True)
                visualizzaButton.setGeometry(QtCore.QRect(180, 60, 201, 31))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                visualizzaButton.setFont(font)
                visualizzaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                visualizzaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                               "border-radius:10px;\n"
                                               "color:rgb(242,233,216);")
                visualizzaButton.setText("Visualizza Prenotazione")
                self.visualizza_completo.append(visualizzaButton)
                object.setFixedSize(383, 111)
                self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)
        self.scroll.setGeometry(QtCore.QRect(10, 100, 431, 481))
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        UI_Lista.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UI_Lista)
        self.statusbar.setObjectName("statusbar")
        UI_Lista.setStatusBar(self.statusbar)

        self.retranslateUi(UI_Lista,tipo)
        self.accountMenu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(UI_Lista)

    def retranslateUi(self, UI_Lista,tipo):
        _translate = QtCore.QCoreApplication.translate
        if tipo == 'dipendenti':
            UI_Lista.setWindowTitle(_translate("", "Personale"))
        elif tipo == 'opere':
            UI_Lista.setWindowTitle(_translate("", "Catalogo"))
        elif tipo == 'prenotazione':
            UI_Lista.setWindowTitle(_translate("", "Prenotazioni"))
        elif tipo == 'mostre':
            UI_Lista.setWindowTitle(_translate("", "Mostre"))

        self.minimizeButton.setText(_translate("UI_Mostre", "-"))
        self.closeButton.setText(_translate("UI_Mostre", "X"))
        self.backButton.setText(_translate("UI_Mostre", ""))
        self.accountMenu.setItemText(0, _translate("UI_Mostre", "Home"))
        self.accountMenu.setItemText(1, _translate("UI_Mostre", "Logout"))
        self.utenteLabel.setText(_translate("UI_Mostre", "NOMEUTENTE"))

    # metodo "getter" per il vettore di bottoni che permettono di visualizzare la scheda completa dell'oggetto
    # corrispondente
    def getVisualizzaCompleto(self):
        return self.visualizza_completo
