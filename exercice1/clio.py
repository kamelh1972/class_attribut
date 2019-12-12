"""exercice1 classe attribut"""
class Clio():
    price_range = [8000, 30000]
    price = 20000
    doors = (3, 5)
    colors = {
        "black" : 1234258,
        "blue" : 14255,
        "green" : 143582,
        "red" : 134625852,
        "white" : 125452
        }
    def __init__(self, number_doors, color, color_number):
        self.number_doors = number_doors
        self.color = color
        self.color_number = color_number

    """methode decorateur qui appel la methode getter"""
    @property
    def number_doors(self):
        return self.__number_doors
    """ @=decorateur methode qui fait appel a la methode setter"""
    @number_doors.setter
    def number_doors(self, number_doors) :
        if number_doors in Clio.doors :
            self.__number_doors = number_doors
        else :
            raise ValueError("la clio n'existe qu'en 5 ou 3 portes")
    """ methode qui leve une exception si le getter n est pas bon"""
    @property
    def color_number(self):
        return self.__color_number
    @color_number.setter
    def color_number(self, color_number) :
        if color_number in Clio.colors.value() :
            self.__color_number = color_number
        else :
            raise ValueError("la couleur n'existe pas")

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color) :
        if color in Clio.colors.keys() :
            self.__color = color
        else :
            raise ValueError("la couleurs n'existe pas")
    @classmethod
    def checkprice(cls):
        if cls.price in range (8000, 30000):
            return cls.price
        else :
            raise ValueError("le prix de la clio doit se situer entre 8000 et 30000")
