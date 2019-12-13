from voiture import Voiture
from bus import Bus

if __name__ == '__main__':

    bus1 = Bus("AA-000-ZZ", "yellow",4)
    print("le bus immatriculé {} , couleur {} à {} étages".format(bus1.immatriculation,bus1.couleur,bus1.number_floors))

    voiture1 = Voiture("BG-564-NB", "white", 5)
    print("l'immatriculation de la voiture {} est {}".format(voiture1.couleur, voiture1.immatriculation))

    voiture1 = Voiture("BG-564-NB", "black", 3)
    print("l'immatriculation de la voiture {} est {}".format(voiture1.couleur, voiture1.immatriculation))

#, voiture2.couleur, voiture2.number_doors)
