from mostra.model.Mostra import Mostra

# classe di gestione delle mostre
class ControllerMostra:
    def __init__(self):
        super(ControllerMostra, self).__init__()
        self.model = Mostra()
        self.listaMostre = []

    def getModel(self):
        return self.model

    # metodo per configurare l'attributo "model" con un oggetto "mostra" sul quale eseguire le varie
    # operazioni del controller
    def setModel(self, titolo, edizione, sala, data_inizio, data_fine, prezzo):
        self.model = Mostra(titolo, edizione, sala, data_inizio, data_fine, prezzo)

    # metodo per salvare la mostra nel database
    def saveMostra(self):
        try:
            return self.model.saveMostra()
        except Exception:
            raise

    # metodo per modificare un particolare campo della mostra
    def modificaDatoMostra(self, campoDaModificare, valoreNuovo):
        try:
            return self.model.modificaDatoMostra(campoDaModificare, valoreNuovo)
        except Exception:
            raise

    # metodo che restituisce la attuale lista delle mostre
    def getListaMostre(self):
        return self.listaMostre

    # metodo per svuotare la attuale lista delle mostre
    def emptyListaMostre(self):
        self.listaMostre = []

    # metodo per configurare la lista delle mostre mediante il filtraggio fornito
    def setListaMostre(self, filtri=None):
        try:
            return self.model.setListaMostre(filtri)
        except Exception:
            raise

    # metodo che restituisce una lista contenente le mostre in corso al momento della chiamata
    def mostreInCorso(self):
        try:
            return self.model.mostreInCorso()
        except Exception:
            raise

    # metodo per eliminare la mostra dal database
    def eliminaMostra(self, idMostra):
        try:
            self.model.eliminaMostra(idMostra)
        except Exception:
            raise

    # metodo per modificare più campi della mostra
    def modificaMostra(self, idMostra, filtri):
        try:
            self.model.modificaMostra(idMostra, filtri)
        except Exception:
            raise