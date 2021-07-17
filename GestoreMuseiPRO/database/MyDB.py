import sqlite3
import  os.path

# classe per il collegamento del database alle funzionalità del programma
class MyDB(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_LOCATION = os.path.join(BASE_DIR, "data.db")
    def __init__(self, db_location=None):
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.DB_LOCATION)
        self.cur = self.connection.cursor()

        #serve per attivare la funzionalità  ON UPDATE CASCADE ON DELETE NO ACTION
        self.connection.execute("PRAGMA foreign_keys = ON")


# connessione
db = MyDB()