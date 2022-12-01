import random

nb_min = 1
nb_max = 10
nombre_question = 7
"""
def calcul_aleatoire():

#---------------------avec for----------------

    for i in range(1, nombre_question):
        nombre_point =0
        
        if nbr==(a+b):
            nombre_point += 1
            print("le nombre de point est: ", nombre_point)
        else:
            print("vous n'avez rien trouvez !")

        print(f"question n° {i} sur {nombre_question}")
        nb = nombre_question - i
        # print(f"question n° {nb} ")
        a = random.randint(nb_min, nb_max)
        b = random.randint(nb_min, nb_max)

        nbr = input(f"entrez le nombre {a} + {b} est egale à :")
        nombre= int(nbr)
        if nombre==(a+b):

            print("resultat correcte !")
        else:
            print("resultat incorrecte !")


    print(f"le nombre de point est {nombre_point}")

calcul_aleatoire()

"""
# ----------------connecte le nombrede point---------------

def calcul_aleatoire():
    # ---------------------avec for----------------
    a = random.randint(nb_min, nb_max)
    b = random.randint(nb_min, nb_max)
    p = random.randint(0, 1)
    operateur = " +"
    if p == 1:
        operateur= " *"

    nbr = input(f"entrez le nombre {a} {operateur} {b} est egale à :")
    nombre = int(nbr)
    calcul= (a + b)
    if p ==1:
        calcul= (a * b)

    if nombre == calcul:
        return True

    return False

nombre_point=0
for i in range(0, nombre_question):
    print(f"question n° {i} sur {nombre_question}")
    if calcul_aleatoire():
        nombre_point += 1
        print("resultat correcte !")
    else:
        print("resultat incorrecte !")
    print()

print(f"le resutat de votre test est {nombre_point} / {nombre_question}")

#------------------<>----------------
moy= (nombre_point/2)
moygen= (nombre_question/2)
if moy >= moygen:
    print("Bravo ! vous etre excellente")
else:
    print("passable")





