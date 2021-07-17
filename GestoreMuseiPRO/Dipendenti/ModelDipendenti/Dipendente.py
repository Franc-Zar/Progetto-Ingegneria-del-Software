import hashlib
import os
import sqlite3
import database.MyDB as MyDB

# classe model dell'entità "dipendente"
class Dipendente:
    def __init__(self, username=None, cf=None, nominativo=None, ruolo=None):
        super(Dipendente, self).__init__()
        self.username = username
        self.password = None
        self.cf = cf
        self.nominativo = nominativo
        self.ruolo = ruolo
        self.assunto = 1

    def setUsername(self,username):
        self.username = username

    def setCf(self,cf):
        self.cf = cf

    def setNominativo(self,nominativo):
        self.nominativo = nominativo

    def setRuolo(self,ruolo):
        self.ruolo = ruolo

    def getUsername(self):
        return self.username

    def getCf(self):
        return self.cf

    def getNominativo(self):
        return self.nominativo

    def getRuolo(self):
        return self.ruolo


    #verifica se il dipendente è già presente nel database
    def checkLavoratoreExists(self):
        try:
            connection = MyDB.db.connection
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM lavoratore WHERE username = ? AND nominativo = ? and cf = ?', (self.username,self.nominativo,self.cf))
            exists = cursor.fetchone()
            if exists:
                return True
            return False
        except sqlite3.Error:
            return False

    # metodo "setter" per tutti gli attributi dell'oggetto "dipendente";
    # se "newDipendente" è True viene generata una nuova password per poi poter salvare il dipendente nel
    # database
    def inserisciDipendente(self,username,cf,nominativo,ruolo,newDipendente):
        if username and cf and nominativo and (ruolo == 'admin' or ruolo == 'catalogatore' or ruolo == 'front_office'):
            self.username = username
            self.cf = cf
            self.nominativo = nominativo
            self.ruolo = ruolo
            if newDipendente:
                self.generaNuovaPasswd()
            return True
        raise Exception

    # metodo che consente il salvataggio del dipendente nel database
    def salvaDipendente(self):
        connection = MyDB.db.connection
        INSERT_LAVORATORE = "INSERT INTO lavoratore (username, password, cf, nominativo, ruolo, assunto) VALUES(?,?,?,?,?,?) "
        try:
            c = connection.cursor()
            if not self.checkLavoratoreExists():
                c.execute(INSERT_LAVORATORE, (self.username, self.password, self.cf, self.nominativo, self.ruolo, self.assunto))
                connection.commit()
                return True
            else:
                connection = MyDB.db.connection
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM lavoratore WHERE username = ? AND nominativo = ? AND ruolo = ? AND cf = ? AND assunto = 0", (self.username,self.nominativo,self.ruolo,self.cf))
                licenziato = cursor.fetchone()

                if licenziato:
                    c.execute(
                        "UPDATE lavoratore SET assunto = 1  WHERE username = ? AND nominativo = ? AND ruolo = ? AND cf = ?",
                        (self.username, self.nominativo, self.ruolo, self.cf))
                    connection.commit()
                    return True
                else:
                    raise sqlite3.Error
        except sqlite3.Error:
            raise


    # metodo per l'eliminazione dell'oggetto "dipendente" dal database
    def deleteLavoratoreByUsername(self):
        try:
            if self.modificaDatoLavoratore('assunto', 0):
                return True
        except sqlite3.Error:
            raise

    # metodo per la modifica di un campo dell'oggetto "dipendente" nel database
    def modificaDatoLavoratore(self, campo_da_modificare, valore_nuovo):
        connection = MyDB.db.connection
        try:
            if self.checkLavoratoreExists():
                c = connection.cursor()
                c.execute("UPDATE lavoratore SET {} = ?  WHERE username = ?".format(campo_da_modificare), (valore_nuovo, self.username))
                connection.commit()
                return True
            return False
        except sqlite3.Error:
            raise

    # metodo che restituisce una lista di oggetti "dipendente" in funzione dei parametri di filtraggio
    # forniti
    @staticmethod
    def getLavoratoreByFields(field_value_list=None):
        condition = ""
        if field_value_list:
            for key, value in dict(field_value_list).items():
                condition += key + " = \'" + str(value) + "\' AND "
        condition += " assunto = 1"
        connection = MyDB.db.connection
        try:
            c = connection.cursor()
            result = c.execute("SELECT * FROM lavoratore WHERE {} ".format(condition))
        except sqlite3.Error:
            return []
        list = []
        for row in result:
            list.append(Dipendente(row[0], row[2], row[3], row[4]))
        return list

    # metodo per la generazione di una nuova password di default da destinare ad un nuovo dipendente da salvare
    # all'interno del database;
    # la password generata è il "ruolo" del nuovo account (es. admin), nel database viene salvato il suo hash
    def generaNuovaPasswd(self):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha512', self.ruolo.encode('utf-8'), salt, 100000)
        self.password = (salt + key).hex()