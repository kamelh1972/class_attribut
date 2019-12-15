class Product():
    article_price = {"dentifrice":2.00, "pate":1.00, "sauce":0.80, "chocolat":1.90}
    def __init__(self, article, price):
        self.article = article
        self.price = price

    def __add__(self, other):

        total_article = self.article + other.article
        total_price = self.price + other.price
        return Product(total_article, total_price)


    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return "article: %i, price: %i" % (self.article, self.price)
