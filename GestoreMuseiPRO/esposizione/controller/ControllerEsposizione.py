from esposizione.model.Esposizione import Esposizione


class ControllerEsposizione:
    def __init__(self):
        super(ControllerEsposizione, self).__init__()
        self.model = Esposizione()

    def setModel(self, data_inizio, codice_opera, ID_mostra, data_fine):
        self.model = Esposizione(data_inizio,codice_opera,ID_mostra,data_fine)

    def saveEsposizione(self):
        try:
            return self.model.saveEsposizione()
        except Exception:
            raise

    def modificaFineEsposizione(self, newValue):
        try:
            return self.model.modificaFineEsposizione(newValue)
        except Exception:
            raise

    def getEsposizioneByFields(self, fieldValueList=None):
        try:
            return self.model.getEsposizioneByFields(fieldValueList)
        except Exception:
            raise

    def eliminaEsposizione(self, idMostra):
        try:
            self.model.eliminaEsposizione(idMostra)
        except Exception:
            raise
