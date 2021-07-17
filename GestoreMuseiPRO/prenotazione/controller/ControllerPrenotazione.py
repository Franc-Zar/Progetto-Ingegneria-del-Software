from prenotazione.model.Prenotazione import Prenotazione

# classe di gestione per le operazioni riguardanti le prenotazioni
class ControllerPrenotazione:
    def __init__(self):
        super(ControllerPrenotazione, self).__init__()
        self.model = Prenotazione()

    def getModel(self):
        return self.model

    # metodo per modificare i valori dell'oggetto "prenotazione" presente nell'attributo "model"
    def setModel(self, codice, data_prenotazione, data_visita, nominativo, telefono, ID_mostra, validita=1):
        self.model.setCodice(codice)
        self.model.setDataPrenotazione(data_prenotazione)
        self.model.setDataVisita(data_visita)
        self.model.setNominativo(nominativo)
        self.model.setTelefono(telefono)
        self.model.setIdMostra(ID_mostra)

    def getCodice(self):
        return self.model.getCodice()

    def getDataPrenotazione(self):
        return self.model.getDataPrenotazione()

    def getDataVisita(self):
        return self.model.getDataVisita()

    def getNominativo(self):
        return self.model.getNominativo()

    def getTelefono(self):
        return self.model.getTelefono()

    def getIDMostra(self):
        return self.model.getIDMostra()

    # metodo per salvare l'oggetto "prenotazione" nel database
    def savePrenotazione(self):
        try:
            return self.model.savePrenotazione()
        except Exception:
            raise

    # metodo per eliminare l'oggetto "prenotazione" dal database
    def deletePrenotazione(self):
        try:
            return self.model.deletePrenotazione()
        except Exception:
            raise

    # metodo per la modifica di un particolare campo dell'oggetto "prenotazione"
    def modificaDatoPrenotazione(self, campoDaModificare, valoreNuovo):
        try:
            return self.model.modificaDatoPrenotazione(campoDaModificare, valoreNuovo)
        except Exception:
            raise

    # metodo che, dati in ingresso data e ora, restituisce il totale delle prenotazioni corrispondenti;
    # se l'ora non è specificata, restituirà tutte le prenotazioni del giorno stesso
    def contaPrenotazioni(self, dataVisita, oraVisita=None):
        try:
            return self.model.contaPrenotazioni(dataVisita, oraVisita)
        except Exception:
            raise

    # metodo che restituisce la lista delle prenotazioni filtrata secondo i criteri forniti
    def getPrenotazioneByFields(self, fieldValueList=None):
        try:
            return self.model.getPrenotazioneByFields(fieldValueList)
        except Exception:
            raise

    # metodo che permette la modifica di campi della particolare prenotazioni fornita
    def updatePrenotazioneByFields(self, idPrenotazione, fieldValueList):
        try:
            return self.model.updatePrenotazioneByFields(idPrenotazione, fieldValueList)
        except Exception:
            raise

    def verificaPrenotazioni(self):
        try:
            self.model.verificaPrenotazioni()
        except Exception:
            raise