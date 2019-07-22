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

# *********************************STRINGS**************************

course = 'Python programing'

print(len(course))  # 18 donne la longueur de la chaîne de caractère
print(course[0])  # P affiche le 1er élément de la chaîne
print(course[-1])  # g affiche le premier élément en partant de la fin
print(course[0:3])  # Pyt affiche de la premiere lettre jusqu'à la 4ème EXCLUE
print(course[:3])  # affiche de 0 jusqu'à la 4eme lettre
print(course[0:])  # affiche de 0 jusqu'à la fin
print(course[:])  # affiche toute la chaîne.

# *****************************ESCAPE SEQUENCES***************************

# cela permet tout simplement d'afficher visuellement des "" dans une string en utilisant \ juste devant.
# on utilise aussi /n pour revenir à la ligne
