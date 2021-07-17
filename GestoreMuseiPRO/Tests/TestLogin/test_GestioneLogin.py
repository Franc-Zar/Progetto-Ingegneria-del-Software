from unittest import TestCase

from database.MyDB import db
from Login.ControllerLogin.GestioneLogin import GestioneLogin

class TestGestioneLogin(TestCase):
    def setUp(self):
        sql = " INSERT OR REPLACE INTO lavoratore VALUES('test','af4500a0be019f949d939b389585f95665b03e2b879e0a6a474744ac81a4bc95262647f11661ac3f1f4880c69117a56a9e3e61bc81a12e4139f039bb28ed7cad46de211dff08df6b11b0efd63abe0c8e09e12c22d039cd331a8c3270c7f52dc7'," \
              " 'testtesttesttest', 'test test', 'admin', 1) "
        db.connection.execute(sql)
        self.gestioneLogin = GestioneLogin()

    def tearDown(self):
        sql = "DELETE FROM lavoratore WHERE username = 'test'"
        db.connection.cursor().execute(sql)
        db.connection.commit()

    def test_changePasswd(self):
        # login dell'utente che vuole effettuare la modifica password
        self.assertTrue(self.gestioneLogin.verificaCredenziali(password='test',username='test'))

        # modifica password fallita (errore nella conferma della vecchia password)
        self.assertRaises(Exception, lambda: self.gestioneLogin.changePasswd('test','nuova_password'))

        # modifica password fallita (errore nella conferma della nuova password)
        self.assertRaises(Exception, lambda: self.gestioneLogin.changePasswd('test','test1'))

        # modifica password fallita (policy non rispettata --> password debole)
        self.assertRaises(Exception,lambda: self.gestioneLogin.changePasswd('test1','test1'))

        # password aggiornata con successo
        self.assertTrue(self.gestioneLogin.changePasswd('S3cur3P@ssw0rd','S3cur3P@ssw0rd'))

        self.gestioneLogin.logOut()

        # eseguo il login con la nuova password
        self.assertTrue(self.gestioneLogin.verificaCredenziali(password='S3cur3P@ssw0rd',username='test'))


    def test_verificaCredenziali(self):
        # login effettuato con password corretta --> viene restituito l'ID account relativo al ruolo 'admin'
        self.assertEqual(self.gestioneLogin.verificaCredenziali(password='test',username='test'),1001)
        self.assertTrue(self.gestioneLogin.isLoggedIn())
        self.gestioneLogin.logOut()

        # login effettuato con password errata --> viene restituito ID = 0
        self.assertFalse(self.gestioneLogin.verificaCredenziali(password='errata', username='test'))
        self.assertFalse(self.gestioneLogin.isLoggedIn())