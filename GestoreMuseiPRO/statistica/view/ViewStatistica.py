from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from mostra.controller import ControllerMostra
from statistica.controller.ControllerStatistica import ControllerStatistica

#classe per la produzione di STATISTICHE GIORNALIERE/MENSILI SU ORARI DI AFFOLLAMENTO e DISDETTE
class ViewStatistica():
    def __init__(self):
        super(ViewStatistica, self).__init__()
        self.controller = ControllerStatistica()

    # metodo che resistuisce il grafico che riporta, dato un giorno, il n.visite per ogni orario
    def visiteGiornaliere(self, giorno):
        result = self.controller.visiteOrarieGiornaliere(giorno)
        fig, ax = plt.subplots(figsize=(4, 4))
        times = ['08:30', '09:30', '10:30', '11:30', '12:30', '13:30','14:30', '15:30', '16:30', '17:30', '18:30']
        numbers = []
        dim = len(times) - len(result)
        while dim>0:
            numbers.append(0)
            dim = dim-1
        index = 0
        for row in result:
            while index < len(times):
                if row[1] == times[index]:
                    numbers.insert(index, row[0])
                    break
                else:
                    index += 1

        ax.bar(times, numbers, color='#4CAF50')
        plt.ylim([0, 20])
        plt.yticks(np.arange(0, 20,2), fontsize=6)

        # Set title and labels for axes
        ax.set(xlabel="Giorno: {}".format(giorno),
               ylabel="N. visitatori")
        ax.set_title("Visite giornaliere", fontsize=10)
        #plt.show()
        return fig

    # metodo che resistuisce il grafico che riporta, dato un mese, il n.visite per ogni orario
    def visiteMensili(self, mese):
        result = self.controller.visiteOrarieMensili(mese)
        fig, ax = plt.subplots(figsize=(4, 4))
        times = ['08:30', '09:30', '10:30', '11:30', '12:30', '13:30','14:30', '15:30', '16:30', '17:30', '18:30']
        numbers = []
        dim = len(times) - len(result)
        while dim>0:
            numbers.append(0)
            dim = dim-1
        index = 0
        for row in result:
            while index < len(times):
                if row[1] == times[index]:
                    numbers.insert(index, row[0])
                    break
                else:
                    index += 1

        ax.bar(times, numbers, color='#4CAF50')
        plt.ylim([0, 100])
        plt.yticks(np.arange(0, 100, 20))

        # Set title and labels for axes
        lista_mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
        ax.set(xlabel="Mese: {}".format(lista_mesi[int(mese[5:7])-1]),
               ylabel="N. visitatori",
               title="Visite mensili")
        return fig

    
    # metodo che resistuisce il grafico che riporta, per ogni mostra attiva nel giorno specificato, il n.visite su n.prenotazioni
    def disdetteGiornaliere(self, giorno):
        result = self.controller.presenzeEffettiveGiornaliere(giorno)[0]
        result2 = self.controller.presenzeEffettiveGiornaliere(giorno)[1]
        fig, ax = plt.subplots(figsize=(4, 4))
        plt.gcf().subplots_adjust(left=0.18)
        mostre_attive = ControllerMostra.Mostra.getMostreAttive(giorno) #restituisce lista di mostre attive come oggetti
        y = [] #asse y: lista mostre attive
        x_prenotazioni = [] #asse x: lista visitatori prenotati
        x_visite_effettive = []
        for el in mostre_attive:
            y.append(el.titolo)
        dim = len(mostre_attive) - len(result)
        while dim > 0:
            x_prenotazioni.append(0)
            dim = dim - 1
        index = 0
        for row in result:
            while index < len(mostre_attive):
                if row[1] == mostre_attive[index].ID:
                    x_prenotazioni.insert(index, row[0])
                    break
                else:
                    index = index + 1

        dim2 = len(mostre_attive) - len(result2)
        while dim2 > 0:
            x_visite_effettive.append(0)
            dim2 = dim2 - 1
        index = 0
        for row in result2:
            while index < len(mostre_attive):
                if row[1] == mostre_attive[index].ID:
                    x_visite_effettive.insert(index, row[0])
                    break
                else:
                    index = index + 1
        plt.xlim([0, 20])
        plt.xticks(np.arange(0, 20, 5))
        y_pos = np.arange(len(y))
        plt.barh(y_pos - 0.15, x_prenotazioni, color='#4CAF00', height=0.3, label='Prenotazioni')
        plt.barh(y_pos + 0.15, x_visite_effettive, height=0.3, label='Visite effettive')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(y, rotation='60', fontsize = 8, verticalalignment='center')

        # Set title and labels for axes
        ax.set_title("Visite effettive giornaliere", fontsize = 10)
        ax.set_xlabel("Giorno {}".format(giorno), fontsize=8)
        ax.set_ylabel("Mostre", fontsize=8)
        plt.legend(fontsize=8)
        return fig

    # metodo che resistuisce il grafico che riporta, per ogni mostra attiva nel mese specificato, il n.visite su n.prenotazioni
    def disdetteMensili(self, mese):
        prenotazioni = self.controller.presenzeEffettiveMensili(mese)[0]
        visite = self.controller.presenzeEffettiveMensili(mese)[1]
        fig , ax = plt.subplots(figsize=(5, 4))

        plt.gcf().subplots_adjust(left=0.20)
        mostre_attive = ControllerMostra.Mostra.getMostreAttiveMese(mese) #restituisce lista di mostre attive come oggetti
        y = [] #asse y: lista mostre attive
        x_prenotazioni = [] #asse x: lista visitatori prenotati
        x_visite_effettive = []
        for el in mostre_attive:
            y.append(el.titolo)
        dim = len(mostre_attive) - len(prenotazioni)
        while dim > 0:
            x_prenotazioni.append(0)
            dim = dim - 1
        index = 0
        for row in prenotazioni:
            while index < len(mostre_attive):
                if row[1] == mostre_attive[index].ID:
                    x_prenotazioni.insert(index, row[0])
                    break
                else:
                    index = index + 1

        dim2 = len(mostre_attive) - len(visite)
        while dim2 > 0:
            x_visite_effettive.append(0)
            dim2 = dim2 - 1
        index = 0
        for row in visite:
            while index < len(mostre_attive):
                if row[1] == mostre_attive[index].ID:
                    x_visite_effettive.insert(index, row[0])
                    break
                else:
                    index = index + 1

        plt.xlim([0, 200])
        plt.xticks(np.arange(0, 200, 50), fontsize = 10)
        y_pos = np.arange(len(y))
        plt.barh(y_pos - 0.15, x_prenotazioni, color = '#4CAF00', height=0.3, label = 'Prenotazioni')
        plt.barh(y_pos + 0.15, x_visite_effettive,height=0.3, label = 'Visite effettive')
        ax.set_yticks(y_pos)

        ax.set_yticklabels(y, fontsize = 8, rotation='60', verticalalignment='center')

        # Set title and labels for
        ax.set_title("Visite effettive mensili", fontsize=10)
        lista_mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre',
                      'Ottobre', 'Novembre', 'Dicembre']

        ax.set_xlabel("Mese {}".format(lista_mesi[int(datetime.strptime(mese, "%Y-%m-%d").month) - 1]), fontsize=10)
        ax.set_ylabel("Mostre", fontsize=10)

        plt.legend(fontsize=10)
        return fig
