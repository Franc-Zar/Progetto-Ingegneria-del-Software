import datetime
import sqlite3

from database import MyDB

# classe model della mostra
class Mostra:
    def __init__(self, titolo=None, edizione=None, sala=None, data_inizio=None, data_fine=None, prezzo=None):
        super(Mostra, self).__init__()
        self.ID = None
        self.titolo = titolo
        self.edizione = edizione
        self.sala = sala
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.prezzo = prezzo


    def getID(self):
        return self.ID

    def getTitolo(self):
        return self.titolo

    def getEdizione(self):
        return self.edizione

    def getSala(self):
        return self.sala

    def getDataInizio(self):
        return self.data_inizio

    def getDataFine(self):
        return self.data_fine

    def getPrezzo(self):
        return self.prezzo

    # metodo per verificare se la mostra è presente nel database
    def checkMostraExists(self):
        # confronto solo i campi più significativi
        list = [self.titolo, self.edizione, self.sala]
        exists = MyDB.db.connection.cursor().execute('SELECT ID FROM mostra WHERE titolo = ? '
                                                     'AND edizione = ? AND sala = ? ', list).fetchone()
        if not exists:
            return False
        else:
            self.ID = exists[0]
            return exists[0]

    # metodo per salvare una mostra nel database
    def saveMostra(self):
        try:
            if not self.checkMostraExists():
                sql = "INSERT INTO mostra VALUES(null, ?, ?, ?, ?, ?, ?);"
                data_tuple = (self.titolo, self.edizione, self.sala, self.data_inizio, self.data_fine, self.prezzo)
                MyDB.db.connection.cursor().execute(sql, data_tuple)
                MyDB.db.connection.commit()
                self.checkMostraExists()  # la invoco cosìcché l'ID assegnato dal db venga salvato nella classe
            else:
                raise Exception('Mostra esistente nel database')
        except sqlite3.Error as e:
            raise Exception(e.args)

    # metodo per terminare una mostra ancora in corso
    def terminaMostra(self, dataFine):
        self.modificaDatoMostra('data_fine', dataFine)

    # metodo per modificare un particolare campo della mostra
    def modificaDatoMostra(self, campo_da_modificare, valore_nuovo):
        try:
            if not self.checkMostraExists():
                raise Exception('Mostra non presente nel db')
            else:
                MyDB.db.connection.cursor().execute(
                    "UPDATE mostra SET {} = ?  WHERE ID = ?".format(campo_da_modificare), (valore_nuovo, self.ID))
                MyDB.db.connection.commit()
        except sqlite3.Error as e:
            raise Exception(e.args)

    # metodo che restituisce la lista delle mostre che rispettano le condizioni del filtraggio considerato
    def setListaMostre(self, filtri=None):
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
        condition += "true"
        try:
            result = MyDB.db.connection.cursor().execute("SELECT * FROM mostra WHERE {}".format(condition))
        except sqlite3.Error as e:
            raise Exception(e.args)
        list = []
        for row in result:
            lista = Mostra(row[1], row[2], row[3], row[4], row[5], row[6])
            lista.codice = row[0]
            list.append(lista)
        return list

    # metodo che restituisce una lista contenente le mostre in corso al momento della chiamata
    def mostreInCorso(self):
        try:
            result = MyDB.db.connection.cursor().execute(
                "SELECT * FROM mostra WHERE data_inizio<='{0}' and (data_fine is '' OR data_fine>='{0}')".format(
                    datetime.date.today().strftime("%Y-%m-%d")
                )
            )
            list = []
            if result:
                for row in result:
                    mostra = Mostra(row[1], row[2], row[3], row[4], row[5], row[6])
                    mostra.ID = row[0]
                    list.append(mostra)
            return list
        except Exception as er:
            raise Exception(er.args[0])

    # metodo per eliminare la mostra dal database
    def eliminaMostra(self, idMostra):
        try:
            MyDB.db.connection.cursor().execute(
                "DELETE FROM mostra WHERE ID={}".format(idMostra))
            MyDB.db.connection.commit()
        except sqlite3.Error:
            raise

    # metodo per modificare più campi della mostra mediante i filtri considerati
    def modificaMostra(self, id_mostra, filtri):
        condition = ""
        dim = len(dict(filtri).items())
        contatore = 0
        for key, value in dict(filtri).items():
            condition = condition + key + " = \'" + str(value) + "\'"
            contatore += 1
            if contatore != dim:
                condition += ", "
        try:
            MyDB.db.connection.cursor().execute("UPDATE mostra SET {0} WHERE ID={1}".format(condition, id_mostra))
            MyDB.db.connection.commit()
        except sqlite3.Error as e:
            raise Exception(e.args)



    @staticmethod
    def getMostreAttive(data):  # ad una certa data
        try:
            # result = MyDB.db.connection.cursor().execute("SELECT * FROM mostra WHERE data_inizio<=\'{0}\' AND (data_fine is NULL OR data_fine>=\'{1}\')".format(data, data))

            result = MyDB.db.connection.cursor().execute(
                "SELECT * FROM mostra WHERE substr(data_inizio, 1, 4)|| substr(data_inizio, 6, 2) || substr(data_inizio, 9, 2) <= substr(\'{0}\', 1,4) || substr(\'{1}\', 6, 2) || substr(\'{2}\', 9, 2)  and (data_fine is NULL OR substr(data_fine, 1,4) || substr(data_fine, 6, 2) || substr(data_fine, 9,2) >= substr(\'{3}\', 1,4) || substr(\'{4}\', 6, 2) || substr(\'{5}\', 9, 2) )".format(
                    data, data, data, data, data, data))
        except sqlite3.Error as e:
            print(e)
            return
        list = []
        for row in result:
            M = Mostra(row[1], row[2], row[3], row[4], row[6], row[5])
            M.ID = row[0]
            list.append(M)
        return list


    @staticmethod
    def getMostreAttiveMese(
            data): 
        try:
            result = MyDB.db.connection.cursor().execute("SELECT * FROM mostra "
                                                         "WHERE substr(data_inizio, 1,4)|| substr(data_inizio, 6, 2)<= substr(\'{0}\', 1,4) || substr(\'{1}\', 6, 2) and (data_fine is NULL OR substr(data_fine, 1,4) || substr(data_fine, 6, 2)  >= substr(\'{2}\', 1,4) || substr(\'{3}\', 6, 2))".format(
                data, data, data, data))
        except sqlite3.Error as e:
            print(e)
            return
        list = []
        for row in result:
            M = Mostra(row[1], row[2], row[3], row[4], row[6], row[5])
            M.ID = row[0]
            list.append(M)
        return list

