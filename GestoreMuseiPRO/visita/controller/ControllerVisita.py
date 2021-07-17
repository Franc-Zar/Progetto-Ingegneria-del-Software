from datetime import datetime

from prenotazione.controller.ControllerPrenotazione import ControllerPrenotazione
from visita.model.Visita import Visita


class ControllerVisita():
    def __init__(self):
        super(ControllerVisita, self).__init__()
        self.model = Visita()

        self.prenotazione = ControllerPrenotazione()

    def setModel(self, data, tariffa, codice_prenotazione, ora_ingresso):
        self.model.setData(data)
        self.model.setTariffa(tariffa)
        self.model.setOraIngresso(ora_ingresso)
        self.model.setCodicePrenotazione(codice_prenotazione)


    def setPrenotazione(self,data, nominativo, telefono, ID_mostra):
        self.prenotazione.setModel(
            None, data, data, nominativo, telefono, ID_mostra
            )
        self.prenotazione.model.codice = self.prenotazione.getCodice()
        try:
            self.prenotazione.savePrenotazione()
        except Exception as e:
            raise

    # ATTENZIONE: i controlli per data e ora sono dati per fatti
    def convertiPrenotazione(self, codice, tariffa, orario):
        listaprenotazione = self.prenotazione.getPrenotazioneByFields({'codice':codice})
        if listaprenotazione:
            if not self.model.getVisitaByFields({'codice_prenotazione': codice}):
                self.prenotazione.model = listaprenotazione[0]
                data = self.prenotazione.getDataVisita()
                if data == datetime.today().strftime("%Y-%m-%d"):
                    self.setModel(data, tariffa, codice, orario)
                    try:
                        self.model.saveVisita()
                    except Exception:
                        raise
                else:
                    raise Exception('La prenotazione non è per il giorno corrente')
            else:
                raise Exception('Esiste già una visita corrispondente questa prenotazione')
        else:
            raise Exception('Non esiste una prenotazione corrispondente questo codice')


    def saveVisita(self, data, ora_ingresso, tariffa, nominativo, telefono, ID_mostra):
        try:
            self.setPrenotazione(data, nominativo, telefono, ID_mostra)
            self.setModel(data, tariffa, None, ora_ingresso)

            self.model.setCodicePrenotazione(self.prenotazione.model.checkPrenotazioneExists())
            return self.model.saveVisita()
        except Exception:
            raise

    def contaVisite(self, dataVisita, oraVisita=None):
        return self.model.contaVisite(dataVisita, oraVisita)
