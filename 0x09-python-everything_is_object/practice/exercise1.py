#!/usr/bin/python3
"""
Exercice 1
"""


mylist = ['spam!', 'one', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
for i in mylist:
    print(len(i))

# Pour len(1) on obtient une erreur objet de type int n'a pas de len()
