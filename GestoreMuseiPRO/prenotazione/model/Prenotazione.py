import sqlite3
from database import MyDB
from datetime import datetime, date


# classe model della prenotazione
class Prenotazione:
    def __init__(self, codice=None, dataPrenotazione=None, dataVisita=None,
                 nominativo=None, telefono=None, ID_mostra=None, validita=1):
        super(Prenotazione, self).__init__()
        self.codice = codice
        self.dataPrenotazione = dataPrenotazione
        self.dataVisita = dataVisita
        self.nominativo = nominativo
        self.telefono = telefono
        self.IdMostra = ID_mostra
        self.validita = validita


    def getCodice(self):
        return self.checkPrenotazioneExists()

    def getDataPrenotazione(self):
        return self.dataPrenotazione

    def getDataVisita(self):
        return self.dataVisita

    def getNominativo(self):
        return self.nominativo

    def getTelefono(self):
        return self.telefono

    def getIDMostra(self):
        return self.IdMostra

    def getValidita(self):
        return self.validita

    def setCodice(self, codice):
        self.codice = codice

    def setDataPrenotazione(self, dataPrenotazione):
        self.dataPrenotazione = dataPrenotazione

    def setDataVisita(self, dataVisita):
        self.dataVisita = dataVisita

    def setNominativo(self, nominativo):
        self.nominativo = nominativo

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setIdMostra(self, IdMostra):
        self.IdMostra = IdMostra

    def setValidita(self, validita):
        self.validita = validita

    # metodo per verificare l'esistenza nel database della prenotazione
    def checkPrenotazioneExists(self):
        list = [self.dataPrenotazione, self.dataVisita, self.nominativo,
                self.telefono, self.IdMostra]
        exists = MyDB.db.connection.cursor().execute('SELECT codice FROM prenotazione WHERE data_prenotazione = ? '
                                                     'AND data_visita = ? AND nominativo = ? AND telefono = ? '
                                                     'AND ID_mostra = ? AND validita = 1', list).fetchone()
        if exists is None:
            return False
        else:
            self.codice = exists[0]
            return exists[0]

    # metodo per salvare la prenotazione nel database
    def savePrenotazione(self):
        try:
            if not self.checkPrenotazioneExists():
                sql = "INSERT INTO prenotazione VALUES(null, ?, ?, ?, ?, ?, ?);"
                data_tuple = (self.dataPrenotazione, self.dataVisita, self.nominativo,
                              self.telefono, self.IdMostra, self.validita)
                MyDB.db.connection.cursor().execute(sql, data_tuple)
                MyDB.db.connection.commit()
            else:
                raise Exception('Prenotazione già esistente nel database')
        except sqlite3.Error as e:
            raise Exception(e.args[0])

    # metodo per eliminare la prenotazione dal database
    def deletePrenotazione(self):
        self.modificaDatoPrenotazione('validita', 0)

    # metodo per modificare un particolare campo della prenotazione
    def modificaDatoPrenotazione(self, campoDaModificare, valoreNuovo):
        if campoDaModificare == 'data_visita':
            datetime.strptime(valoreNuovo, '%d-%m-%Y')
            n_prenotati = self.contaPrenotazioni(self.dataVisita).fetchall()
            if n_prenotati[0][0] >= 5:
                raise Exception('Non ci sono posti disponibili')
        try:
            if not self.checkPrenotazioneExists():
                raise Exception('Prenotazione non presente nel database')
            else:
                MyDB.db.connection.cursor().execute(
                    "UPDATE prenotazione SET {} = ?  WHERE codice = ?".format(campoDaModificare),
                    (valoreNuovo, self.codice))
                MyDB.db.connection.commit()
        except sqlite3.Error as e:
            raise Exception(e.args)

    # metodo che, dati in ingresso data e ora, restituisce il totale delle prenotazioni corrispondenti;
    # se l'ora non è specificata, restituirà tutte le prenotazioni del giorno stesso
    def contaPrenotazioni(self, dataVisita, oraVisita=None):
        sql = 'SELECT COUNT(*) FROM prenotazione WHERE validita = 1 AND data_visita = \'{}\''.format(dataVisita)
        if oraVisita is not None:
            sql = sql + ' AND ora_visita = \'{}\''.format(oraVisita)
        try:
            return MyDB.db.connection.cursor().execute(sql)
        except sqlite3.Error as e:
            raise Exception(e.args[0])

    # metodo che restituisce la lista delle prenotazioni filtrata secondo i criteri forniti
    def getPrenotazioneByFields(self, filtri=None):
        if not filtri:
            condition = ""
        else:
            condition = ""
            for key, value in dict(filtri).items():
                if value:
                    if type(value) is not tuple:
                        condition += key + " = \'" + str(value) + "\' AND "
                    else:
                        if not value[0]:
                            condition += key + " <= \'" + str(value[1]) + "\' AND "
                        elif not value[1]:
                            condition += key + " >= \'" + str(value[0]) + "\' AND "
                        else:
                            condition += key + " BETWEEN \'" + str(value[0]) + "\' AND \'" + str(value[1]) + "\' AND "
        condition +=  "validita = 1"
        try:
            result = MyDB.db.connection.cursor().execute("SELECT * FROM prenotazione WHERE {} ".format(condition))
            list = []
            for row in result:
                prenotazione = Prenotazione(row[0], row[1], row[2], row[3], row[4], row[5])
                list.append(prenotazione)
            return list
        except sqlite3.Error as e:
            raise Exception(e.args[0])

    # metodo che permette la modifica di campi della particolare prenotazioni fornita
    def updatePrenotazioneByFields(self, idPrenotazione, fieldValueList):
        condition = ""
        dim = len(dict(fieldValueList).items())
        contatore= 0
        for key, value in dict(fieldValueList).items():
            condition = condition + key + " = \'" + str(value) + "\'"
            contatore += 1
            if contatore != dim:
                condition += ", "
        try:
            MyDB.db.connection.cursor().execute("UPDATE prenotazione SET {0} WHERE codice={1}".format(
                condition, idPrenotazione))
            MyDB.db.connection.commit()
        except sqlite3.Error as e:
            raise Exception(e.args)

    #metodo che controlla quali prenotazioni non sono andate a buon fine e che quindi non sono diventate visite fino alla data odierna(ponendo validita =0)
    @staticmethod
    def verificaPrenotazioni():
        sub_query = "SELECT visita.codice_prenotazione FROM visita WHERE  visita.data<\'{}\'".format(
            date.today().strftime("%Y-%m-%d"))
        sql = 'UPDATE prenotazione SET validita = 0 WHERE codice NOT IN ({})'.format(sub_query)
        try:
            result = MyDB.db.connection.cursor().execute(sql)
            MyDB.db.connection.commit()
        except sqlite3.Error as e:
            raise Exception(e.args[0])