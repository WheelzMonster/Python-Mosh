# Une séquence (comme les listes et chaines de caractères) sont des structures de données ordonnées!

# EXERCICE 1****************************************************************************************

# reponse = input(
#     "saisissez vos couleurs préférées, si vous choisissez stop le programme s'arrête: ")
# mesCouleurs = []

# while reponse != 'stop':
#     mesCouleurs.append(reponse)
#     reponse = input(
#         "saisissez vos couleurs préférées, si vous choisissez stop le programme s'arrête: ")

# for couleur in mesCouleurs:
#     print(couleur)


# EXERCICE 3*************************************************************************************

# def valide(saisie):
#     if saisie == '':
#         return False
#     for x in saisie:
#         if x not in 'atgc':
#             return False


# chaine = input("saisissez une chaine ADN: ")

# while valide(chaine) == False:
#     print("saisie incorrect")
#     chaine = input("saisissez une chaine ADN: ")

# sequence = input("saisissez une séquence ADN: ")

# while valide(sequence) == False:
#     print("saisie incorrect")
#     sequence = input("saisissez une sequence ADN: ")


# def ADN(sequenceADN, chaineADN):
#     i = 0
#     for chaineADN in sequenceADN:
#         if chaine in chaineADN:
#             i += 1
#     print("la chaine apparait", i, "fois dans la sequence")


# print("la séquence ADN: ", sequence)
# print("la chaine ADN: ", chaine)
# ADN(sequence, chaine)

# RECOPIER LA FIN SUR MYLEARNING BOX

# EXERCICE 4 *****************************************************************************************

saisieNote = input('veuillez saisir chaque notes séparées par un espace: ')
listresult = saisieNote.split()

listresult = [int(i) for i in listresult]
print(listresult)
