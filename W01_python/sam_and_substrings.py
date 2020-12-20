#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    """
    Solution de l'exercice en programmation dynamique.
    Le principe est d'ajouter graduellement chaque digit et de calculer
    les sommes intermédiaires de manière intelligente

    Pour mieux comprendre, décortiquons un exemple : 123
    Si on cherche à la main les substrings, on trouve 1 2 3 12 23 123
    Pas grand chose d'intéressant jusque là.

    En ajoutant les digit un par un, calculons les sommes ajoutées à chaque fois.
    1   : 1         Somme = 1
    12  : 2 12      Somme = 14
    123 : 3 23 123  Somme = 149
                    Total = 164

    On voit un pattern apparaître : la somme suivante vaut 10 fois la précédente,
    plus le digit ajoutée multiplié par sa place dans la chaîne.
    Victoire ! Il ne reste plus qu'à coder :)

    """

    MODULO = 10**9 + 7
    total = 0
    current = 0

    for index, digit in enumerate(n):
        current = current*10 + (index + 1) * int(digit)
        current %= MODULO

        total += current
        total %= MODULO

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
