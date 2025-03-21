#TP1 - Manipulation de fonctions de base en Python

# Etape 1 : supprime "pass" pour coder la fonction
# Etape 2 : supprime les """ pour pouvoir effectuer les tests

# EXO 1
# Objectif : Faire une multiplication de deux entiers naturels sans le signe *
def mul(x, y):
    pass

#Test
"""
print("mul 1:\n   attendu: 6\n   reçu:   " + str(mul(2, 3)))
print("mul 2:\n   attendu: 28\n   reçu:   " + str(mul(4, 7)))
"""

# EXO 2
# Objectif : Faire une division euclidienne (quotient + reste)
# de deux entiers naturels sans les signes /, // et %. y est le diviseur.
def div(x, y):
    pass

#Test 
"""
print("div 1:\n   attendu: (2, 0)\n   reçu:   " + str(div(10, 5)))
print("div 2:\n   attendu: (2, 2)\n   reçu:   " + str(div(12, 5)))
"""

# EXO 3
# Objectif : Vérifier si une liste est triée par ordre croissant
def est_triee(liste):
    pass

#Test
"""
print("est_triee 1:\n   attendu: True\n   reçu:   "+str(est_triee([1, 2, 3, 4, 5])))
print("est_triee 2:\n   attendu: False\n   reçu:   "+str(est_triee([1, 3, 2, 4, 5])))
"""

# EXO 4
# Objectif : Fusionner deux listes alternativement
def fusionner_alternativement(liste1, liste2):
    pass

#Test
"""
print("fusionner_alternativement:\n   attendu: [1, 'a', 2, 'b', 3, 'c']\n   reçu:   "+str(fusionner_alternativement([1, 2, 3], ['a', 'b', 'c'])))
"""


# EXO 5
# Objectif : Calculer la puissance d'un nombre sans utiliser l'opérateur `**`
def puissance(x, exposant):
    pass

# Test
"""
print("puissance:\n   attendu: 8\n   reçu:   " + str(puissance(2, 3)))
"""

# EXO 6
# Objectif : Vérifier si un nombre est pair ou impair
def est_pair(n):
    pass

# Test
"""
print("est_pair:\n   attendu: True\n   reçu:   " + str(est_pair(4)))
print("est_pair:\n   attendu: False\n   reçu:   " + str(est_pair(7)))
"""

# EXO 7
# Objectif : Vérifier si un nombre est un nombre premier
def est_premier(n):
    pass

# Test
"""
print("est_premier:\n   attendu: True\n   reçu:   " + str(est_premier(7)))
print("est_premier:\n   attendu: False\n   reçu:   " + str(est_premier(8)))
"""

# EXO 8
# Objectif : Trouver la somme des chiffres d'un nombre
def somme_chiffres(n):
    pass

# Test
"""
print("somme_chiffres:\n   attendu: 6\n   reçu:   " + str(somme_chiffres(123)))
"""


# EXO 9
# Objectif : Calculer la somme des n premiers entiers naturels
def somme_premiers_n(n):
    pass

# Test
"""
print("somme_premiers_n:\n   attendu: 15\n   reçu:   " + str(somme_premiers_n(5)))
"""

# EXO 10
# Objectif : Trouver le plus grand commun diviseur (PGCD) de deux nombres
def pgcd(a, b):
    pass

# Test
"""
print("pgcd:\n   attendu: 6\n   reçu:   " + str(pgcd(54, 24)))
"""
