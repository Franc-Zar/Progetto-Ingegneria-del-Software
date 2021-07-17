import unittest

from Tests.TestLogin import test_GestioneLogin
from Tests.TestPrenotazioni import test_ControllerPrenotazione
from Tests.TestDipendenti import test_ControllerDipendente
from Tests.TestVisite import test_ControllerVisita
from Tests.TestMostre import test_ControllerMostra
from Tests.TestCatalogo import test_GestioneOpera

def runSuite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_GestioneLogin))
    suite.addTests(loader.loadTestsFromModule(test_GestioneOpera))
    suite.addTests(loader.loadTestsFromModule(test_ControllerMostra))
    suite.addTests(loader.loadTestsFromModule(test_ControllerVisita))
    suite.addTests(loader.loadTestsFromModule(test_ControllerPrenotazione))
    suite.addTests(loader.loadTestsFromModule(test_ControllerDipendente))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)

if __name__ == '__main__':
    runSuite()