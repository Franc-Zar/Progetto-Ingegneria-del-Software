import sqlite3
from datetime import datetime

from opera.ModelOpera.Opera import Opera

# classe controller per la gestione del catalogo opere
class GestioneCatalogo:
    def __init__(self):
        super(GestioneCatalogo, self).__init__()
        self.model = Opera()
        self.listaOpere = []

    # metodo per configurare l'attributo "model" con l'oggetto "opera" sul quale eseguire le operazioni
    def setModel(self, model):
        self.model = model

    def getListaOpere(self):
        return self.listaOpere

    def emptyListaOpere(self):
        self.listaOpere = []

    # metodo per configurare la lista delle opere filtrata mediante le condizioni fornite
    def setListaOpere(self, codice=None, titolo=None, autore=None, tipologia=None, dataAcquisizioneMin=None, dataAcquisizioneMax=None,
                      annoProduzioneMin=None, annoProduzioneMax=None, valoreMin=None, valoreMax=None):
        if not self.listaOpere:
            filtri = {}
            if codice:
                filtri['codice'] = codice

            if titolo:
                filtri['titolo'] = titolo

            if autore:
                filtri['artista'] = autore

            if tipologia:
                filtri['tipologia'] = tipologia

            if dataAcquisizioneMin or dataAcquisizioneMax:
                filtri['data_acquisizione'] = (dataAcquisizioneMin,dataAcquisizioneMax)

            if annoProduzioneMin or annoProduzioneMax:
                filtri['anno_produzione'] = (annoProduzioneMin, annoProduzioneMax)

            if valoreMin or valoreMax:
                filtri['valore'] = (valoreMin, valoreMax)

            self.listaOpere = self.getOpereFiltrate(filtri)


    # metodo per modificare i campi dell'opera
    def modificaOpera(self, titolo=None, codice=None, tipologia=None, valore=None, dataAcquisizione=None,
                      annoProduzione=None, autore=None, immagine=None, dimensioni=None):
        try:
            try:
                if titolo:
                    if self.modificaDatoOpera("titolo", titolo):
                        self.model.setTitolo(titolo)

                if codice and type(int(codice)) is int:
                    self.modificaDatoOpera("codice", codice)

                if tipologia:
                    self.modificaDatoOpera("tipologia", tipologia)

                if valore and type(float(valore)) is float:
                    if self.modificaDatoOpera("valore", valore):
                        self.model.setValore(valore)

                if dataAcquisizione and type(datetime.strptime(dataAcquisizione,'%Y-%m-%d')) is datetime:
                    self.modificaDatoOpera("data_acquisizione", dataAcquisizione)

                if annoProduzione and type(int(annoProduzione)) is int:
                    if self.modificaDatoOpera("anno_produzione", annoProduzione):
                        self.model.setAnnoProduzione(annoProduzione)

                if autore:
                    if self.modificaDatoOpera("artista", autore):
                        self.model.setAutore(autore)

                if immagine:
                    self.modificaDatoOpera("img", immagine)

                if dimensioni:
                    self.modificaDatoOpera("dimensioni", dimensioni)
                return True
            except ValueError:
                return False
        except sqlite3.Error:
            return False

    # metodo per aggiungere un'opera al database
    def aggiungiOpera(self, titolo, autore, tipologia, dimensioni, anno_produzione, immagine, data_acquisizione, valore):
        try:
            try:
                if self.inserisciOpera(titolo, autore, tipologia, dimensioni, anno_produzione,
                                       immagine, data_acquisizione, valore):
                    return self.salvaOpera()
            except sqlite3.Error:
                raise
        except Exception:
            raise


    def getModel(self):
        return self.model

    # metodo per modificare i campi dell'oggetto "mostra" presente in "model"
    def inserisciOpera(self, titolo, autore, tipologia, dimensioni, anno_produzione, img, data_acquisizione, valore):
        return self.model.inserisciOpera(titolo, autore, tipologia, dimensioni, anno_produzione, img, data_acquisizione,
                                         valore)

    # metodo per salvare l'opera nel database
    def salvaOpera(self):
        return self.model.salvaOpera()

    # metodo per eliminare l'opera dal database
    def eliminaOpera(self):
        try:
            return self.model.eliminaOpera()
        except sqlite3.Error:
            raise

    # metodo per modificare un particolare campo dell'opera
    def modificaDatoOpera(self, campo_da_modificare, valore_nuovo):
        return self.model.modificaDatoOpera(campo_da_modificare, valore_nuovo)

    # metodo per ottenere la lista contenente le opere che rispettano i criteri di filtraggio forniti
    def getOpereFiltrate(self, field_value_list=None):
        return self.model.getOpereFiltrate(field_value_list)