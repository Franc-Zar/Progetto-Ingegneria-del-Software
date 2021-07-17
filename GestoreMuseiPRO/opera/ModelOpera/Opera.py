import sqlite3
from datetime import datetime

import database.MyDB as MyDB

# classe model dell'opera
class Opera:
    def __init__(self, titolo=None, valore=None, autore=None, dimensioni=None, tipologia=None, anno_produzione=None, img=None, data_acquisizione=None):
        super(Opera, self).__init__()
        self.codice = None
        self.presente = 1
        self.titolo = titolo
        self.valore = valore
        self.autore = autore
        self.dimensioni = dimensioni
        self.tipologia = tipologia
        self.anno_produzione = anno_produzione
        self.img = img
        self.data_acquisizione = data_acquisizione

    def setCodice(self,codice):
        self.codice = codice

    def setTitolo(self,titolo):
        self.titolo = titolo

    def setValore(self,valore):
        self.valore = valore

    def setAutore(self,autore):
        self.autore = autore

    def setDimensioni(self,dimensioni):
        self.dimensioni = dimensioni

    def setTipologia(self,tipologia):
        self.tipologia = tipologia

    def setAnnoProduzione(self,annoProduzione):
        self.anno_produzione = annoProduzione

    def setImg(self,img):
        self.img = img

    def setDataAcquisizione(self,dataAcquisizione):
        self.data_acquisizione = dataAcquisizione

    def getCodice(self):
        return self.codice

    def getTitolo(self):
        return self.titolo

    def getValore(self):
        return self.valore

    def getAutore(self):
        return self.autore

    def getDimensioni(self):
        return self.dimensioni

    def getTipologia(self):
        return self.tipologia

    def getAnnoProduzione(self):
        return self.anno_produzione

    def getImg(self):
        return self.img

    def getDataAcquisizione(self):
        return self.data_acquisizione


    # metodo per modificare i vari attributi della mostra
    def inserisciOpera(self, titolo, autore, tipologia, dimensioni, annoProduzione, img, dataAcquisizione, valore):
       if titolo and autore and tipologia and dimensioni and annoProduzione \
               and type(int(annoProduzione)) is int and img and dataAcquisizione and type(datetime.strptime(dataAcquisizione,'%Y-%m-%d')) is datetime\
               and valore and type(float(valore)) is float:
            self.titolo = titolo
            self.valore = valore
            self.autore = autore
            self.dimensioni = dimensioni
            self.tipologia = tipologia
            self.anno_produzione = annoProduzione
            self.img = img
            self.data_acquisizione = dataAcquisizione
            return True
       raise Exception

    # metodo per verificare se l'opera è già presente nel database
    def operaExists(self):
        try:
            list = [self.titolo, self.valore, self.autore, self.anno_produzione]

            exists = MyDB.db.connection.cursor().execute('SELECT codice FROM opera WHERE titolo = ? '
                           'AND valore = ? AND artista = ? AND anno_produzione = ? AND presente = 1', list).fetchone()
            if not exists:
                return False
            else:
                return True
        except sqlite3.Error:
            return False

    # metodo per salvare l'opera nel database
    def salvaOpera(self):
        try:
            if not self.operaExists():
                sql = "INSERT INTO opera VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
                data_tuple = (self.titolo, self.valore, self.autore, self.dimensioni, self.tipologia, self.anno_produzione, self.img, self.data_acquisizione, self.presente)
                MyDB.db.connection.cursor().execute(sql, data_tuple)
                MyDB.db.connection.commit()
                return True
            else:
                connection = MyDB.db.connection
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * FROM opera WHERE titolo = ? AND artista = ? "
                    "AND valore = ? AND dimensioni = ? AND tipologia = ? AND anno_produzione = ? AND img = ?"
                    "AND data_acquisizione = ? and presente = 0",
                    (self.titolo, self.autore, self.valore, self.dimensioni,
                     self.tipologia, self.anno_produzione, self.img, self.data_acquisizione))
                rimossa = cursor.fetchone()

                if rimossa:
                    cursor.execute(
                        "UPDATE opera SET presente = 1  WHERE titolo = ? AND artista = ? "
                    "AND valore = ? AND dimensioni = ? AND tipologia = ? AND anno_produzione = ? AND img = ?"
                    "AND data_acquisizione = ?",
                        (self.titolo, self.autore, self.valore, self.dimensioni, self.tipologia, self.anno_produzione, self.img))
                    connection.commit()
                    return True
                else:
                    raise sqlite3.Error
        except sqlite3.Error:
            raise

    # metodo per eliminare l'opera dal database
    def eliminaOpera(self):
        try:
            if self.modificaDatoOpera('presente', 0):
                return True
        except sqlite3.Error:
            raise

    # metodo per modificare un particolare dato dell'opera
    def modificaDatoOpera(self, campo_da_modificare, valore_nuovo):
        try:
            if self.operaExists():
                MyDB.db.connection.cursor().execute("UPDATE opera SET {} = ?  WHERE codice = ?".format(campo_da_modificare), (valore_nuovo, self.codice))
                MyDB.db.connection.commit()
                return True
        except sqlite3.Error:
            raise

    # metodo che restituisce una lista di opere filtrate secondo i criteri forniti
    @staticmethod
    def getOpereFiltrate(field_value_list=None):
        if not field_value_list:
            condition = ""
        else:
            condition = ""
            for key, value in dict(field_value_list).items():
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
        condition += "presente = 1"

        try:
            result = MyDB.db.connection.cursor().execute("SELECT * FROM opera WHERE {}".format(condition))
        except sqlite3.Error:
            return []
        list = []
        for row in result:
            opera = Opera(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            opera.codice = row[0]
            list.append(opera)
        return list