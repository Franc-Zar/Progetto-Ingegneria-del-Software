import sqlite3
from unittest import TestCase

from Dipendenti.ControllerDipendenti.ControllerDipendente import ControllerDipendente
from database.MyDB import db


class TestControllerDipendente(TestCase):

    # inserimento valori di test
    def setUp(self):
        sql = "INSERT OR REPLACE INTO lavoratore VALUES('test1','af4500a0be019f949d93','test1test1test1t', 'test1 test1', 'catalogatore', 1)," \
              "('test2', 'af46282fa4789738', 'test2test2test2t', 'test2 test2' ,'front_office',1)," \
              "('test3', 'b563gdwf5463a639', 'test3test3test3t', 'test3 test3' ,'admin',1)," \
              "('test4', 'b563gdwf5463a639', 'test4test4test4t', 'test4 test4' ,'admin',1)"
        db.connection.execute(sql)
        self.gestioneDipendenti = ControllerDipendente()

    # eliminazione valori di test
    def tearDown(self):
        for i in range(1,6):
            sql = "DELETE FROM lavoratore WHERE username = 'test" + str(i) + "' "
            db.connection.cursor().execute(sql)
            db.connection.commit()


    # metodo per la verifica della correttezza dei criteri di filtraggio: verifica che i dipendenti siano effettivamente
    # filtrati secondo i criteri precedentemente stabiliti
    def assertFiltraggioCorretto(self,username=None,cf=None,nominativo=None,ruolo=None):
        for dipendente in self.gestioneDipendenti.getListaDipendenti():
            if username:
                if dipendente.getUsername() != username:
                    self.fail()
            if cf:
                if dipendente.getCf() != cf:
                    self.fail()
            if nominativo:
                if dipendente.getNominativo() != nominativo:
                    self.fail()
            if ruolo:
                if dipendente.getRuolo() != ruolo:
                    self.fail()


    def test_set_lista_dipendenti(self):
        self.setUp()

        # Ricerca filtrata per username presente nel database
        self.gestioneDipendenti.setListaDipendenti('test1')
        self.assertFiltraggioCorretto('test1')
        self.gestioneDipendenti.emptyListaDipendenti()

        # Ricerca filtrata per nominativo presente nel database
        self.gestioneDipendenti.setListaDipendenti(None,None,'test3 test3')
        self.assertFiltraggioCorretto(None,None,'test3 test3')
        self.gestioneDipendenti.emptyListaDipendenti()

        # Ricerca filtrata per codice fiscale presente nel database
        self.gestioneDipendenti.setListaDipendenti(None,'test2test2test2t',None,None)
        self.assertFiltraggioCorretto(None,'test2test2test2t')
        self.gestioneDipendenti.emptyListaDipendenti()

        # Ricerca filtrata per ruolo definito nel database
        self.gestioneDipendenti.setListaDipendenti(None, 'admin')
        self.assertFiltraggioCorretto(None,None,None,'admin')
        self.gestioneDipendenti.emptyListaDipendenti()

        # Ricerca filtrata per ruolo non definito nella gerarchia dei permessi del programma
        self.gestioneDipendenti.setListaDipendenti(None,None,None,'amministratore')
        self.assertFalse(self.assertFiltraggioCorretto(None,None,None,'amministratore'))
        self.gestioneDipendenti.emptyListaDipendenti()

        self.tearDown()

    def test_aggiungi_dipendente(self):
        self.setUp()

        # inserimento nel database di un nuovo dipendente
        self.assertTrue(self.gestioneDipendenti.aggiungiDipendente('test5','cfcfcfcfcfcfcfcf','nome cognome','admin'))

        # inserimento nel database di un dipendente già presente
        self.assertRaises(sqlite3.Error, lambda: self.gestioneDipendenti.aggiungiDipendente('test5','cfcfcfcfcfcfcfcf','nome cognome','admin'))

        self.tearDown()



    def test_modifica_dipendente(self):
        self.setUp()

        # inserimento nel model del controller del dipendente sul quale eseguire le operazioni di modifica dati
        self.assertTrue(self.gestioneDipendenti.inserisciDipendente('test2', 'test2test2test2t', 'test2 test2', 'front_office', False))

        # modifica ruolo dell'utente 'test2' non consentita in quanto 'amministratore' non è un ruolo presente nella gerarchia del
        # programma --> il ruolo risulta invariato
        self.assertFalse(self.gestioneDipendenti.modificaDipendente(None,None,'amministratore'))

        # modifica codice fiscale dell'utente 'test2' non consentita in quanto la lunghezza non è di 16 caratteri --> il codice risulta invariato
        self.assertFalse(self.gestioneDipendenti.modificaDipendente(None,'nuovo_cf'))

        # modifica nominativo dell'utente 'test2' consentita
        self.assertTrue(self.gestioneDipendenti.modificaDipendente(None,None,None,'nuovo_nome'))

        # modifica ruolo dell'utente 'test2' consentita
        self.assertTrue(self.gestioneDipendenti.modificaDipendente(None,None,'admin'))

        self.tearDown()


    def test_del_lavoratore_by_username(self):
        self.setUp()

        # inserimento nel model del controller del dipendente da eliminare dal database
        self.gestioneDipendenti.inserisciDipendente('test2', 'test2test2test2t', 'test2 test2', 'front_office', False)

        # eliminazione dipendente precedentemente inserito
        self.assertTrue(self.gestioneDipendenti.deleteLavoratoreByUsername())

        self.tearDown()