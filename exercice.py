#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi

# TODO: Définissez vos fonction ici

def vol_mass(a = 2, b = 4, c = 2, p = 10 ):
    volume = (4/3) * pi * a * b * c
    masse = p * volume

    return volume, masse

#TODO: À partir d’une phrase donnée par l’utilisateur, écrire un programme qui affiche toutes les lettres
# qui sont utilisées plus de 5 fois dans la phrase, en ordre décroissant d’utilisation (le plus fréquent en premier).


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(vol_mass())
