#-------une fonction d'affichage-------#
#--------<>------

def affichage( nom, age):
    print()
    print("Bonjour " + nom + "votre age est: " + str(age) + " ans")
    print("L'ans prochain vous aurrai " + str ((age)+1 ) + " ans")

    if age < 10:
        print("vous êtes enfant")
    elif age == 17:
        print("vous êtes mineur, l'ans prochain vous serai majeur")
    elif age ==18:
        print("felicitation , vous êtes majeur")
    elif age < 68:
        print("vous etre majeur")
    elif age >= 68:
        print("vous êtes sénior")
    else:
        print(" vous êtes mineur ")

    """condition = age >=18
    if condition :
        print("vous êtes majeur")
    else:
        print(" vous êtes mineur ")"""

def demande_nom():
    nom= " "
    while nom == " ":
        nom =input("entrez votre nom: ")
    return nom

def demande_age(nom_pers):
    age = 0
    while age== 0:
        age_str= input(nom_pers+ " votre age:")
        try:
            age =int(age_str)
        except:
            print("erreur, rentrez un nombre !")

    return age

noms1= demande_nom()
noms2= demande_nom()

ages1= demande_age(noms1)
ages2= demande_age( noms2)

affic= affichage(noms1 ,ages1)
affic= affichage(noms2,ages2)
nb_per = 4
for i in range(0 , nb_per):
    nom = input(" personne n°")
    age = demande_age(nom)
    affichage( nom, age )


