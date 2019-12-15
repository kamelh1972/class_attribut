from person import Person

class Employee(Person):
    statut = ["employe","technicien","manager","cadre"]

    def __init__(self,nom, prenom, age,nom_statut):
        Person.__init__(self,nom, prenom, age)
        self.statut = nom_statut

    @classmethod
    def checkstatut(cls):
        if cls.statut in statut():
            return cls.statut
        else:
            raise ValueError("le statut ne correspond pas")
