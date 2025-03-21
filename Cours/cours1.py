# Salut bienvenue dans ce cours ! Ce cours est dédié aux débutants.
# Mais il peut intéresser tout de même des personnes plus expérimentées.
# L'objectif est de te faire découvrir les bases de Python.

# ================= COMMENT UTILISER CE FICHIER =================
# Comment te servir de ce fichier : retire les caractères """ """ et exécute le fichier.
# Voici un exemple

# Retire les """ avant ET après print("Bien joué ! On va pouvoir commencer...") et exécute le code. 
"""
print("Bien joué ! On va pouvoir commencer...")

"""

# ================= PREMIERS AFFICHAGES =================
# La fonction print() permet d'afficher des éléments dans le terminal.
# Elle nous servira tout au long des cours / TP pour afficher nos résultats

# Supprime les commentaires et exécute pour tester
"""
print("Hello World")  # Ici on affiche donc Hello World 
print()  # Ici je fais un print vide pour faire un retour à la ligne
"""


# ================= OPÉRATIONS MATHÉMATIQUES DE BASE =================
# Les calculs de base sont possibles:

# Supprime les commentaires et exécute pour tester
"""
print(6 + 2)  # Addition avec le signe +
print(6 - 2)  # Soustraction avec le signe -
print(6 * 2)  # Multiplication avec le signe *
print(6**2)   # Puissance avec le signe **
print()
"""


# ================= DIVISIONS =================
# Pour la division :
# Supprime les commentaires et exécute pour tester
"""
print(5 / 2)   # La division avec le signe /
print(5 // 2)  # La division entière avec le signe //
print(5 % 2)   # Le reste de la division entière avec le signe %
print()
"""

# ================= COMBINAISONS D'OPÉRATIONS =================
# Supprime les commentaires et exécute pour tester
"""
# On peut combiner ces calculs.
print((4 + 2) * 7)
# Ou obtenir des valeurs comme racine carrée en manipulant correctement ces opérateurs.
print(36**0.5)  # x puissance 0.5 correspond à la racine carrée de x
print()
"""

# ================= VARIABLES ET AFFECTATIONS =================
# Supprime les commentaires et exécute pour tester
"""
# Il est possible de stocker ces résultats dans des variables. On appelle ça l'affectation.
x = 6          # On affecte une valeur à x
print(x)       # On peut afficher x
x = x + 2      # Ou effectuer des calculs dessus
print(x)   
print()
"""

# ================= MODIFICATION DE VARIABLES =================
# Supprime les commentaires et exécute pour tester
"""
x = 3          # Ici on écrase l'ancienne valeur de x. x devient 3
print(x)
x = x + 3      # On peut modifier x comme cela pour ajouter 3 à x
print(x)       
x += 3         # Avec += on fait la même chose que la ligne du dessus
print(x)       # N'oublie pas d'afficher la valeur finale
print()
"""

# ================= CALCULS AVEC VARIABLES =================
# Supprime les commentaires et exécute pour tester

"""
x = -3
y = 6 * 3      # On peut affecter directement le résultat d'un calcul à une variable
print(y)       # On peut afficher y
print(y + 2)   # Ou effectuer de nouveaux calculs dessus
print(x + y)   # On peut donc additionner des variables
print()
"""

# ================= AFFICHAGE AVANCÉ =================
# Supprime les commentaires et exécute pour tester

"""
# Affichage: on a vu que la fonction print affiche des valeurs ou du texte.
print("Hello")
print(5)
# Si tu veux afficher Hello puis 5 tu peux le faire comme cela
print("Hello", 5)  # Par défaut il y aura un espace entre le Hello et le 5

# Tu peux répéter le processus autant de fois que tu souhaites
print("Hello", 5, "Hello", 5, "Hello", "...") 
print()
"""

# ================= CONCATÉNATION ET CONTRÔLE DE SORTIE =================
# Supprime les commentaires et exécute pour tester

"""
# Tu peux éviter l'espace automatique en utilisant la concaténation (+) 
# Attention, la concaténation ne peut additionner que des chaînes de caractères 
# donc il faut forcer le type avec str()
print("Hello" + str(5))
print()
"""

# ================= PERSONNALISATION DE FIN DE LIGNE =================
# Supprime les commentaires et exécute pour tester

"""
# Par défaut print fait un retour à la ligne. En réalité il rajoute le caractère 
# du retour à la ligne (\n) à la fin de l'affichage. 
# Tu peux forcer le caractère de fin pour éviter ça.

print("Hello", end="\n\n")  # Si tu veux sauter une ligne
print("Hello", end="5")     # Si tu veux 5 en fin de ligne
print(" comme il n'y a pas de \\n à la fin ce print se trouve sur la même ligne")
print()
"""

# ================= BOUCLE FOR =================
# Supprime les commentaires et exécute pour tester

"""
# For: la fonction for parcourt une liste. Ainsi i prend la première valeur de la
# liste, puis la seconde...
for i in [1, 2, 3]:
    print("Valeur:", i)
print()

for i in ["a", "b", "c"]:
    print("Lettre:", i)
print()
"""

# ================= FONCTION RANGE =================
# Supprime les commentaires et exécute pour tester

"""
# La fonction range crée une suite d'entiers
print(range(10))
print(list(range(10)))  # Si on convertit ça en liste
print()

# range(10) correspond à range(0,10) on part de 0 et on s'arrête avant 10.
# Mais tu peux partir de l'entier de ton choix jusqu'à l'entier de ton choix
print(list(range(3, 10)))
print(list(range(-3, 3)))
print()

# Tu peux aussi te déplacer de deux en deux en utilisant un pas.
print(list(range(0, 10, 2)))
# Ou de n en n
print(list(range(0, 10000, 1000)))
print()
"""

# ================= MANIPULATION DE LISTES =================
# Supprime les commentaires et exécute pour tester

"""
# Maintenant qu'on a des listes on veut pouvoir les manipuler.
l = ["a", "b", "c"]  # On stocke cette liste dans la variable l
print(l)                  # On affiche la liste complète
print()

print(l[0])  # On affiche le premier élément de la liste grâce à l'index 0
print(l[1])  # On affiche le deuxième élément de la liste grâce à l'index 1
print(l[2])  # On affiche le troisième élément de la liste grâce à l'index 2
print()
"""

# ================= PARCOURIR UNE LISTE =================
# Supprime les commentaires et exécute pour tester

"""
# Tu peux afficher la liste comme cela
l = ["a", "b", "c"]
for letter in l:
    print(letter, end=" ")  # Pour avoir un espace entre chaque lettre
print()
"""

# ================= FONCTION LEN() =================
# Supprime les commentaires et exécute pour tester

"""
l = ["a", "b", "c"]
# Sur les listes encore tu peux obtenir la taille de la liste avec len()
print(len(l))  # On obtient 4, il y a bien 4 lettres
# len marche aussi sur les chaînes de caractères et donne le nombre de lettres
print(len("Hello"))
print()
"""

# ================= BOOLÉENS ET OPÉRATIONS DE COMPARAISON =================
# Supprime les commentaires et exécute pour tester

"""
# Maintenant on va voir les booléens. En Python on a accès à True et False.
# Ces valeurs sont très utiles pour vérifier si quelque chose est vrai.
print(2 + 2 == 5)  # Le signe == vérifie si 2+2 et 5 sont identiques
print(2 + 2 == 4)
print()

print(2 + 2 != 5)  # Le signe != vérifie si 2+2 et 5 sont différents
print(2 + 2 != 4)
print()

print(4 > 5)  # Le signe > vérifie si 4 est supérieur à 5
print(5 > 4)
print()

print(6 < 5)  # Le signe < vérifie si 6 est inférieur à 5
print(5 < 6)
print()

print(5 >= 5)  # Le signe >= vérifie si 5 est supérieur ou égal à 5
print(5 >= 4)
print(6 >= 5)
print()

print(5 <= 5)  # Le signe <= vérifie si 5 est inférieur ou égal à 5
print(4 <= 5)
print(6 <= 5)
print()
"""

# ================= CONDITIONS IF, ELIF, ELSE =================
# Supprime les commentaires et exécute pour tester

"""
# Cela sert beaucoup dans les blocs conditionnels
if 2 + 2 == 5:  
    # if: si 2+2 == 5 renvoie True alors on fait print("2+2=5")
    print("2+2=5")
elif 2 + 2 == 4:  
    # elif: si 2+2 == 5 est faux mais que 2+2 == 4 alors on fait print("2+2=4")
    print("2+2=4")
else:  
    # else: si aucune des conditions précédentes n'est vraie alors on fait print("Je ne sais pas...")
    print("Je ne sais pas combien font 2+2")
print()
"""

# ================= BOUCLE WHILE =================
# Supprime les commentaires et exécute pour tester

"""
# C'est aussi utile pour les blocs while. While fait une action tant que la condition est true.
a = 5
while a > 0:
    print(a, "> 0 =>", a > 0)
    a -= 1
print("Fin de boucle.")
print(a, "> 0 =>", a > 0)
print()
"""

# ================= OPÉRATEURS LOGIQUES =================
# Supprime les commentaires et exécute pour tester

"""
# Tu peux combiner ces booléens grâce à des opérateurs logiques
# AND
print("AND:")
print(True and True)    # True
print(False and True)   # False
print(True and False)   # False
print(False and False)  # False
print()

# OR
print("OR:")
print(True or True)     # True
print(False or True)    # True
print(True or False)    # True
print(False or False)   # False
print()

# NOT
print("NOT:")
print(not True)         # False
print(not False)        # True
print()

# XOR
print("XOR:")
print(True ^ True)      # False
print(False ^ True)     # True
print(True ^ False)     # True
print(False ^ False)    # False
print()
"""

# ================= TYPES DE DONNÉES =================
# Supprime les commentaires et exécute pour tester
"""
# Type:
# Maintenant on va voir les types. On s'en sert depuis le début mais on n'en a pas encore parlé.
print(type(22))      # int : c'est un nombre entier
print(type(22.22))   # float : c'est un nombre à virgule flottante 
print(type([1,2,3])) # list : c'est une liste 
print(type("abc"))   # str : c'est une chaîne de caractères
print(type(True))    # bool : c'est un booléen
print()
"""

# ================= TYPES COMPLEXES ET TUPLES =================
# Supprime les commentaires et exécute pour tester

"""
# Un type dont on n'a pas encore parlé est le type complex :
print(type(2 + 1j))  # On utilise le j pour la partie imaginaire (là où en maths on utilise i) 
# Un autre est le tuple
print(type((2, 1)))
print()
"""

# ================= UTILISATION DES TUPLES =================
# Supprime les commentaires et exécute pour tester

"""
# Tuple
# Un tuple est comme un p-uplet en maths : suite ordonnée d'éléments
a = (1, 2, 3)
print(type(a))
# Tu peux donc définir plusieurs variables d'un coup :
(b, c, d) = a
print("b:", b, "c:", c, "d:", d)
print("a:", a)
print()
"""

# ================= ÉCHANGE DE VARIABLES AVEC TUPLES =================
# Supprime les commentaires et exécute pour tester

"""
# C'est également pratique pour interchanger des variables exemple :
# Sans tuple :
a = 1
b = 2 
temp = a  # On doit utiliser une variable temporaire 
a = b
b = temp 
print(a, b)

# Avec tuple
a = 1
b = 2
a, b = b, a  # Tu remarqueras que les parenthèses ne sont pas nécessaires
print(a, b)
print()
"""

# ================= ACCÈS AUX ÉLÉMENTS D'UN TUPLE =================
# Supprime les commentaires et exécute pour tester

"""
# Tu peux récupérer les éléments d'un tuple :  
a = (1, 2, 3, 4, 5)
print(a[0])  # Premier élément
print(a[4])  # Dernier élément
print()
"""

# ================= ENTRÉES UTILISATEUR AVEC INPUT =================
# Supprime les commentaires et exécute pour tester

"""
# Input permet de demander d'effectuer une requête à l'utilisateur grâce au terminal
a = input()  # Ici on stocke la valeur donnée par l'utilisateur dans a
print("Valeur de a récupérée :", a)
print()

a = input("Rentre une valeur : ")  # Ici on le fait en mettant un message de notre choix
print("Valeur de a récupérée :", a)
print()
"""

# ================= FONCTIONS PERSONNALISÉES =================
# On va maintenant voir les fonctions. On définit une fonction avec le mot clé def
# Une fonction ne s'exécute que si elle est appelée. C'est pourquoi les fonctions
# ne sont pas en commentaires par contre leurs appels sont eux en commentaires

# Définissons d'abord des fonctions:
def fonction():
    print("Fonction exécutée!")


# On peut faire une fonction qui prend des paramètres
def add(x, y):
    print(x + y)


# Maintenant les fonctions définies, appelons-les :

# Supprime les commentaires et exécute pour tester
"""
fonction()
add(2, 3)
add(7, 3)
"""

# Dans ce fichier nous n'avons pas utilisé de fonction. Note que dans un projet Python
# il est important de séparer ton code en différentes fonctions.

# ================= CONCLUSION =================
# La partie théorique de ce premier cours est finie, maintenant il faut que tu 
# pratiques, fais des tests de ton côté et fais les TP présents dans le repo.
