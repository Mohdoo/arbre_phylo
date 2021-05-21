############################################
### Simulation d'un arbre phylogénétique ###
###    Méthodes d’affichage de l’arbre   ###
###     Ce code est sous licence CC0     ###
############################################

### imports nécessaires ###

from config import *
from evolution import feuille



### fonctions d’affichage et d’écriture de l’arbre ###

# affiche l'arbre
# ça serait cool d’afficher tout l’arbre avec les branches
def afficher_arbre(arbre):
    print("Affichage partiel de l'arbre")
    print("Seuls les organismes sans descendants sont affichés")
    afficher_feuilles(arbre, 0)


# affiche les feuilles d'un arbre
def afficher_feuilles(arbre, profondeur):
    if arbre["gauche"] != None:
        afficher_feuilles(arbre["gauche"], profondeur + 1)
    
    if arbre["droite"] != None:
        afficher_feuilles(arbre["droite"], profondeur + 1)

    if feuille(arbre):
        print("'" + arbre["genes"] + "'", end=" ")

        if arbre["vivant"]:
            print("vivant", end=" ")
        else:
            print("mort  ", end=" ")
        
        print("(génération " + str(profondeur) + ")")