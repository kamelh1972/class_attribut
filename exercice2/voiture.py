"""exercice2  heritage"""
from vehicule import Vehicule

class Voiture(Vehicule):
    doors = (3, 5)
    def __init__(self, immatriculation, couleur, number_doors):
        Vehicule.__init__(self, immatriculation, couleur)
        self.number_doors = number_doors



    @property
    def number_doors(self):
        return self.__number_doors


    @number_doors.setter
    def number_doors(self,number_doors):
        if number_doors in Voiture.doors:
            self.__number_doors = number_doors
        else:
            raise ValueError("le nombre de porte n'existe pas")
