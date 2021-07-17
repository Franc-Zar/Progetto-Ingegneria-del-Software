import sqlite3
from Dipendenti.ModelDipendenti.Dipendente import Dipendente

# controller per le funzionalità riguardanti la gestione del personale
class ControllerDipendente:
    def __init__(self):
        super(ControllerDipendente, self).__init__()
        self.model = Dipendente()
        self.listaDipendenti = []

    def setModel(self,model):
        self.model = model

    def getModel(self):
        return self.model

    def getListaDipendenti(self):
        return self.listaDipendenti

    def emptyListaDipendenti(self):
        self.listaDipendenti = []

    # metodo per inizializzare la lista dei dipendenti in funzione dei possibili parametri di filtraggio
    # forniti
    def setListaDipendenti(self,username=None,cf=None,nominativo=None,ruolo=None):
            if not self.listaDipendenti:
                filtri = {}
                if username:
                    filtri['username'] = username
                if cf:
                    filtri['cf'] = cf
                if nominativo:
                    filtri['nominativo'] = nominativo
                if ruolo:
                    filtri['ruolo'] = ruolo
                self.listaDipendenti = self.getLlavoratoreByFields(filtri)


    # metodo per aggiungere un nuovo dipendente nella tabella del database riservata al personale
    def aggiungiDipendente(self, username, cf, nominativo, ruolo):
        try:
            if self.inserisciDipendente(username, cf, nominativo, ruolo, True):
                try:
                    return self.salvaDipendente()
                except sqlite3.Error:
                    raise
        except Exception:
            raise

    # metodo per configurare l'attributo "model" del controller con un dipendente per poter eseguire operazioni su
    # quest'ultimo
    def inserisciDipendente(self,username,cf,nominativo,ruolo,newDipendente):
        try:
            return self.model.inserisciDipendente(username,cf,nominativo,ruolo,newDipendente)
        except Exception:
            raise

    # metodo che esegue operazioni direttamente correlate al salvataggio nel database del dipendente presente
    # nell'attributo "model"
    def salvaDipendente(self):
        try:
            return self.model.salvaDipendente()
        except sqlite3.Error:
            raise

    # metodo per eliminare il dipendente presente nell'attributo "model" dalla tabella del database
    # riservata al personale
    def deleteLavoratoreByUsername(self):
        try:
            return self.model.deleteLavoratoreByUsername()
        except sqlite3.Error:
            raise

    # metodo per modificare un campo del dipendente presente nell'attributo "model"
    def modificaDatoLavoratore(self, campoDaModificare, valoreNuovo):
        return self.model.modificaDatoLavoratore(campoDaModificare, valoreNuovo)

    # metodo per eseguire il filtraggio, in funzione del dizionario fornito, all'interno della tabella
    # del personale nel database. Restituisce una lista popolata con i dipendenti che soddisfano le varie
    # condizioni di filtraggio
    def getLlavoratoreByFields(self, fieldValueList=None):
        return self.model.getLavoratoreByFields(fieldValueList)

    # metodo per eseguire la modifica di più campi del dipendente presente nell'attributo "model"
    def modificaDipendente(self, username=None, cf=None, ruolo=None, nominativo=None):
        try:
            if cf:
                self.modificaDatoLavoratore("cf", cf)
            if ruolo:
                self.modificaDatoLavoratore("ruolo", ruolo)
            if nominativo:
                if self.modificaDatoLavoratore("nominativo", nominativo):
                    self.model.setNominativo(nominativo)
            if username:
                self.modificaDatoLavoratore("username", username)
            return True
        except sqlite3.Error:
            return False
