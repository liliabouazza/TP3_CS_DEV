"""
Fichier du jeu du pendu
Date : 02/10/2023
Editeur : Lilia Bouazza - Cyril Recordon
Todo :
"""

from random import random

fichier = open('mots.txt';'r')

meilleur_score = 0

def Choisir_mot():
    mot = random.choice(fichier)
    return mot

print(Choisir_mot())