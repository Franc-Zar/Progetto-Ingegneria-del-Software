import sqlite3
from datetime import datetime
from unittest import TestCase

from database.MyDB import db
from mostra.controller.ControllerMostra import ControllerMostra


class TestControllerMostra(TestCase):

    # inserimento valori di test
    def setUp(self):
        sql = "INSERT INTO mostra VALUES(NULL, 'test1', 1, 'Sala A', '2021-07-11', '2022-01-13', 5.0)," \
              "(NULL, 'test2', 1, 'Sala B', '2021-12-13', '2022-12-13', 11.0)" \
              ",(NULL, 'test3', 2, 'Sala A', '2021-07-11', '2021-11-13', 8.0)," \
              "(NULL, 'test4', 1, 'Sala C', '2021-09-14', '2021-09-16', 15.0)," \
              "(NULL, 'test5', 3, 'Sala A', '2022-04-25', '2022-08-21', 3.0)"
        db.connection.execute(sql)
        self.controllerMostra = ControllerMostra()

    # eliminazione valori di test
    def tearDown(self):
        for i in range(1,8):
            sql = "DELETE FROM mostra WHERE titolo = 'test" + str(i) + "' "
            db.connection.cursor().execute(sql)
            db.connection.commit()

    def assertMostraInCorso(self,mostreInCorso):
        for mostra in mostreInCorso:
            if datetime.strptime(mostra.getDataFine(), '%Y-%m-%d') < datetime.today():
                self.fail()

    def assertFiltraggioCorretto(self,titolo=None,edizioneMin=None,edizioneMax=None,sala=None,
                                 dataInizioMin=None,dataInizioMax=None,dataFineMin=None,
                                 dataFineMax=None,prezzo=None):
        for mostra in self.controllerMostra.getListaMostre():
            if titolo:
                if mostra.getTitolo() != titolo:
                    self.fail()
            if edizioneMin:
                if mostra.getEdizione() < edizioneMin:
                    self.fail()
            if edizioneMax:
                if mostra.getEdizione() > edizioneMax:
                    self.fail()
            if sala:
                if mostra.getSala() != sala:
                    self.fail()
            if dataInizioMin:
                if datetime.strptime(mostra.getDataInizio(), '%Y-%m-%d') < datetime.strptime(dataInizioMin, '%Y-%m-%d'):
                    self.fail()
            if dataInizioMax:
                if datetime.strptime(mostra.getDataInizio(),'%Y-%m-%d') > datetime.strptime(dataInizioMax,'%Y-%m-%d'):
                    self.fail()
            if dataFineMin:
                if datetime.strptime(mostra.getDataFine(), '%Y-%m-%d') < datetime.strptime(dataFineMin, '%Y-%m-%d'):
                    self.fail()
            if dataFineMax:
                if datetime.strptime(mostra.getDataFine(), '%Y-%m-%d') > datetime.strptime(dataFineMax, '%Y-%m-%d'):
                    self.fail()
            if prezzo:
                if mostra.getPrezzo() != prezzo:
                    self.fail()


    def test_save_mostra(self):
        # inserimento corretto di una nuova mostra nel database
        self.controllerMostra.setModel("test6",1,"Sala C","2021-11-12","2021-11-13",10.0)
        self.assertIsNone(self.controllerMostra.saveMostra())

        # inserimento di una mostra presente nel database
        self.controllerMostra.setModel("test6", 1, "Sala C", "2021-11-12", "2021-11-13", 10.0)
        self.assertRaises(Exception, lambda: self.controllerMostra.saveMostra())


    def test_modifica_dato_mostra(self):
        # modifica prezzo di una mostra non presente nel database
        self.controllerMostra.setModel("test6", 1, "Sala C", "2021-11-12", "2021-11-13", 10.0)
        self.assertRaises(Exception, lambda: self.controllerMostra.modificaDatoMostra("prezzo", 15))

        # modifica prezzo di una mostra presente nel database
        self.controllerMostra.setModel('test2', 1, 'Sala B', '2021-12-13', '2022-12-13', 11.0)
        self.assertIsNone(self.controllerMostra.modificaDatoMostra("prezzo", 15))

        # modifica titolo di una mostra presente nel database
        self.controllerMostra.setModel('test2', 1, 'Sala B', '2021-12-13', '2022-12-13', 11.0)
        self.assertIsNone(self.controllerMostra.modificaDatoMostra("titolo", "test7"))


    def test_setListaMostre(self):
        # filtraggio per titolo
        self.controllerMostra.setListaMostre({'titolo':"test1"})
        self.assertFiltraggioCorretto("test1")
        self.controllerMostra.emptyListaMostre()

        # filtraggio per edizione
        self.controllerMostra.setListaMostre({'edizione': (1,3)})
        self.assertFiltraggioCorretto(None,1,3)
        self.controllerMostra.emptyListaMostre()

        # filtraggio per sala
        self.controllerMostra.setListaMostre({'sala': "Sala A"})
        self.assertFiltraggioCorretto(None,None,None,"Sala A")
        self.controllerMostra.emptyListaMostre()

        # filtraggio per range data inizio
        self.controllerMostra.setListaMostre({'data_inizio': ("2022-01-01","2022-12-31")})
        self.assertFiltraggioCorretto(None,None,None,None,"2022-01-01","2021-12-31")
        self.controllerMostra.emptyListaMostre()

        # filtraggio per range data fine
        self.controllerMostra.setListaMostre({'data_fine': ("2022-01-01", "2022-12-31")})
        self.assertFiltraggioCorretto(None, None, None, None, None, None, "2022-01-01", "2022-12-31")
        self.controllerMostra.emptyListaMostre()


    def test_mostreInCcorso(self):
        self.setUp()

        self.assertMostraInCorso(self.controllerMostra.mostreInCorso())

        self.tearDown()

    def test_eliminaMostra(self):

        # eliminazione mostra esistente
        self.controllerMostra.setModel('test1', 1, 'Sala A', '2021-07-11', '2022-01-13', 5.0)
        self.assertTrue(self.controllerMostra.getModel().checkMostraExists())
        self.assertIsNone(self.controllerMostra.eliminaMostra(self.controllerMostra.getModel().getID()))

        # eliminazione mostra non più esistente
        self.controllerMostra.setModel('test1', 1, 'Sala A', '2021-07-11', '2022-01-13', 5.0)
        self.assertFalse(self.controllerMostra.getModel().checkMostraExists())
        self.assertRaises(sqlite3.OperationalError,lambda: self.controllerMostra.eliminaMostra(self.controllerMostra.getModel().getID()))


    def test_modificaMostra(self):
        # modifica mostra non esistente
        self.controllerMostra.setModel('nome_sbagliato', 1, 'Sala A', '2021-07-11', '2022-01-13', 5.0)
        self.assertFalse(self.controllerMostra.getModel().checkMostraExists())
        self.assertRaises(Exception, lambda: self.controllerMostra.modificaMostra(self.controllerMostra.getModel().getID(),{'titolo':'nuovo titolo'}))

        # modifica mostra esistente
        self.controllerMostra.setModel('test2', 1, 'Sala B', '2021-12-13', '2022-12-13', 11.0)
        self.assertTrue(self.controllerMostra.getModel().checkMostraExists())
        self.assertIsNone(self.controllerMostra.modificaMostra(self.controllerMostra.getModel().getID(),{'sala':'Sala C','prezzo': 10}))