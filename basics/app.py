# ***********************************VAR TYPES***************************************


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
