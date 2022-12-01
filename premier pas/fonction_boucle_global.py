#

nom= " "
age = 0
def demande_nom():
    global nom
    while nom == " ":
        nom =input("entrez votre nom: ")
    return nom

def demande_age():
    global age
    while age== 0:
        age_str= input("votre age:")
        try:
            age =int(age_str)
        except:
            print("erreur, rentrez un nombre !")
    return age

demande_nom()
demande_age()

print("Bonjour "+nom)
print("votre age est: "+str(age)+ " ans")
