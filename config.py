############################################
### Simulation d'un arbre phylogénétique ###
###     Fichier config et constantes     ###
###     Ce code est sous licence CC0     ###
############################################

### Paramètres modifiables ###

# nombre de générations simulées
# attention, le programme est exponentiellement lourd en fonction de ce paramètre
GENERATIONS = 10

# ADN de la première génération
ADN = "AAAAAAAAAA"

# nucléotides possibles
NUCLEOTIDES = "ACGT"



### paramètres constants ou calculés, ne pas modifier ###

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