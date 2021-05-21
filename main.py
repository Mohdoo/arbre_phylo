############################################
### Simulation d'un arbre phylogénétique ###
###     Point de départ du programme     ###
###     Ce code est sous licence CC0     ###
############################################

### imports nécessaires ###

from config import *
from evolution import *
from affichage import *



### Programme principal ###

if __name__ == "__main__":

    arbre_vivant = LUCA.copy()

    # simulation des générations
    # on simule jusqu'à la dernière génération ou jusqu'à la mort totale de l'arbre
    for i in range(GENERATIONS):
        cycle(arbre_vivant)
        if est_mort(arbre_vivant):
            break

    # affichage de l'arbre
    afficher_arbre(arbre_vivant)
