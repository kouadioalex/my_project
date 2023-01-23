#
nom= ""
while nom == "":
    nom =input("entrez votre nom: ")

age=0
while (age== 0):
        age_str = input("entrez votre age:")
        try:
            age= int(age_str)
            age_pro = age+ 1
        except:
            print("ERREUR, entrez un nombre: ")

print( )
print("Bonjour Mr "+ nom +" vous avez "+ str(age)+ " ans")
print("Votre âge prochain est: "+ str(age_pro) +" ans")
