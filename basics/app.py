# ***********************************VAR TYPES***************************************


import math
studentCount = 1000
rating = 4.99
isPublished = True  # Important ! c'est un T maj
courseName = "Python"
Paragraph = """
Je peux faire ceci sur plusieurs lignes
grâce aux triples guillemets"""

x = 1
y = 2

# même chose*****************************

x, y = 1, 2

# si deux variables ont la même valeur on peut faire :

x = y = 3


# *********************************STRINGS******************************


course = 'Python programing'

print(len(course))  # 18 donne la longueur de la chaîne de caractère
print(course[0])  # P affiche le 1er élément de la chaîne
print(course[-1])  # g affiche le premier élément en partant de la fin
print(course[0:3])  # Pyt affiche de la premiere lettre jusqu'à la 4ème EXCLUE
print(course[:3])  # affiche de 0 jusqu'à la 4eme lettre
print(course[0:])  # affiche de 0 jusqu'à la fin
print(course[:])  # affiche toute la chaîne.


# *****************************ESCAPE SEQUENCES***************************


# cela permet tout simplement d'afficher visuellement des "" ou autres caractères dans une string en utilisant \ juste devant.

# exemple : // /' /"" servent à ce qu'apparaissent visuellement ces caractères dans une string. Apparaissent ici respectivement un / un simple quote ' et un double ""

# on utilise aussi /n pour revenir à la ligne


# *****************************FORMATTED STRINGS***************************


# sert à implémenter des variables dans une chaîne de caractère sans devoir gérer les esspaces etc

first = 'louis'
last = 'escartin'
full = f"{first} {last}"  # louis escartin

# on peut aussi faire directement des calculs etc entre les {}

full2 = f"{len(first)} {3 + 2}"  # 5 5


# *****************************USEFUL STRINGS METHODS***************************

course = 'Python Programmation'

course.upper()  # convertie toute la chaine de caractère en majuscule
course.lower()  # convertie toute la chaine de caractère en minuscule
course.title()  # ajoute une majuscule au début de chaque mots de la chaîne de caractères
course.strip()  # enlève tout les espaces en trop au début où à la fin de la chaîne de caractère,il existe aussi rstrip et lstrip
course.find("pro")
# pour des meilleurs info, souris sur method, ça cherche a quel index se trouve la sub. -1 si rien n'est trouvé

course.replace("P", "j")
# Jython Jrogramming, remplace une ancienne valeur (arg1) par une nouvelle valeur (arg2)

"Programmation" in course
# regarde si une string est inclue dans une variable, si oui renvoi True, sinon renvoi False

"Programmation" not in course
# regarde si une string n'est pas inclue dans une variable, si oui renvoi True, sinon renvoi False


# **************************************NUMBERS************************************


# En python, on peut aussi travailler avec des nombres sous forme binaire de la façon suivante : 0b + notre chiffre en binaire

x = 0b10  # affiche 2

# Pour afficher un nombre sous sa forme binaire on utilise la méthode bin

print(bin(x))  # 0b10

# En python, on peut aussi travailler avec des nombres sous forme héxadécimale de la façon suivante : 0b + notre chiffre en binaire

x = 0x12c  # affiche 300

# Pour afficher un nombre sous sa forme binaire on utilise la méthode bin

print(hex(x))  # 0x12c

# Les nombres complexes de forme a + bi se font avec J

complexe = 1 + 2J

# Pour les opérateurs arithmétiques on connait les bases + - * / mais il en existe d'autres :

10 // 3  # les deux / représente une divison dont le résultat est ramené à l'entier le plus proche
10 % 3  # le reste de la division de 10 par 3, ici 1
10 ** 3  # 10 à la puissance 3 donc ici 1000

# il y a une version raccourcie lorsqu'on fait une assignation de valeure

x = x + 1  # x += 1 est identique, ça marche pour le + mais aussi pour tous les autres opérateurs ci-dessus

# Note importante, en python le ++, -- etc pour faire +1, -1 etc n'existe pas


# *****************************USEFUL NUMBER METHODS***************************

round(5.7)  # pour la valeur arrondie
abs(55)  # pour la valeur absolue

# On peut importer le module Math pour avoir plusieurs propriété, pour les voir il suffit de faire math. et regarder la liste


math.floor(4.5)  # arrondie a l'inferieur

# Note : taper python built-in functions ou python 3 math module en ce qui concerne l'import math pour plus d'info


# *****************************TYPE CONVERSION***************************

# Il y a 4 méthodes pour convertir des types de variable

str()  # chaine de caractère
int()  # nombre entier
bool()  # booléen
float()  # nombre a virgule

# lorsqu'on convertie un type en bool il faut prendre en compte les "Falsy value" qui sont les suivantes

bool('')
bool(0)
bool([])
bool(None)  # ou null

# tout cela renvoi false


# *****************************CONDITIONS, LOGICAL AND TERNARY OPERATORS***************************

# Les if else on connait c'est simple il faut juste pas oublier : à la fin de la condition et regarder l'indentation

age = 26

if age > 21:
    print("you're allowed in")
else:
    print("you're not allowed in")

# pour les opérateurs il y a : and, or, not


name = ''

if not name.strip():  # si le nom est vide (donc que name vaut false puisqu'une chaine vide renvoi false) alors grace au not la condition vaut true donc on rentre dans le block mais si name n'est PAS vide (donc que name vaut true comme toute chaine non vide) alors grace au not la condition vaut false et on ne rentre pas dans le block (le strip c'est pour enlever les espaces car sinon la chaîne pourrait ne pas être considéré comme vide même si rien n'est écrit dedans)
    print('name is empty')


# pour certaines conditions plutot que d'utiliser le 'and' on peut faire ça :

age = 22

if 18 <= age < 65:
    print("you're eligible")

# age = 22
# if age >= 18:
#   message = "eligible"
# else :
#   message = "not eligible"

# l'équivalent de ceci avec l'opérateur ternaire c'est ça :

message = 'eligible' if age >= 18 else "not eligible"


# ***********************************************LOOPS****************************************


# FOR LOOP *************************************************


# Pour les chaines de caractères les lists etc on utilise for in

string = 'chaine'

for lettre in string:
    print(lettre)

for x in ['a', 'b', 'c']:
    print(x)

# Si on veut faire tourner la boucle un certain nombre de fois on utilise la fonction range()

for loop in range(5):
    print(loop)  # affichera 1, 2,3,4,5 en colonne

# la fonction range peut prendre 3 arguments (début, fin(non inclue), pas) donc pour les paires de 0 a 10 non inclue on  fait :

for paires in range(0, 10, 2):
    print(paires)

# regarder dans notes.md pour plus d'infos sur range


# FOR ... ELSE LOOP*************************************************


namesArr = ['AJohn', 'Mary']

for name in namesArr:
    if name.startswith('J'):
        print('found')
        break  # arrête la boucle for
else:
    print('not found')

# dans une boucle for ... else, si la boucle s'exécute en entier (c'est-à-dire sans break) alors
# le code dans le else sera exécuté. Si la boucle n'arrive pas au bout alors le else est ignoré.


# WHILE LOOP*************************************************


guess = 0
answer = 5

while guess != answer:
    guess = int(input('guess the number: '))
print('number guessed!')

# On peut aussi rajouter un else après le while comme avec le for, et il ne s'exécutera que si la boucle while est exécuté en entier sans break


# ***********************************************FUNCTIONS**************************************************


# On créer le squelette de base d'une fonctions qui prend un nombre et lui ajoute un autre nombre

def increment(number, by):
    return number + by


# on fait l'appel de la fonction et on donne une valeur à chaque paramètres
increment(2, 5)

# Pour renvoyer plusieurs valeurs à la fois il suffit de faire dans la fonction increment :
# return (number, number + by) ce qui renverra : (2, 7) Ce resultat est appelé 'Tuple'

# Un tuple est comme une list mais qu'on ne peut pas modifier, qui est en read-only, il s'ecrit comme une list mais avec des ()

# Pour rajouter de la lisibilité à notre code on peut utiliser des keyword arguments dans l'appel de la fonction :

increment(2, by=5)

# On peut utiliser des paramètres par défaut pour les fonctions


def maFonction(number, by=1):
    return number + by


maFonction(5)
# renvoi 6 car si l'on ne donne pas de valeur à un paramètre de notre fonction auquel on a associé une valeur par défaut, il prendra cette valeur.

# Pour rendre notre fonction encore plus lisible on peut utiliser du type hinting, c'est à dire écrire le type de chaque élément de notre fonction sous cette forme


# le type après la flèche représente le type de l'elément retourné par la fonction:
def testFonction(number: int, by: int = 1) -> int:
    return number + by


# XARGS******************************************************************************
