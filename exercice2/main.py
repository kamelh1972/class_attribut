from voiture import Voiture
from bus import Bus

#if __name__ == '__main__':

bus1 = Bus("AA-000-ZZ", "yellow", 1)
print(bus1.immatriculation)
print(bus1.couleur)

voiture1 = Voiture("BG-564-NB", "white", 5)
print("l'immatriculation de la voiture {} est {}".format(voiture1.couleur, voiture1.immatriculation))
