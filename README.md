# Arbre phylogénétique 🌳 #

Base de simulation d’un arbre phylogénétique simple.
Part d’un organisme ayant un code génétique de base ([LUCA](https://fr.wikipedia.org/wiki/LUCA)), et le fait vivre, muter ou mourir.

## Lancement 🧫 ##

Exécutez `main.py`.

## Paramétrage 🧬 ##

Modifiez les constantes `GENERATIONS`, `ADN` et `NUCLEOTIDES` dans `config.py`.

## Complexité & coût 🔬 ##

Dépend de la valeur du paramètre `GENERATIONS`. Au minimum, est égale à `1` (l’organisme primordial meurt). Au maximum, est égale à `2^GENERATIONS` (tous les organismes mutent à chaque génération). Attention, généralement 20 générations produisent environ 600 organismes. Le programme peut devenir très lent au-delà.

## Idées d’améliorations 🧪 ##

 - Permettre de visualier l’arbre entier et les branches, plutôt que de seulement voir les organismes des feuilles. En théorie l’arbre devrait ressembler à un vrai arbre phylogénétique.
- Rendre les probabilités des évènements « vivre », « mourir » et « muter » plus faciles à modifier.
- Faire une fenêtre graphique qui montre l’arbre et permet de changer les paramètres sans modifier le code ou un fichier de configuration.
- Simuler un comportement pour chaque organisme selon son code génétique.

## Contribuer 🧩 ##

Ce programme est en CC0 (« Domaine Public »). Faites-en ce que vous voulez.

## 🇺🇸 English Version 🇬🇧 ##

This is a short program designed to simulate organisms and their mutations, with the goal of creating a small phylogenetic tree. It doesn’t simulate life, only rando mutations.
The code (variables and comments) is written in French, but with an automatic translation device you should be able to fully understand.
This program only simulates the organisms, it doesn’t show the full tree because that would be long to implement. All the code is in CC0 (“Public Domain”) so feel free to use it, translate it, do whatever you want!

Also, English can be 🇦🇺 and 🇳🇿 too.
