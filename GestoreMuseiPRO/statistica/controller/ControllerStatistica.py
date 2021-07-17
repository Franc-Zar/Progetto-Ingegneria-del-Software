from statistica.model.Statistica import *


class ControllerStatistica():
    def __init__(self):
        super(ControllerStatistica, self).__init__()
        self.model = Statistica()

    def visiteOrarieGiornaliere(self, giorno):
        try:
            return self.model.visiteOrarieGiornaliere(giorno)
        except Exception:
            raise

    def visiteOrarieMensili(self, mese):
        try:
            return self.model.visiteOrarieMensili(mese)
        except Exception:
            raise

    '''
    def stats_disdetta_mensile(self, mese):
        return self.model.stats_disdetta_mensile(mese)
    '''

    def presenzeEffettiveGiornaliere(self, giorno):
        try:
            return self.model.presenzeEffettiveGiornaliere(giorno)
        except Exception:
            raise

    def presenzeEffettiveMensili(self, mese): 
        try:
            return self.model.presenzeEffettiveMensili(mese)
        except Exception:
            raise
