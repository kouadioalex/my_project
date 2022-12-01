#
def chaine_caractere(chaine):
    return any( [ c.isdigit() for  c in chaine ])

nom = input("entrez le nom : ")
if nom==" ":
    print(" votre nom est vide ")
elif chaine_caractere(nom):
    print("ce nom est invalide, il contient des chiffre ")
else:
    print("bonjour " + nom)








