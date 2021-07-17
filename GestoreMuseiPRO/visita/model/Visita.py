import sqlite3

from database import MyDB


class Visita:
    def __init__(self, codice=None, data=None, oraIngresso=None, tariffa=None, codicePrenotazione=None):
        super(Visita, self).__init__()
        self.codice = codice
        self.data = data
        self.oraIngresso = oraIngresso
        self.tariffa = tariffa
        self.codicePrenotazione = codicePrenotazione

    def setData(self, data):
        self.data = data

    def setTariffa(self, tariffa):
        self.tariffa = tariffa

    def setCodicePrenotazione(self, codicePrenotazione):
        self.codicePrenotazione = codicePrenotazione

    def setOraIngresso(self, oraIngresso):
        self.oraIngresso = oraIngresso


    def checkVisitaExists(self):
        list = [self.data, self.oraIngresso, self.tariffa, self.codicePrenotazione]
        exists = MyDB.db.connection.cursor().execute('SELECT codice FROM visita WHERE data = ? AND ora_ingresso = ?'
                                                     'AND tariffa = ? AND codice_prenotazione = ? ', list).fetchone()
        if not exists:
            return False
        else:
            self.codice = exists[0]
            return exists[0]

    def saveVisita(self):
        try:
            if not self.checkVisitaExists():
                sql = "INSERT INTO visita VALUES (null, ?, ?, ?, ?);"
                data_tuple = (self.data, self.oraIngresso, self.tariffa, self.codicePrenotazione)
                MyDB.db.connection.cursor().execute(sql, data_tuple)
                MyDB.db.connection.commit()
            else:
                raise Exception('Visita già esistente nel database')
        except sqlite3.Error as e:
            raise Exception(e.args[0])


    #metodo che dati in ingresso data e ora, restituiscono il totale delle visite effettuate in quel  dato momento
    #se l'ora non è specificata, restituirà le visite della giornata totale
    @staticmethod
    def contaVisite(data, oraIngresso = None):
        sql = 'SELECT COUNT(*) FROM visita WHERE data = \'{}\''.format(data)
        if not oraIngresso:
            sql = sql + ' AND ora_ingresso = \'{}\''.format(oraIngresso)
        try:
            result = MyDB.db.connection.cursor().execute(sql)
        except sqlite3.Error as e:
            raise Exception(e.args)
        return result

    @staticmethod
    def getVisitaByFields(fieldValueList=None):
        if not fieldValueList:
            condition = 1
        else:
            condition = ""
            for key, value in dict(fieldValueList).items():
                condition = condition + key + " = \'" + str(value) + "\' AND "
            condition = condition + "1"
        try:
            result = MyDB.db.connection.cursor().execute("SELECT * FROM visita WHERE {} ".format(condition))
        except sqlite3.Error as e:
            raise Exception(e.args)
        list = []
        for row in result:
            visita = Visita(row[0], row[1], row[3], row[4], row[2])
            list.append(visita)
        return list
