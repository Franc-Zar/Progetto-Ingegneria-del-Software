from PyQt5 import QtCore, QtGui, QtWidgets
from Ui import logo_rc
from opera.ControllerOpera.GestioneCatalogo import GestioneCatalogo


# classe di correlazione tra le funzionalità del controller e le scelte effettuate dall'utente tramite
# l'input/output dell'interfaccia grafica relativa alla modifica dei dati dell'opera presa in considerazione
class Ui_ModificaOpera(object):
    def __init__(self, opera):
        self.gestioneCatalogo = GestioneCatalogo()
        self.gestioneCatalogo.setModel(opera)

    def getModel(self):
        return self.gestioneCatalogo.getModel()

    # metodo per impostare nelle label dell'interfaccia gli attuali valori dell'opera presa in considerazione
    def setLabels(self):
        self.newCodice.setText(str(self.getModel().getCodice()))
        self.newAutore.setText(self.getModel().getAutore())
        self.newTitolo.setText(self.getModel().getTitolo())
        self.newValore.setText(str(self.getModel().getValore()))
        self.newTipologia.setText(self.getModel().getTipologia())
        self.newImmagine.setText(self.getModel().getImg())
        self.newAnnoProd.setText(self.getModel().getAnnoProduzione())
        self.newDimensioni.setText(str(self.getModel().getDimensioni()))
        self.newDataAcquisizione.setText(self.getModel().getDataAcquisizione())

    # metodo per modificare i campi dell'opera presa in esame
    def modificaOpera(self):
        if self.newTitolo.text() and self.newCodice.text() \
                and self.newTipologia.text() and self.newValore.text() \
                and self.newDataAcquisizione.text() and self.newAnnoProd.text() \
                and self.newAutore.text() and self.newImmagine.text() and self.newDimensioni.text() \
                and self.gestioneCatalogo.modificaOpera(self.newTitolo.text(), self.newCodice.text(),
                                                        self.newTipologia.text(), self.newValore.text(),
                                                        self.newDataAcquisizione.text(), self.newAnnoProd.text(),
                                                        self.newAutore.text(), self.newImmagine.text(),
                                                        self.newDimensioni.text()):
            if self.newTitolo.text():
                self.gestioneCatalogo.getModel().setTitolo(self.newTitolo.text())
            if self.newCodice.text():
                self.gestioneCatalogo.getModel().setCodice(self.newCodice.text())
            if self.newTipologia.text():
                self.gestioneCatalogo.getModel().setTipologia(self.newTipologia.text())
            if self.newValore.text():
                self.gestioneCatalogo.getModel().setValore(self.newValore.text())
            if self.newDataAcquisizione.text():
                self.gestioneCatalogo.getModel().setDataAcquisizione(self.newDataAcquisizione.text())
            if self.newAnnoProd.text():
                self.gestioneCatalogo.getModel().setAnnoProduzione(self.newAnnoProd.text())
            if self.newAutore.text():
                self.gestioneCatalogo.getModel().setAutore(self.newAutore.text())
            if self.newImmagine.text():
                self.gestioneCatalogo.getModel().setImg(self.newImmagine.text())
            if self.newDimensioni.text():
                self.gestioneCatalogo.getModel().setDimensioni(self.newDimensioni.text())
            return True
        self.ErrorLabel.setText("Oops, qualcosa è andato storto!")

    def setupUi(self, ModificaOpera):
        ModificaOpera.setObjectName("ModificaOpera")
        ModificaOpera.resize(472, 379)
        self.frame = QtWidgets.QFrame(ModificaOpera)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 501, 391))
        self.frame.setStyleSheet("background-color: rgb(242, 233, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.newAutore = QtWidgets.QLineEdit(self.frame)
        self.newAutore.setGeometry(QtCore.QRect(70, 100, 341, 31))
        self.newAutore.setAutoFillBackground(False)
        self.newAutore.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                     "background-color:rgba(0,0,0,0);\n"
                                     "border:2px solid rgba(0,0,0,0);\n"
                                     "color:rgb(3, 95, 144);\n"
                                     "border-bottom-color: rgb(3, 95, 144);\n"
                                     "padding-bottom:10px;")
        self.newAutore.setText("")
        self.newAutore.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newAutore.setObjectName("NewAutore")

        self.newTitolo = QtWidgets.QLineEdit(self.frame)
        self.newTitolo.setGeometry(QtCore.QRect(70, 60, 341, 31))
        self.newTitolo.setAutoFillBackground(False)
        self.newTitolo.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                     "background-color:rgba(0,0,0,0);\n"
                                     "border:2px solid rgba(0,0,0,0);\n"
                                     "color:rgb(3, 95, 144);\n"
                                     "border-bottom-color: rgb(3, 95, 144);\n"
                                     "padding-bottom:10px;")
        self.newTitolo.setText("")
        self.newTitolo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newTitolo.setObjectName("NewTitolo")

        self.newTipologia = QtWidgets.QLineEdit(self.frame)
        self.newTipologia.setGeometry(QtCore.QRect(70, 140, 341, 31))
        self.newTipologia.setAutoFillBackground(False)
        self.newTipologia.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                        "background-color:rgba(0,0,0,0);\n"
                                        "border:2px solid rgba(0,0,0,0);\n"
                                        "color:rgb(3, 95, 144);\n"
                                        "border-bottom-color: rgb(3, 95, 144);\n"
                                        "padding-bottom:10px;")
        self.newTipologia.setText("")
        self.newTipologia.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newTipologia.setObjectName("NewTipologia")

        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(40, 20, 191, 20))
        self.Title.setStyleSheet("color:rgb(229, 82, 2);\n"
                                 "font: 11pt \"Ubuntu\";")
        self.Title.setObjectName("Title")

        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(460, 20, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("background-color: rgb(229, 82, 2); \n"
                                      "border-radius:10px;\n"
                                      "color:rgb(3, 95, 144);")
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName("close_button")

        self.minimizeButton = QtWidgets.QPushButton(self.frame)
        self.minimizeButton.setGeometry(QtCore.QRect(440, 20, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeButton.setMouseTracking(True)
        self.minimizeButton.setStyleSheet("color:rgb(3, 95, 144);")
        self.minimizeButton.setFlat(True)
        self.minimizeButton.setObjectName("minimizeButton")

        self.salvaOpera = QtWidgets.QPushButton(self.frame)
        self.salvaOpera.setGeometry(QtCore.QRect(340, 340, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.salvaOpera.setFont(font)
        self.salvaOpera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.salvaOpera.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                      "border-radius:10px;\n"
                                      "color:rgb(242,233,216);")
        self.salvaOpera.setObjectName("SalvaOpera")

        self.ErrorLabel = QtWidgets.QLabel(self.frame)
        self.ErrorLabel.setGeometry(QtCore.QRect(100, 350, 221, 20))
        self.ErrorLabel.setStyleSheet("color: rgb(247, 8, 8);")
        self.ErrorLabel.setText("")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.logo_label = QtWidgets.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(420, 50, 61, 61))
        self.logo_label.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logo_label.setText("")
        # self.logo_label.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")

        self.newValore = QtWidgets.QLineEdit(self.frame)
        self.newValore.setGeometry(QtCore.QRect(250, 180, 161, 31))
        self.newValore.setAutoFillBackground(False)
        self.newValore.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                     "background-color:rgba(0,0,0,0);\n"
                                     "border:2px solid rgba(0,0,0,0);\n"
                                     "color:rgb(3, 95, 144);\n"
                                     "border-bottom-color: rgb(3, 95, 144);\n"
                                     "padding-bottom:10px;")
        self.newValore.setText("")
        self.newValore.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newValore.setObjectName("NewValore")

        self.newCodice = QtWidgets.QLineEdit(self.frame)
        self.newCodice.setGeometry(QtCore.QRect(70, 180, 171, 31))
        self.newCodice.setAutoFillBackground(False)
        self.newCodice.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                     "background-color:rgba(0,0,0,0);\n"
                                     "border:2px solid rgba(0,0,0,0);\n"
                                     "color:rgb(3, 95, 144);\n"
                                     "border-bottom-color: rgb(3, 95, 144);\n"
                                     "padding-bottom:10px;")
        self.newCodice.setText("")
        self.newCodice.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newCodice.setObjectName("NewID")

        self.newDataAcquisizione = QtWidgets.QToolButton(self.frame)
        self.newDataAcquisizione.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newDataAcquisizione.setGeometry(QtCore.QRect(70, 300, 341, 31))
        self.newDataAcquisizione.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                               "border-radius:10px;\n"
                                               "color:rgb(242,233,216);")
        self.newDataAcquisizione.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.newDataAcquisizione.setMenu(QtWidgets.QMenu(self.newDataAcquisizione))
        self.calendar = QtWidgets.QCalendarWidget(self.frame)
        self.calendar.setMaximumDate(QtCore.QDate.currentDate())
        self.calendar.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.newDataAcquisizione)
        action.setDefaultWidget(self.calendar)
        self.newDataAcquisizione.menu().addAction(action)
        self.calendar.clicked.connect(lambda: self.get_date(self.calendar, self.newDataAcquisizione))
        self.newDataAcquisizione.setObjectName("newDataAcquisizione")

        self.newAnnoProd = QtWidgets.QLineEdit(self.frame)
        self.newAnnoProd.setGeometry(QtCore.QRect(70, 260, 341, 31))
        self.newAnnoProd.setAutoFillBackground(False)
        self.newAnnoProd.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                       "background-color:rgba(0,0,0,0);\n"
                                       "border:2px solid rgba(0,0,0,0);\n"
                                       "color:rgb(3, 95, 144);\n"
                                       "border-bottom-color: rgb(3, 95, 144);\n"
                                       "padding-bottom:10px;")
        self.newAnnoProd.setText("")
        self.newAnnoProd.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newAnnoProd.setObjectName("NewAnnoProd")

        self.newDimensioni = QtWidgets.QLineEdit(self.frame)
        self.newDimensioni.setGeometry(QtCore.QRect(70, 220, 171, 31))
        self.newDimensioni.setAutoFillBackground(False)
        self.newDimensioni.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                         "background-color:rgba(0,0,0,0);\n"
                                         "border:2px solid rgba(0,0,0,0);\n"
                                         "color:rgb(3, 95, 144);\n"
                                         "border-bottom-color: rgb(3, 95, 144);\n"
                                         "padding-bottom:10px;")
        self.newDimensioni.setText("")
        self.newDimensioni.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newDimensioni.setObjectName("NewDimensioni")

        self.newImmagine = QtWidgets.QLineEdit(self.frame)
        self.newImmagine.setGeometry(QtCore.QRect(250, 220, 161, 31))
        self.newImmagine.setAutoFillBackground(False)
        self.newImmagine.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                       "background-color:rgba(0,0,0,0);\n"
                                       "border:2px solid rgba(0,0,0,0);\n"
                                       "color:rgb(3, 95, 144);\n"
                                       "border-bottom-color: rgb(3, 95, 144);\n"
                                       "padding-bottom:10px;")
        self.newImmagine.setText("")
        self.newImmagine.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newImmagine.setObjectName("NewImmagine")

        self.retranslateUi(ModificaOpera)
        QtCore.QMetaObject.connectSlotsByName(ModificaOpera)
        ModificaOpera.setTabOrder(self.newTitolo, self.newAutore)
        ModificaOpera.setTabOrder(self.newAutore, self.newTipologia)
        ModificaOpera.setTabOrder(self.newTipologia, self.newCodice)
        ModificaOpera.setTabOrder(self.newCodice, self.newValore)
        ModificaOpera.setTabOrder(self.newValore, self.newDimensioni)
        ModificaOpera.setTabOrder(self.newDimensioni, self.newImmagine)
        ModificaOpera.setTabOrder(self.newImmagine, self.newAnnoProd)
        ModificaOpera.setTabOrder(self.newAnnoProd, self.newDataAcquisizione)
        ModificaOpera.setTabOrder(self.newDataAcquisizione, self.salvaOpera)
        ModificaOpera.setTabOrder(self.salvaOpera, self.minimizeButton)
        ModificaOpera.setTabOrder(self.minimizeButton, self.exitButton)

    def retranslateUi(self, ModificaOpera):
        _translate = QtCore.QCoreApplication.translate
        ModificaOpera.setWindowTitle(_translate("ModificaOpera", "Modifica Opera"))
        self.newAutore.setPlaceholderText(_translate("ModificaOpera", "Autore"))
        self.newTitolo.setPlaceholderText(_translate("ModificaOpera", "Titolo"))
        self.newTipologia.setPlaceholderText(_translate("ModificaOpera", "Tipologia"))
        self.Title.setWhatsThis(_translate("ModificaOpera",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Modifica Password</span></p></body></html>"))
        self.Title.setText(_translate("ModificaOpera",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Modifica Opera</span></p></body></html>"))
        self.exitButton.setText(_translate("ModificaOpera", "X"))
        self.minimizeButton.setText(_translate("ModificaOpera", "-"))
        self.salvaOpera.setText(_translate("ModificaOpera", "Salva "))
        self.newValore.setPlaceholderText(_translate("ModificaOpera", "Valore"))
        self.newCodice.setPlaceholderText(_translate("ModificaOpera", "ID"))
        self.newDataAcquisizione.setText(_translate("ModificaOpera", "Data Acquisizione"))
        self.newAnnoProd.setPlaceholderText(_translate("ModificaOpera", "Anno Produzione"))
        self.newDimensioni.setPlaceholderText(_translate("ModificaOpera", "Dimensioni"))
        self.newImmagine.setPlaceholderText(_translate("ModificaOpera", "Immagine"))

    # metodo per scrivere la data scelta sul calendar widget sopra il bottone passato come parametro
    def get_date(self, calendar, button):
        date = calendar.selectedDate()
        button.setText(date.toString("yyyy-MM-dd"))
