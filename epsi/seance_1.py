from math import sqrt
from random import randint

# EXERCICE1********************************************************************************

# age = int(input(" quel age as-tu ? "))

# if age >= 18:
#     print("vous etes majeurs")
# else:
#     print("vous etes mineur")

# EXERCICE2***********************************************************************************

# a = int(input("choisissez a: "))
# b = int(input("choisissez b: "))
# c = int(input("choisissez c: "))

# delta = b**2 - (4*a*c)

# if delta > 0:
#     print("il y a 2 racines:")
#     racine1 = (-b - sqrt(delta)) / 2*a
#     racine2 = (-b + sqrt(delta)) / 2*a
#     print(racine1)
#     print(racine2)

# elif delta == 0:
#     print("il y a une racine")
#     racine1 = -b / 2*a
#     print(racine1)
# else:
#     print("il n'y a pas de racine")

# Exercice 3*************************************************************************************

# reponse = int(
#     input("saisissez une valeur, si vous choisissez 0 le programme s'arrête"))
# sommeEntier = 0
# nombreDeSaisies = 1
# EntierSuperieur100 = []

# while reponse != 0:
#     if reponse > 100:
#         EntierSuperieur100.append(reponse)
#     sommeEntier += reponse
#     nombreDeSaisies = nombreDeSaisies + 1
#     reponse = int(
#         input("saisissez une valeur, si vous choisissez 0 le programme s'arrête"))


# print(sommeEntier, nombreDeSaisies, EntierSuperieur100)

# Exercice 4**********************************************************************************

# nombre = int(input("choisissez un nombre: "))
# limite = nombre // 2
# diviseur = []

# for i in range(1, limite+1):
#     if limite % i == 0:
#         diviseur.append(i)

# diviseur.append(nombre)
# print("liste des diviseurs : ", diviseur)

# Exercice 5

nombre = randint(0, 100)
reponse = int(input("Devinez le nombre entre 0 et 100: "))

while reponse != nombre:
    reponse = int(input("choisissez un autre nombre: "))
    if reponse > nombre:
        print("c'est moins")
    elif reponse < nombre:
        print("c'est plus")
    else:
        print("c'est gagné")
