"""exercice2 heritage"""
from vehicule import Vehicule

class Bus(Vehicule):
    floor = (1, 2)
    def __init__(self, immatriculation, couleur, number_floors):
        Vehicule.__init__(self,immatriculation, couleur)
        self.number_floors = number_floors


    @property
    def number_floors(self):
        return self.__number_floors


    @number_floors.setter
    def number_floors(self,number_floors):
        if number_floors in Bus.floor:
            self.__number_floors = number_floors
        else:
            raise ValueError("le nombre d'etage n'existe pas")
