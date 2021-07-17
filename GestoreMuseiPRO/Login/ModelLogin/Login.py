# classe per il modellamento dello stato in cui si trova l'account all'interno del programma:
# PasswordVerificata = True --> l'utente può interagire all'interno del programma (interfaccia Home)
# PasswordVerificata = False --> l'utente non ha i diritti di accedere (interfaccia Login)
class Login:
    def __init__(self):
        self.username = None
        self.passwdVerificata = False
        self.ruolo = None

    # metodo richiamato al momento del logout per azzerare le condizioni dell'account precedentemente attivo
    def logOut(self):
        self.username = None
        self.passwdVerificata = False
        self.ruolo = False

    # metodo per la verifica che l'account attuale è attivo
    def isLoggedIn(self):
        if not self.username and not self.passwdVerificata and not self.ruolo:
           return False
        return True

    # metodo per configurare lo stato dell'account come attivo
    def logIn(self, username, ruolo):
        self.username = username
        self.ruolo = ruolo
        self.passwdVerificata = True

    def getUser(self):
        return self.username

    def getRuolo(self):
        return self.ruolo