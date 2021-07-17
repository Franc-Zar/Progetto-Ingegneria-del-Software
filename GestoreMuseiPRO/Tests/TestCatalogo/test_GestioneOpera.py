import sqlite3
from unittest import TestCase
from datetime import datetime
from database.MyDB import db
from opera.ControllerOpera.GestioneCatalogo import GestioneCatalogo


class TestGestioneOpera(TestCase):

    # inserimento valori test
    def setUp(self):
        sql = "INSERT OR REPLACE INTO opera VALUES(NULL,'test1',250000,'autore1', '200x400', 'Quadro', 2003,'-','2017-05-03',1)," \
              "(NULL,'test2',540000,'autore2', '200x400', 'Dipinto', 1980,'-','2014-11-06',1)," \
              "(NULL,'test3',310000,'autore3', '200x400', 'Quadro', 1990,'-','2018-05-14',1)," \
              "(NULL,'test4',1750000,'autore4', '200x400', 'Quadro', 1976,'-','2020-02-23',1)"
        db.connection.execute(sql)
        self.gestioneCatalogo = GestioneCatalogo()

    # eliminazione valori di test
    def tearDown(self):
         for i in range(1, 6):
            sql = "DELETE FROM opera WHERE artista = 'autore" + str(i) + "' "
            db.connection.cursor().execute(sql)
            db.connection.commit()

    # metodo per la verifica della correttezza dei criteri di filtraggio: verifica che le opere siano effettivamente
    # filtrate secondo i criteri precedentemente stabiliti
    def assertFiltraggioCorretto(self, titolo=None, valoreMin=None, valoreMax=None, autore=None,
                                 dimensioni=None, tipologia=None, annoProduzioneMin=None,
                                 annoProduzioneMax=None, immagine=None,dataAcquisizioneMin=None,
                                 dataAcquisizioneMax=None):
        for opera in self.gestioneCatalogo.getListaOpere():
            if titolo:
                if opera.getTitolo() != titolo:
                    self.fail()
            if valoreMin:
                if opera.getValore() < valoreMin:
                    self.fail()
            if valoreMax:
                if opera.getValore() > valoreMax:
                    self.fail()
            if autore:
                if opera.getAutore() != autore:
                    self.fail()
            if dimensioni:
                if opera.getDimensioni() != dimensioni:
                    self.fail()
            if annoProduzioneMin:
                if opera.getAnnoProduzione() > annoProduzioneMin:
                    self.fail()
            if annoProduzioneMax:
                if opera.getAnnoProduzione() < annoProduzioneMax:
                    self.fail()
            if immagine:
                if opera.getImg() != immagine:
                    self.fail()
            if tipologia:
                if opera.getTipologia() != tipologia:
                    self.fail()
            if dataAcquisizioneMin:
                if datetime.strptime(opera.getDataAcquisizione(),'%Y-%m-%d') < datetime.strptime(dataAcquisizioneMin,'%Y-%m-%d'):
                    self.fail()
            if dataAcquisizioneMax:
                if datetime.strptime(opera.getDataAcquisizione(),'%Y-%m-%d') > datetime.strptime(dataAcquisizioneMax,'%Y-%m-%d'):
                    self.fail()


    def test_setListaOpere(self):
        # ricerca filtrata per titolo opera presente nel database
        self.gestioneCatalogo.setListaOpere(None,'test1')
        self.assertFiltraggioCorretto('test1')
        self.gestioneCatalogo.emptyListaOpere()

        # ricerca filtrata per titolo opera non presente nel database
        self.gestioneCatalogo.setListaOpere(None, 'titolo errato')
        self.assertFalse(self.assertFiltraggioCorretto('titolo errato'))
        self.gestioneCatalogo.emptyListaOpere()

        # ricerca filtrata per valore minimo
        self.gestioneCatalogo.setListaOpere(None,None,None,None,None,None,None,None,260000)
        self.assertFiltraggioCorretto(None,260000)
        self.gestioneCatalogo.emptyListaOpere()

        # ricerca filtrata per valore minimo e valore massimo
        self.gestioneCatalogo.setListaOpere(None, None, None, None, None, None, None, None, 260000,280000)
        self.assertFiltraggioCorretto(None, 260000,280000)
        self.gestioneCatalogo.emptyListaOpere()

        # ricerca filtrata per data acquisizione minima e data acquisizione massima
        self.gestioneCatalogo.setListaOpere(None,None,None,None,"2014-11-06","2015-11-06")
        self.assertFiltraggioCorretto(None,None,None,None,None,None,None,None,None,"2014-11-06","2015-11-06")
        self.gestioneCatalogo.emptyListaOpere()

        # ricerca filtrata per tipologia
        self.gestioneCatalogo.setListaOpere(None, None, None, 'Quadro')
        self.assertFiltraggioCorretto(None,None,None,None,None,'Quadro')
        self.gestioneCatalogo.emptyListaOpere()

        self.tearDown()

    def test_modificaOpera(self):
        self.assertTrue(self.gestioneCatalogo.inserisciOpera('test1','autore1','Quadro',
                                                             '200x400',2003,'-','2017-05-03',250000))

        # modifica valore opera consentita
        self.assertTrue(self.gestioneCatalogo.modificaOpera(None,None,None,150000))

        # modifica valore opera non consentita
        self.assertFalse(self.gestioneCatalogo.modificaOpera(None, None, None, 'valore'))

        # modifica vari attributi consentita
        self.assertTrue(self.gestioneCatalogo.modificaOpera('nuovo_titolo',12331,'Dipinto',200000,'2011-05-15'))

    def test_aggiungiOpera(self):
        # opera aggiunta poichè non presente nel catalogo
        self.assertTrue(self.gestioneCatalogo.aggiungiOpera('test5','autore5','Dipinto',
                                                            '400x350',1978,'-','2014-11-26',10000))

        # opera non aggiunta poichè già presente nel catalogo
        self.assertRaises(sqlite3.Error,lambda:self.gestioneCatalogo.aggiungiOpera('test5', 'autore5', 'Dipinto',
                                                            '400x350', 1978, '-', '2014-11-26', 10000))


        # opera non aggiunta poichè un parametro non è stato fornito (titolo)
        self.assertRaises(Exception, lambda: self.gestioneCatalogo.aggiungiOpera(None, 'autore5', 'Dipinto',
                                                                                     '400x350', 1978, '-', '2014-11-26',
                                                                                     10000))


    def test_eliminaOpera(self):
        self.assertTrue(self.gestioneCatalogo.inserisciOpera('test1', 'autore1', 'Quadro',
                                                             '200x400', 2003, '-', '2017-05-03', 250000))
        # eliminazione opera presente nel catalogo
        self.assertTrue(self.gestioneCatalogo.eliminaOpera())

        self.assertTrue(self.gestioneCatalogo.inserisciOpera('none', 'none', 'none',
                                                             'none', 2003, '-', '2017-05-03', 250000))
        # eliminazione opera non presente nel catalogo
        self.assertFalse(self.gestioneCatalogo.eliminaOpera())