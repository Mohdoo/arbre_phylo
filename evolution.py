############################################
### Simulation d'un arbre phylogénétique ###
###     Fonctions d’I/O sur l’arbre      ###
###     Ce code est sous licence CC0     ###
############################################

### imports nécessaires ###

import random
from config import *



### fonctions de lecture dans l’arbre ###

# renvoie True si l'arbre ne possède aucun descendant
# principe : on regarde si un descendant existe
def feuille(arbre):
    return not (arbre["gauche"] or arbre["droite"])


# vérifie si toutes les feuilles d'un arbre sont mortes : renvoie True si c'est le cas
# principe : l'arbre est vivant si au moins une de ses feuilles est vivante
def est_mort(arbre):
    mort = True

    if arbre["gauche"] != None:
        mort = est_mort(arbre["gauche"])
    
    if arbre["droite"] != None and mort:
        mort = est_mort(arbre["droite"])

    if feuille(arbre):
        mort = not arbre["vivant"]

    return mort



### fonctions d’évolution et de modification ###

# prend un arbre et applique une génération sur chacune de ses feuilles
# principe : pour chaque feuille de l'arbre, la fait vivre (aucun effet), mourir (elle ne peut plus muter), ou muter (voir la fonction evolution)
def cycle(arbre):
    if arbre["gauche"] != None:
        cycle(arbre["gauche"])

    if arbre["droite"] != None:
        cycle(arbre["droite"])

    if feuille(arbre) and arbre["vivant"]:

        choix = random.random()

        if choix < POSSIBLES["mourir"]:
            arbre["vivant"] = False
        elif choix < POSSIBLES["vivre"]:
            pass
        else:
            evolution(arbre)
        # le choix "vivre" n'a pas d'effet


# fait évoluer une feuille
# principe : donne deux fils à l'organisme, l'un est identique au père (il continue sa lignée), l'autre a muté
def evolution(arbre):
    # vérification que l'arbre est bien une feuille
    if feuille(arbre):
        arbre_continuite = LUCA.copy()
        arbre_continuite["genes"] = arbre["genes"]
        # descendant mutant
        arbre["gauche"] = arbre_continuite.copy()
        mutation(arbre["gauche"])
        # descendant qui ne mute pas
        arbre["droite"] = arbre_continuite.copy()


# applique une mutation à une feuille
# principe : on prend une lettre au hasard du génome courant, et on la transforme en un autre nucléotide possible
def mutation(arbre):
    # choix du gène qui va muter
    mutant_index = random.choice(range(TAILLE_GENOME))

    # choix du nucléotide muté (+ sécurité pour assurer que la mutation ait un effet)
    courant = arbre["genes"][mutant_index]
    mutant = courant
    while courant == mutant:
        mutant = random.choice(NUCLEOTIDES)

    # application de la mutation
    arbre["genes"] = arbre["genes"][0:mutant_index] + mutant + arbre["genes"][mutant_index + 1: TAILLE_GENOME]