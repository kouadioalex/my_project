#
"""personne = {"nom":"bah", "age": 23, 'taille':1.65}

personne['poste'] ="devellopeur"

achat = ("fromage", "hanbergeur", "panini")

personne['achat'] = achat

for i in personne:
    print(f"clé: {i} - valeur {personne[i]}")
    #print(i)
    #print(personne[i])
"""

personne = [ ("melanie",28, 1.45),
            ("paul", 35, 1.33),
            ("adama", 18, 1.40),
            ("kone", 12, 1.17)
]

def affichage(nom , liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None


result= affichage('adama',personne)
print(result)

personne_dict = {"melanie": (26, 1.56),
                 "paul": (45, 1.77),
                 "kone": (23, 1.22),
                 "fatou": (36, 1.55)}

info = personne_dict.get("paul")
if not info:
#if info==None:
    print("il n'existe pas")
print(info)




