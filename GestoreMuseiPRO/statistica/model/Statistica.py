from database.MyDB import *
import sqlite3


class Statistica:
    def __init__(self):
        super(Statistica, self).__init__()

    # Query che restituisce, dato il giorno, il numero di visite per orario
    @staticmethod
    def visiteOrarieGiornaliere(giorno):
        sql = "SELECT COUNT(*), ora_ingresso FROM visita " \
              "WHERE data = '{}' group by ora_ingresso order by ora_ingresso".format(giorno)
        try:
            result = db.connection.cursor().execute(sql).fetchall()
            return result
        except sqlite3.Error as e:
            raise Exception(e.args)


    # Query che restituisce, dato il mese, il numero di visite per orario dei giorni del mese
    @staticmethod
    def visiteOrarieMensili(mese):  # inserire mese come '01, ..09, 10 .. 12' e non '1, 2, 3, 4, 5 ...'
        # QUERY MENSILE
        sql = "SELECT COUNT(*), ora_ingresso FROM visita " \
              "WHERE substr(data,1,4)||substr(data,6,2) = substr(\'{0}\',1,4)||substr(\'{1}\',6,2)  group by ora_ingresso order by ora_ingresso".format(
            mese, mese)
        try:
            result = db.connection.cursor().execute(sql).fetchall()
            return result
        except sqlite3.Error as e:
            raise Exception(e.args)


    # metodo  che restituisce n.prenotazioni in un giorno e n.visite effettive in quel giorno (raggruppate in base alle mostre attive)
    @staticmethod
    def presenzeEffettiveGiornaliere(giorno):
        sql2 = "SELECT COUNT(*), ID_mostra FROM prenotazione " \
               "WHERE data_visita= '{}' AND validita = 1 GROUP BY ID_mostra".format(giorno)

        sql = "SELECT COUNT(*), ID_mostra FROM prenotazione " \
              "WHERE data_visita= '{}' group by ID_mostra".format(giorno)
        try:
            prenotazioni = db.connection.cursor().execute(sql).fetchall()
            visite_effettive = MyDB().connection.cursor().execute(sql2).fetchall()
            return prenotazioni, visite_effettive
        except sqlite3.Error as e:
            raise Exception(e.args)

    # metodo  che restituisce n.prenotazioni in un mese e n.visite effettive in quel mese (raggruppate in base alle mostre attive)
    @staticmethod
    def presenzeEffettiveMensili(mese):
        sql2 = "SELECT COUNT(*), ID_mostra FROM prenotazione " \
               "WHERE    substr(data_visita,1,4)||substr(data_visita,6,2)= substr(\'{0}\',1,4)||substr(\'{1}\',6,2) AND validita = 1 GROUP BY ID_mostra".format(
            mese, mese)

        sql = "SELECT COUNT(*), ID_mostra FROM prenotazione " \
              "WHERE   substr(data_visita,1,4)||substr(data_visita,6,2)= substr(\'{0}\',1,4)||substr(\'{1}\',6,2) group by ID_mostra".format(
            mese, mese)
        try:
            prenotazioni = db.connection.cursor().execute(sql).fetchall()
            visite_effettive = db.connection.cursor().execute(sql2).fetchall()
            return prenotazioni, visite_effettive
        except sqlite3.Error as e:
            raise Exception(e.args)
