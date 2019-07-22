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
