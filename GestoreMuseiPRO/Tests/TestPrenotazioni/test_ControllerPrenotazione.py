from datetime import datetime
from unittest import TestCase

from database.MyDB import db
from prenotazione.controller.ControllerPrenotazione import ControllerPrenotazione


class TestControllerPrenotazione(TestCase):

    def setUp(self):
        sql1 = " INSERT OR REPLACE INTO mostra VALUES(-1, 'test1', 1, 'Sala A', '2021-07-11', '2022-12-29', 5.0)," \
               "(-2, 'test2', 1, 'Sala B', '2021-12-13', '2022-12-13', 11.0) "

        sql2 = " INSERT OR REPLACE INTO prenotazione VALUES(NULL, '2022-06-11', '2022-06-14', 'test1', '123213245612121', -1, 1)," \
              "(NULL, '2022-12-07', '2022-12-22', 'test2', '124118205632312', -2, 1)," \
              "(NULL, '2022-06-13', '2022-06-14', 'test3', '1222512456334243134', -1, 1)," \
              "(NULL, '2022-09-04', '2022-09-10', 'test4', '1290130456332313243133', -2, 1) "
        db.connection.execute(sql1)
        db.connection.execute(sql2)
        self.controllerPrenotazione = ControllerPrenotazione()


    def tearDown(self):
        for i in range(1,8):
            sql1 = "DELETE FROM prenotazione WHERE nominativo = 'test" + str(i) + "' "
            db.connection.cursor().execute(sql1)
            db.connection.commit()
        for i in range(1,3):
            sql2 = "DELETE FROM mostra WHERE titolo = 'test" + str(i) + "' "
            db.connection.cursor().execute(sql2)
            db.connection.commit()

    def assertFiltraggioCorretto(self,listaPrenotazioni,codice=None,dataPrenotazioneMin=None,dataPrenotazioneMax=None,
                                 dataVisitaMin=None,dataVisitaMax=None,nominativo=None,telefono=None,IDMostra=None):
        for prenotazione in listaPrenotazioni:
            if codice:
                if codice != prenotazione.getCodice():
                    self.fail()
            if dataPrenotazioneMin:
                if datetime.strptime(prenotazione.getDataPrenotazione(), '%Y-%m-%d') < datetime.strptime(dataPrenotazioneMin, '%Y-%m-%d'):
                    self.fail()
            if dataPrenotazioneMax:
                if datetime.strptime(prenotazione.getDataPrenotazione(), '%Y-%m-%d') > datetime.strptime(
                                dataPrenotazioneMax, '%Y-%m-%d'):
                    self.fail()
            if dataVisitaMin:
                if datetime.strptime(prenotazione.getDataVisita(), '%Y-%m-%d') < datetime.strptime(dataVisitaMin, '%Y-%m-%d'):
                    self.fail()
            if dataVisitaMax:
                if datetime.strptime(prenotazione.getDataVisita(), '%Y-%m-%d') > datetime.strptime(dataVisitaMax, '%Y-%m-%d'):
                    self.fail()
            if nominativo:
                if nominativo != prenotazione.getNominativo():
                    self.fail()
            if telefono:
                if telefono != prenotazione.getTelefono():
                    self.fail()
            if IDMostra:
                if IDMostra != prenotazione.getIDMostra():
                    self.fail()



    def test_save_prenotazione(self):
        # inserimento di una prenotazione già esistente
        self.controllerPrenotazione.setModel(None, '2022-06-11', '2022-06-14', 'test1', '123213245612121', -1)
        self.assertRaises(Exception, lambda: self.controllerPrenotazione.savePrenotazione())

        # inserimento di una nuova prenotazione
        self.controllerPrenotazione.setModel(None, '2022-03-11', '2022-04-14', 'test5', '123213165617121', -1)
        self.assertIsNone(self.controllerPrenotazione.savePrenotazione())

    def test_del_prenotazione_by_codice(self):
        # eliminazione prenotazione presente
        self.controllerPrenotazione.setModel(None, '2022-06-11', '2022-06-14', 'test1', '123213245612121', -1)
        self.assertIsNone(self.controllerPrenotazione.deletePrenotazione())

        # eliminazione prenotazione già eliminata
        self.controllerPrenotazione.setModel(None, '2022-06-11', '2022-06-14', 'test1', '123213245612121', -1)
        self.assertRaises(Exception, lambda: self.controllerPrenotazione.deletePrenotazione())

    def test_modifica_dato_prenotazione(self):
        # modifica ID mostra della prenotazione
        self.controllerPrenotazione.setModel(None, '2022-06-11', '2022-06-14', 'test1', '123213245612121', -1)
        self.assertIsNone(self.controllerPrenotazione.modificaDatoPrenotazione('ID_mostra', -2))

        # modifica titolo per mostra non presente nel database
        self.controllerPrenotazione.setModel(None, '2022-11-11', '2022-04-14', 'test43', '161243245612121', -1)
        self.assertRaises(Exception, lambda: self.controllerPrenotazione.modificaDatoPrenotazione('titolo', 'test1111'))

        # modifica titolo per mostra non presente nel database
        self.controllerPrenotazione.setModel(None, '2022-11-11', '2022-04-14', 'test43', '161243245612121', -1)
        self.assertRaises(Exception, lambda: self.controllerPrenotazione.modificaDatoPrenotazione('titolo', 'test1111'))

    def test_get_prenotazione_by_fields(self):
        # filtraggio sul nominativo
        self.assertFiltraggioCorretto(self.controllerPrenotazione.getPrenotazioneByFields({'nominativo': 'test1'}),
                                      None, None, None, None, None,'test1', )
        # filtraggio tramite ID della mostra
        self.assertFiltraggioCorretto(self.controllerPrenotazione.getPrenotazioneByFields({'ID_mostra': -1}), None, None,
                                      None, None, None, None, None, -1)
        # filtraggio tramite range di date di prenotazione
        self.assertFiltraggioCorretto(self.controllerPrenotazione.getPrenotazioneByFields({'data_prenotazione':("2022-01-01", "2022-12-31")}),
                                      None,"2022-01-01","2022-12-31")

        # filtraggio tramite range di date di visita
        self.assertFiltraggioCorretto(
            self.controllerPrenotazione.getPrenotazioneByFields({'data_visita': ("2022-01-01", "2022-12-31")}),
            None,None,None,"2022-01-01", "2022-12-31")

    def test_upd_prenotazione_by_fields(self):
        # modifica ID mostra di prenotazione esistente
        self.controllerPrenotazione.setModel(None, '2022-06-11', '2022-06-14', 'test1', '123213245612121', -1)
        self.assertIsNone(self.controllerPrenotazione.updatePrenotazioneByFields(
            self.controllerPrenotazione.getModel().checkPrenotazioneExists(), {'ID_mostra': -2}))

        # modifica nominativo di prenotazione non esistente
        self.controllerPrenotazione.setModel(None, '2023-06-11', '2023-06-14', 'nome cognome', '12321344264233281', -1)
        self.assertRaises(Exception, lambda: self.controllerPrenotazione.updatePrenotazioneByFields(
            self.assertFalse(self.controllerPrenotazione.getModel().checkPrenotazioneExists()), {'nominativo': 'nuovo_nome'}))



