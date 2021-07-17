import hashlib, os
from sqlite3 import Error

from password_strength import PasswordPolicy

from Login.ModelLogin.Login import Login
from database.MyDB import db

# classe per la gestione dell'accesso degli utenti all'interno del programma, dalla verifica delle credenziali
# alla corretta definizione dei privilegi e permessi dell'account in considerazione
class GestioneLogin:
    def __init__(self):
        self.model = Login()
        self.policy = PasswordPolicy.from_names(length=5, uppercase=1, nonletters=2)


    def getRuolo(self):
        return self.model.getRuolo()

    def isLoggedIn(self):
        return self.model.isLoggedIn()

    def getUsername(self):
        return self.model.getUser()

    def logIn(self, username, ruolo):
        self.model.logIn(username, ruolo)

    def logOut(self):
        self.model.logOut()


    # metodo per effettuare l'aggiornamento della password relativa all'account in considerazione
    def changePasswd(self, oldPasswd, newPasswd):
        conn = db.connection
        sql = " SELECT password FROM lavoratore WHERE username = \'{}\' AND assunto = 1".format(self.getUsername())
        cur = conn.execute(sql)
        result = cur.fetchone()

        if not result:
            return False
        else:
            if oldPasswd == newPasswd:
                if not self.policy.test(newPasswd):
                    salt = os.urandom(32)
                    key = hashlib.pbkdf2_hmac('sha512',
                                              newPasswd.encode('utf-8'),
                                              salt,
                                              100000)
                    try:
                        cur = conn.execute('UPDATE lavoratore SET password = \'{0}\' WHERE username = \'{1}\''.format(
                            (salt + key).hex(),
                            self.getUsername()))
                        conn.commit()
                    except Error:
                        raise Exception('Modifica password fallita')
                    return True
                else:
                    raise Exception("Oops, Password Debole")
            else:
                raise Exception("Oops, Conferma Fallita")


    # metodo per la verifica delle credenziali fornite nell'interfaccia di login e, in caso di successo,
    # per il reindirizzamento all'interfaccia "Home" corrispondente al ruolo dell'account
    def verificaCredenziali(self, password, oldPasswd = None, username = None):
        accountID = 0
        user = self.getUsername()
        if not user:
            user = username
        sql = " SELECT password,ruolo FROM lavoratore WHERE username = \'{}\' AND assunto = 1".format(user)
        cur = db.connection.execute(sql)
        result = cur.fetchone()

        if not result:
            return accountID
        else:
            passwd = result[0]
            ruolo = result[1]
            if not self.getUsername():
                NewKey = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                                 (bytes.fromhex(passwd))[:32], 100000)
            else:
                NewKey = hashlib.pbkdf2_hmac('sha512',
                                             oldPasswd.encode('utf-8'),
                                                 (bytes.fromhex(passwd))[:32], 100000)
            if NewKey == (bytes.fromhex(passwd))[32:]:
                if  ruolo == "admin":
                    accountID = 1001
                elif ruolo == "front_office":
                    accountID = 1002
                elif ruolo == "catalogatore":
                    accountID = 1003
                self.model.logIn(user, ruolo)
        return accountID