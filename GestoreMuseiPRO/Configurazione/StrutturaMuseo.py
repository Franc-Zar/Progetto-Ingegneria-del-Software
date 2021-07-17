import json
import os

# classe che permette di interagire con l'omonimo file .json di configurazione per modificare il numero
# massimo di visitatori possibili e aggiungere nuove sale all'interno del museo
class StrutturaMuseo:
    def __init__(self):
        self.setStruttura()

    def getSale(self):
        return self.sale

    def getCapienza(self):
        return self.capienza

    def setCapienza(self,capienza):
        self.capienza = capienza

    def setSale(self, sale):
        self.sale = sale

    # metodo richiamato nel costruttore per impostare gli attributi dell'oggetto con i valori corrispondenti
    # presenti al momento della creazione nel file di configurazione .json
    def setStruttura(self):
        baseDir = os.path.dirname(os.path.abspath(__file__))
        pathStruttura = os.path.join(baseDir, "StrutturaMuseo.json")

        with open(pathStruttura) as configurazione:
            strutturaMuseo = json.load(configurazione)

        self.sale = strutturaMuseo['Struttura Museo']['sale']
        self.capienza = strutturaMuseo['Struttura Museo']['n_prenotazioni_max']

        configurazione.close()

    # metodo per aggiornare il file di configurazione .json con i nuovi parametri forniti
    def setNewStruttura(self,newSala=None,newCapienza=None):
        try:
            baseDir = os.path.dirname(os.path.abspath(__file__))
            pathStruttura = os.path.join(baseDir, "StrutturaMuseo.json")

            with open(pathStruttura, 'r+') as configurazione:
                strutturaMuseo = json.load(configurazione)

                if newSala:
                    strutturaMuseo['Struttura Museo']['sale'].append(newSala)
                    self.sale = strutturaMuseo['Struttura Museo']['sale']

                if newCapienza:
                    if type(int(newCapienza)) is int:
                        strutturaMuseo['Struttura Museo']['n_prenotazioni_max'] = int(newCapienza)
                        self.capienza = newCapienza
                    else:
                        return False

                configurazione.seek(0)
                json.dump(strutturaMuseo, configurazione, indent=4)
                configurazione.truncate()

                configurazione.close()
                return True
        except Exception:
            return False