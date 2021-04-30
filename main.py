############################################
### Simulation d'un arbre phylogénétique ###
###     Ce code est sous licence CC0     ###
############################################

### imports nécessaires ###

import random



### Paramètres modifiables ###

# nombre de générations simulées
GENERATIONS = 10

# ADN de la première génération
ADN = "AAAAAAAAAA"

# nucléotides possibles
NUCLEOTIDES = "ACGT"



## paramètres constants ou calculés, ne pas modifier ###

# possibilités pour chaque feuille à chaque génération
# + probabilités pour chaque évènement
# méga flemme d'expliquer comment changer les probabilités
# en gros on classe de la moins probable à la plus probable
# et on ajoute à chaque fois la probabilité de l'élément, sachant que la somme de tout fait 1
# comme ça le choix est facile
# c'est chiant à changer du coup, mais ça facilite mon implémentation
POSSIBLES = {
    "mourir": 0.1, # proba 0.1
    "vivre": 0.5, # proba 0.4, ajouté à celle de mourir
    "muter": 1 # proba 0.5, ajoutée à celles de vivre et mourir
}

# taille du génome des organismes
TAILLE_GENOME = len(ADN)

# organisme primordial
LUCA = {
    "genes": ADN,
    "vivant": True,
    "gauche": None,
    "droite": None
}



### fonctions utilisées ###

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
