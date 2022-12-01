
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
ages2= demande_age(noms2)

print("Bonjour "+noms1)
print("votre age est: "+str(ages1)+ " ans")

print("Bonjour "+noms2)
print("votre age est: "+str(ages2)+ " ans")
