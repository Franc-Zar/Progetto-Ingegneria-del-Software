from unittest import TestCase

from database.MyDB import db
from visita.controller.ControllerVisita import ControllerVisita


class TestControllerVisita(TestCase):

    # inserimento valori di test (mostra --> prenotazione --> visita)
    def setUp(self):
        sql1 = " INSERT OR REPLACE INTO mostra VALUES(-1, 'test1', 1, 'Sala A', '2021-07-11', '2022-12-29', 5.0)," \
               "(-2, 'test2', 1, 'Sala B', '2021-12-13', '2022-12-13', 11.0) "

        sql2 = " INSERT OR REPLACE INTO prenotazione VALUES(NULL, '2022-06-11', '2022-06-14', 'test1', '123213245612121', -1, 1)," \
               "(NULL, '2022-12-07', '2022-12-22', 'test2', '124118205632312', -2, 1)," \
               "(NULL, '2022-06-13', '2022-06-14', 'test3', '1222512456334243134', -1, 1)," \
               "(NULL, '2022-09-04', '2022-09-10', 'test4', '1290130456332313243133', -2, 1) "

        sql3 = "INSERT OR REPLACE INTO visita VALUES(NULL, '2022-06-13', '9:00', 'ridotto', -1)," \
               "(NULL, '2022-12-09', '9:30', 'intero', -2)," \
               "(NULL, '2022-09-08', '10:00', 'gratuito', -3) "
        db.connection.execute(sql1)
        db.connection.execute(sql2)
        db.connection.execute(sql3)
        self.controllerVisita = ControllerVisita()

    # eliminazione valori di test
    def tearDown(self):
        db.connection.cursor().execute("DELETE FROM visita WHERE data = '2022-12-09'")
        for i in range(-5,0):
            sql1 = "DELETE FROM visita WHERE codice_prenotazione = " + str(i)
            db.connection.cursor().execute(sql1)
            db.connection.commit()
        for i in range(1,8):
            sql2 = "DELETE FROM prenotazione WHERE nominativo = 'test" + str(i) + "' "
            db.connection.cursor().execute(sql2)
            db.connection.commit()
        for i in range(1,3):
            sql3 = "DELETE FROM mostra WHERE titolo = 'test" + str(i) + "' "
            db.connection.cursor().execute(sql3)
            db.connection.commit()


    def test_converti_prenotazione(self):
        # inserimento visita nuova
        self.assertIsNone(self.controllerVisita.setPrenotazione('2022-12-22', 'test5','124118121421632312', -2))

        # inserimento visita già presente
        self.assertRaises(Exception,lambda: self.controllerVisita.setPrenotazione('2022-12-22', 'test5','124118121421632312', -2))


    def test_save_visita(self):
        # salvataggio nuova visita
        self.assertIsNone(self.controllerVisita.saveVisita('2022-12-09', '9:30', 'intero', 'test5', 153616418468261, -2))

        # salvataggio visita già presente
        self.assertRaises(Exception, lambda: self.controllerVisita.saveVisita('2022-12-09', '9:30', 'intero', 'test5', 153616418468261, -2))