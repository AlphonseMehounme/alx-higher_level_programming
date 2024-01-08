#!/usr/bin/python3
"""
   Module Personne
"""
class Personne:
    """
        Class Personne
    """
    __nombre_per = 0

    def __init__(self, nom="", prenom):
        """
            Function init
        """
        self.nom = nom
        self.prenom = prenom
        Personne.nombre_per += 1

    def hello(self, pays="Benin"):
        print("Hello ", self.prenom)
        print("You are in ", pays)

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom


print(Personne.nombre_per)
p = Personne("Al", "mhm")
print(p.nom())
p.nom("ALX")
print(p.nom())
print(Personne.nombre_per)
