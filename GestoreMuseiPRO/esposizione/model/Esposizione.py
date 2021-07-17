import sqlite3
import database.MyDB as MyDB


class Esposizione():
    def __init__(self, dataInizio=None, codiceOpera=None, idMostra=None, dataFine=None):
        super(Esposizione, self).__init__()
        self.dataInizio = dataInizio
        self.codiceOpera = codiceOpera
        self.idMostra = idMostra
        self.dataFine = dataFine

    # metodo usato per aggiungere opera ad una mostra e salvarla nel db
    def saveEsposizione(self):
        sql = ''' INSERT INTO esposizione (data_inizio, codice_opera, ID_mostra, data_fine) VALUES(?,?,?,?) '''
        try:
            MyDB.db.connection.cursor().execute(sql, (self.dataInizio,
                                                      self.codiceOpera, self.idMostra, self.dataFine))
            MyDB.db.connection.commit()
        except sqlite3.Error as e:
            if 'UNIQUE' in str(e):
                raise Exception('Esposizione esistente nel database')
            else:
                raise e

    def modificaFineEsposizione(self, newValue):
        try:
            # to do: check delle date
            result = MyDB.db.connection.cursor().execute("UPDATE esposizione SET data_fine = ?  "
                                                         "WHERE data_inizio = ? AND codice_opera = ? AND ID_mostra = ? ",
                                                         (newValue, self.dataInizio, self.codiceOpera,
                                                          self.idMostra))
            MyDB.db.connection.commit()
        except sqlite3.Error as e:
            raise e

    @staticmethod
    def getEsposizioneByFields(fieldValueList=None):
        if fieldValueList == None:
            condition = 1  # se non specifico la condizione, restituisce la lista intera
        else:
            condition = ""
            for key, value in dict(fieldValueList).items():
                condition = condition + key + " = \'" + str(value) + "\' AND "
            condition += "1"
        try:
            result = MyDB.db.connection.cursor().execute("SELECT * FROM esposizione WHERE {}".format(condition))
        except sqlite3.Error as e:
            raise e
        list = []
        for row in result:
            e = Esposizione(row[0], row[1], row[2], row[3])
            list.append(e)
        return list

    def eliminaEsposizione(self, idMostra):
        try:
            MyDB.db.connection.cursor().execute(
                "DELETE FROM esposizione WHERE ID_mostra={}".format(idMostra))
            MyDB.db.connection.commit()
        except sqlite3.Error as e:
            raise e
