import os
import sqlite3
import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore
from database import MyDB
from Login.ViewLogin.ModificaPasswd import UiModificaPasswd
from Login.ViewLogin.login import UiLogin
from Configurazione.StrutturaMuseo import StrutturaMuseo
from Dipendenti.ViewDipendenti.ModificaDipendente import UiModificaDipendente
from Dipendenti.ViewDipendenti.dipendente_complete import Ui_DipendenteComplete
from Dipendenti.ViewDipendenti.dipendenti import Ui_Dipendenti
from Configurazione.ViewStrutturaMuseo import Ui_StrutturaMuseo
from Ui.Home.adminHome import UiAdminHome
from Ui.Home.catalogoHome import UiCatalogoHome
from mostra.view.mostre import UiMostre
from prenotazione.view.prenotazioni import Ui_Prenotazione
from visita.view.visite import UiVisite
from View.PopUp import PopUp
from View.VisualizzaLista import UiLista
from mostra.view.mostra_complete import UiMostraComplete
from Ui.Home.FrontOfficeHome import UiFrontOfficeHome
from opera.ViewOpera.ModificaOpera import Ui_ModificaOpera
from opera.ViewOpera.catalogo import UiCatalogo
from opera.ViewOpera.opera_complete import Ui_OperaComplete
from prenotazione.view.prenotazione_complete import UiPrenotazioneComplete

# classe principale del programma:
# al suo interno sono presenti i vari collegamenti tra le singole interfacce grafiche, le quali
# complessivamente realizzano il funzionamento complessivo dello stesso
from statistica.view.statistiche import UiStatistiche


class GestoreMuseiPRO(QMainWindow):
    def __init__(self):
        super(GestoreMuseiPRO, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.username = ""
        self.ruolo = ""
        self.home = None
        self.popUp = PopUp()
        self.con = MyDB.db
        self.startLogin()
        self.show()


    # metodo che avvia l'interfaccia del Login
    def startLogin(self):
        self.username = ""
        self.ruolo = ""
        self.home = UiLogin()
        self.home.controller.logOut()
        self.home.setupUi(self)
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.exitButton.clicked.connect(sys.exit)
        self.home.mostraCheckBox.stateChanged.connect(self.home.mostraPasswd)
        self.home.loginField.clicked.connect(self.accessoHome)


    # interfaccia grafica per aggiornare la password relativa all'account in considerazione
    def startModificaPasswd(self):
        self.popUp.setUi(UiModificaPasswd())
        self.popUp.getUi().setupUi(self.popUp)
        self.popUp.getUi().controller.logIn(self.username,self.ruolo)
        self.popUp.getUi().closeButton.clicked.connect(self.popUp.close)
        self.popUp.getUi().minimizeButton.clicked.connect(self.popUp.showMinimized)
        self.popUp.getUi().mostraCheckBox.clicked.connect(self.popUp.getUi().mostraPasswd)
        self.popUp.getUi().modificaButton.clicked.connect(self.popUp.getUi().aggiornaPasswd)
        self.popUp.show()


    # metodo che avvia l'interfaccia home associata al ruolo di "admin"
    def startAdminHome(self):
        self.home = UiAdminHome()
        self.home.setupUi(self)
        self.home.utenteLabel.setText(self.username)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home,False))
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.catalogoButton.clicked.connect(self.startUiCatalogo)
        self.home.mostreButton.clicked.connect(self.startUIMostre)
        self.home.prenotazioniButton.clicked.connect(self.startUIPrenotazioni)
        self.home.visiteButton.clicked.connect(self.startUiVisite)
        self.home.statButton.clicked.connect(self.startStatistiche)
        self.home.dipendentiButton.clicked.connect(self.startUiDipendente)

    # metodo che avvia l'interfaccia home associata al ruolo "catalogatore"
    def startCatalogoHome(self):
        self.home = UiCatalogoHome()
        self.home.setupUi(self)
        self.home.utenteLabel.setText(self.username)
        self.home.catalogoButton.clicked.connect(self.startUiCatalogo)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home,False))
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.closeButton.clicked.connect(sys.exit)

    # metodo che avvia l'interfaccia home associata al ruolo "front_office"
    def startFrontOfficeHome(self):
        self.home = UiFrontOfficeHome()
        self.home.setupUi(self)
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.prenotazioniButton.clicked.connect(self.startUIPrenotazioni)
        self.home.visiteButton.clicked.connect(self.startUiVisite)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home,False))
        self.home.utenteLabel.setText(self.username)
    
    # metodo che avvia l'interfaccia di gestione del personale
    def startUiDipendente(self):
        self.home = Ui_Dipendenti()
        self.home.setupUi(self)
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.utenteLabel.setText(self.username)
        self.home.backButton.clicked.connect(self.goHome)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.inserisciButton.clicked.connect(self.home.nuovoDipendente)
        self.home.visualizzaButton.clicked.connect(lambda: self.startListaDipendenti(self.home.listaDipendenti()))
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
    
    # metodo che avvia l'interfaccia di modifica di un dipendente selezionato dalla lista filtrata precedentemente
    def startModificaDipendente(self,dipendente,listaDipendenti):
        self.popUp.setUi(UiModificaDipendente(dipendente))
        self.popUp.getUi().setupUi(self.popUp)
        self.popUp.getUi().closeButton.clicked.connect(self.popUp.close)
        self.popUp.getUi().minimizeButton.clicked.connect(self.popUp.showMinimized)
        self.popUp.getUi().setLabels()

        # metodo che aggiorna la lista filtrata precedentemente con il dipendente modificato
        def salvaDipendente():
            if self.popUp.getUi().modificaDipendente():
                listaDipendenti.remove(dipendente)
                listaDipendenti.append(self.popUp.getUi().getModel())
                self.popUp.close()
                self.startListaDipendenti(listaDipendenti)

        self.popUp.getUi().salvaButton.clicked.connect(salvaDipendente)
        self.popUp.show()

    # metodo che avvia la visualizzazione della lista dipendenti filtrata
    def startListaDipendenti(self, listaDipendenti):
        self.popUp.close()
        self.home = UiLista()
        self.home.setupUi(self, listaDipendenti, 'dipendenti')
        self.home.utenteLabel.setText(self.username)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.backButton.clicked.connect(self.startUiDipendente)

        # metodo per selezionare un particolare dipendente tra quelli presenti nella lista filtrata
        # al fine di visualizzare la relativa scheda completa
        def getDipendente():
            for visualizza_dipendente in self.home.getVisualizzaCompleto():
                if visualizza_dipendente.isChecked():
                    index_dipendente = self.home.getVisualizzaCompleto().index(visualizza_dipendente)
                    return listaDipendenti[index_dipendente]

        for visualizza_dipendente in self.home.getVisualizzaCompleto():
            visualizza_dipendente.clicked.connect(lambda: self.startDipendenteComplete(getDipendente(), listaDipendenti))

    # metodo che avvia l'interfaccia di visualizzazione della scheda dipendente completa
    def startDipendenteComplete(self, dipendente, listaDipendenti):
        self.home = Ui_DipendenteComplete(dipendente)
        self.home.setupUi(self)
        self.home.setLabels()
        self.home.utenteLabel.setText(self.username)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.rimuoviButton.clicked.connect(lambda: eliminaDipendente(dipendente, listaDipendenti))
        self.home.backButton.clicked.connect(lambda: self.startListaDipendenti(listaDipendenti))
        self.home.modificaButton.clicked.connect(lambda: self.startModificaDipendente(dipendente, listaDipendenti))

        # metodo che permette di eliminare il dipendente dal database, rimuovendolo anche dalla lista
        # precedentemente filtrata
        def eliminaDipendente(dipendente, listaDipendenti):
            try:
                if self.home.eliminaDipendente():
                    listaDipendenti.remove(dipendente)
                    self.startListaDipendenti(listaDipendenti)
            except sqlite3.Error:
                self.startDipendenteComplete(dipendente, listaDipendenti)

    def startStatistiche(self):
        self.home = UiStatistiche()
        self.home.setupUi(self)
        self.home.userLabel.setText(self.username)
        self.home.backButton.clicked.connect(self.goHome)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.closeButton.clicked.connect(sys.exit)

    # metodo che avvia l'interfaccia delle funzionalità di gestione del catalogo
    def startUiCatalogo(self):
        self.home = UiCatalogo()
        self.home.setupUi(self)
        self.home.utenteLabel.setText(self.username)
        self.home.inserisciButton.clicked.connect(self.home.nuovaOpera)
        self.home.backButton.clicked.connect(self.goHome)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.visualizzaButton.clicked.connect(lambda: self.startListaOpere(self.home.listaOpere()))
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))


    # metodo che avvia l'interfaccia di visualizzazione della scheda opera completa
    def startOperaComplete(self,opera,listaOpere):
        self.home = Ui_OperaComplete(opera)
        self.home.setupUi(self)
        self.home.setLabels()
        self.home.exitButton.clicked.connect(sys.exit)
        self.home.Minimize.clicked.connect(self.showMinimized)
        self.home.User.setText(self.username)
        self.home.rimuoviOpera.clicked.connect(lambda: eliminaOpera(opera, listaOpere))
        self.home.backButton.clicked.connect(lambda: self.startListaOpere(listaOpere))
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.ModificaOpera.clicked.connect(lambda: self.startModificaOpera(opera,listaOpere))

        # metodo che permette di eliminare l'opera dal database, rimuovendola anche dalla lista
        # precedentemente filtrata
        def eliminaOpera(opera, listaOpere):
            try:
                if self.home.eliminaOpera():
                    listaOpere.remove(opera)
                    self.startListaOpere(listaOpere)
            except sqlite3.Error:
                self.startOperaComplete(opera, listaOpere)

    # metodo che avvia la visualizzazione della lista opere filtrata
    def startListaOpere(self,listaOpere):
        self.popUp.close()
        self.home = UiLista()
        self.home.setupUi(self, listaOpere, "opere")
        self.home.utenteLabel.setText(self.username)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.backButton.clicked.connect(self.startUiCatalogo)

        # metodo per selezionare una particolare opera tra quelle presenti nella lista filtrata
        # al fine di visualizzare la relativa scheda completa
        def getOpera():
            for visualizza_opera in self.home.getVisualizzaCompleto():
                if visualizza_opera.isChecked():
                    index_opera = self.home.getVisualizzaCompleto().index(visualizza_opera)
                    return listaOpere[index_opera]

        for visualizza_opera in self.home.getVisualizzaCompleto():
            visualizza_opera.clicked.connect(lambda: self.startOperaComplete(getOpera(), listaOpere))

    # metodo che avvia l'interfaccia di modifica di un'opera selezionata dalla lista filtrata precedentemente
    def startModificaOpera(self,opera,listaOpere):
        self.popUp.setUi(Ui_ModificaOpera(opera))
        self.popUp.getUi().setupUi(self.popUp)
        self.popUp.getUi().setLabels()
        self.popUp.getUi().exitButton.clicked.connect(self.popUp.close)
        self.popUp.getUi().minimizeButton.clicked.connect(self.popUp.showMinimized)
        self.popUp.show()

        # metodo che permette il salvataggio delle modifiche precedentemente apportate all'opera
        def salvaModificheOpera():
            if self.popUp.getUi().modificaOpera():
                    listaOpere.remove(opera)
                    listaOpere.append(self.popUp.getUi().getModel())
                    self.popUp.close()
                    self.startListaOpere(listaOpere)

        self.popUp.getUi().salvaOpera.clicked.connect(salvaModificheOpera)
        self.popUp.show()

    # metodo che avvia l'interfaccia di visualizzazione delle operazioni relative alla gestione mostre
    def startUIMostre(self):
        self.home = UiMostre()
        self.home.setupUi(self)
        self.home.utenteLabel.setText(self.username)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.backButton.clicked.connect(self.goHome)

        try:
            self.home.caricaOpere()
            self.home.caricaSale()
        except Exception:
            self.home.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.home.nuovaLabel.setText("Errore nel caricamento delle opere in catalogo")

        self.home.inserisciButton.clicked.connect(self.home.saveMostra)
        self.home.visualizzaButton.clicked.connect(lambda: self.startListaMostre(self.home.getListaMostre()))
        self.show()

    # metodo che avvia la visualizzazione della lista mostre filtrata
    def startListaMostre(self,listaMostre):
        self.home = UiLista()
        self.home.setupUi(self, listaMostre, 'mostre')
        self.home.utenteLabel.setText(self.username)
        self.home.backButton.clicked.connect(self.startUIMostre)
        self.home.closeButton.clicked.connect(sys.exit)

        # metodo per selezionare una particolare mostra tra quelle presenti nella lista filtrata
        # al fine di visualizzare la relativa scheda completa
        def getIdMostra(listaMostre):
            for visualizza_scheda in self.home.getVisualizzaCompleto():
                if visualizza_scheda.isChecked():
                    indexMostra = self.home.getVisualizzaCompleto().index(visualizza_scheda)
                    return listaMostre[indexMostra].getID()

        for visualizza_scheda,mostra in zip(self.home.getVisualizzaCompleto(), listaMostre):
            visualizza_scheda.clicked.connect(lambda: self.startMostraComplete(getIdMostra(listaMostre)))

    # metodo che avvia l'interfaccia di visualizzazione della scheda completa della mostra
    def startMostraComplete(self,idMostra):
        self.home = UiMostraComplete(idMostra)
        self.home.setupUi(self)
        try:
            self.home.caricaSale()
            self.home.caricaOpere()
        except Exception as e:
            self.home.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.home.msgLabel.setText(e.args[0])
        self.home.setLabels()

        self.home.backButton.clicked.connect(self.startUIMostre)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.userLabel.setText(self.username)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home, True))
        self.home.minimizeButton.clicked.connect(self.showMinimized)

        self.home.eliminaButton.clicked.connect(self.home.terminaFunction)
        self.home.modificaButton.clicked.connect(self.home.modificaFunction)


    # metodo che avvia l'interfaccia di visualizzazione delle operazioni riguardanti la gestione
    # delle prenotazioni
    def startUIPrenotazioni(self):
        self.home = Ui_Prenotazione()
        self.home.setupUi(self)
        try:
            self.home.caricaMostre()
        except Exception:
            self.home.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.home.nuovaLabel.setText("Errore nel caricamento delle mostre aperte")

        self.home.utenteLabel.setText(self.username)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.backButton.clicked.connect(self.goHome)
        self.home.inserisciButton.clicked.connect(self.home.savePrenotazione)

        self.home.visualizzaButton.clicked.connect(lambda: self.startListaPrenotazioni(self.home.getListaPrenotazioni()))
        self.home.qrButton.clicked.connect(lambda: self.startListaPrenotazioni(
            self.home.getPrenotazioneQr(
                QFileDialog.getOpenFileName(self, "Seleziona il png del Qr", os.path.dirname(os.path.realpath(__file__)),
                                            "Image Files(*.png)"))))
        self.show()

    # metodo che avvia la visualizzazione della lista prenotazioni filtrata
    def startListaPrenotazioni(self, listaPrenotazioni):
        self.home = UiLista()
        self.home.setupUi(self, listaPrenotazioni, 'prenotazione')
        self.home.utenteLabel.setText(self.username)
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.backButton.clicked.connect(self.startUIPrenotazioni)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))

        # metodo per selezionare una particolare prenotazione tra quelle presenti nella lista filtrata
        # al fine di visualizzare la relativa scheda completa
        def getIdPrenotazione(listaPrenotazioni):
            for visualizza_scheda in self.home.getVisualizzaCompleto():
                if visualizza_scheda.isChecked():
                    indexPrenotazione = self.home.getVisualizzaCompleto().index(visualizza_scheda)
                    return listaPrenotazioni[indexPrenotazione].getCodice()
            raise Exception("Impossibile visualizzare scheda prenotazione")

        for visualizza_scheda,prenotazione in zip(self.home.getVisualizzaCompleto(), listaPrenotazioni):
            visualizza_scheda.clicked.connect(lambda: self.startPrenotazioneComplete(getIdPrenotazione(listaPrenotazioni)))

    # metodo che avvia l'interfaccia di visualizzazione della scheda completa prenotazione
    def startPrenotazioneComplete(self,idPrenotazione):
        self.home = UiPrenotazioneComplete(idPrenotazione)
        self.home.setupUi(self)
        try:
            self.home.caricaMostre()
        except Exception:
            self.home.msgLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.home.msgLabel.setText("Errore nel caricamento delle opere in catalogo")

        self.home.setLabels()
        self.home.backButton.clicked.connect(self.startUIPrenotazioni)
        self.home.closeButton.clicked.connect(sys.exit)
        self.home.userLabel.setText(self.username)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.eliminaButton.clicked.connect(self.home.eliminaFunction)
        self.home.modificaButton.clicked.connect(self.home.modificaFunction)

    # metodo che avvia l'interfaccia di visualizzazione delle operazioni riguardanti la gestione visite
    def startUiVisite(self):
        self.home = UiVisite()
        self.home.setupUi(self)
        self.home.backButton.clicked.connect(self.goHome)
        self.home.utenteLabel.setText(self.username)
        self.home.accountMenu.activated.connect(lambda: self.gestioneAccount(self.home))
        self.home.minimizeButton.clicked.connect(self.showMinimized)
        self.home.closeButton.clicked.connect(sys.exit)

        listaIdMostre = []
        try:
            listaIdMostre = self.home.caricaMostre()
        except Exception:
            self.home.nuovaLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.home.nuovaLabel.setText("Errore nel caricamento delle mostre aperte")

        self.home.inserisciButton.clicked.connect(lambda: self.home.saveVisita(listaIdMostre))
        self.home.qrButton.clicked.connect(lambda: self.home.prenotazioneToVisitaQr(
            QFileDialog.getOpenFileName(self, "Seleziona il png del Qr", os.path.dirname(os.path.realpath(__file__)), "Image Files(*.png)"))
                                           )
        self.home.insCodiceButton.clicked.connect(self.home.prenotazioneToVisitaCodice)
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # metodo di reindirizzamento all'interfaccia home relativa al ruolo dell'account in utilizzo
    def goHome(self):
        if self.ruolo == "admin":
            self.startAdminHome()
        elif self.ruolo == "front_office":
            self.startFrontOfficeHome()
        elif self.ruolo == "catalogatore":
            self.startCatalogoHome()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            sys.exit()
        elif event.key() == QtCore.Qt.Key_Return and not self.username:
            self.accessoHome()

    # metodo per la gestione dell'accesso al programma in funzione del ruolo
    def accessoHome(self):
        self.con = MyDB.MyDB()
        try:
            accountID = self.home.verificaCredenziali()
            self.username = self.home.controller.getUsername()
            self.ruolo = self.home.controller.getRuolo()
            if accountID == 1001:
                self.startAdminHome()
            elif accountID == 1002:
                self.startFrontOfficeHome()
            elif accountID == 1003:
                self.startCatalogoHome()
            else:
                self.home.errorLabel.setText("Ooops, credenziali errate!")
        except Exception as e:
            self.home.errorLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.home.errorLabel.setText(e.args[0])


    # metodo di gestione delle opzioni fornite nelle combobox presenti nelle interfacce
    def gestioneAccount(self, view, notHome=True):
        if view.accountMenu.currentText() == "Logout":
            self.startLogin()
            self.con.connection.close()
        elif notHome:
            if view.accountMenu.currentText() == "Home":
                self.goHome()
        elif view.accountMenu.currentText() == "Modifica Password":
            self.startModificaPasswd()
        elif view.accountMenu.currentText() == "Struttura Museo":
            self.startModificaMuseo()

    # metodo che avvia l'interfaccia di modifica della struttura del museo
    def startModificaMuseo(self):
        strutturaMuseo = StrutturaMuseo()
        self.popUp.setUi(Ui_StrutturaMuseo())
        self.popUp.getUi().setupUi(self.popUp)
        self.popUp.getUi().newCapienzaMax.setText(str(strutturaMuseo.getCapienza()))
        self.popUp.getUi().closeButton.clicked.connect(self.popUp.close)
        self.popUp.getUi().minimizeButton.clicked.connect(self.popUp.showMinimized)
        self.popUp.getUi().salvaStruttura.clicked.connect(lambda: self.popUp.close() if strutturaMuseo.setNewStruttura(
            self.popUp.getUi().newSala.text(), self.popUp.getUi().newCapienzaMax.text())
                                                            else self.popUp.getUi().errorLabel.setText("Oops, qualcosa è andato storto!"))
        self.popUp.show()
