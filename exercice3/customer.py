
from person import Person
from product import Product
"""import des 2 fichiers.py et de leur methode"""

class Customer(Person):
    article = {}
    def __init__(self, nom, prenom, age, article_price):
        Person.__init__(self,nom, prenom, age)
        self.article = article_price

    @property
    def article(self):
        return self.__article


    @article.setter
    def article(self,article_price):
        if article in Product.article_price.keys():
            self.___article = article_price
        else:
            raise ValueError("l article ne figure pas ")

    @property
    def article_price(self):
        return self.__article_price

    @article_price.setter
    def article_price(self, article_price):
        if article_price in Product.article_price.values():
            self.__article_price = article_price
        else:
            raise ValueError
