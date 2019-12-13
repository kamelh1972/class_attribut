"""exercice2 heritage"""
from vehicule import Vehicule

class Bus(Vehicule):
    number_floors = (1, 2)
    def __init__(self, immatriculation, couleur, number_floors):
        Vehicule.__init__(self,immatriculation, couleur)
        self.number_floors = number_floors
