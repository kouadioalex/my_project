#
#---------excercice sur la convertion ---------------------
"""def convertion(pouce, cm):
    nmb= 0
    while nmb==0:
        nombre= input("entrez un nombre: ")
        try:
            nmb= int(nombre)
        except:
            print("erreur, entrez un nombre")

    choix= 0
    while choix==0:
        nomb= input("entrez 1 ou 2: ")
        try:
            choix= int(nomb)
        except:
            print("erreur, entre un nombre  comprir entre 1 ou 2")

    a= int(choix)
    if a==1:
        pcs = float(nmb)*pouce
        print(f"convertion de pouce vers cm est {pcs} en pouce")
    elif a ==2:
        pcs = float(nmb) * cm
        print(f"convertion de cm vers pouce est {pcs} en cm")
    else:
        print("entrez un nombre")

##------<>

convertion(2.54, 0.394 )
"""
#----------------------excercice sur la cuison des ouefs  --------------------

"""
Cuisson des oeufs
Vous aimez les oeufs à la coque, ou les oeufs durs ? Dans tous les cas le plus important c'est de respecter la cuisson.

Pour cet exercice de code, vous allez réaliser un programme de type "minuteur" qui permettra d'afficher en temps réel le temps restant de cuisson.

-> Votre programme proposera 3 options :

- Oeufs à la coque : 3 minutes

- Oeufs mollets : 6 minutes

- Oeufs durs : 9 minutes

Une fois l'option choisie, votre programme commencera à attendre la durée concernée.

A chaque seconde, vous afficherez un "." sur une même ligne (afin que l'on voit un effet de progression).

Et toutes les 10 secondes vous irez à la ligne suivante en affichant le temps restant.

Exemple:
..........

Temps restant : 2:50..........

Temps restant : 2:40.....

(voir la vidéo ci-dessus pour avoir une illustration)

Quand le temps est écoulé, vous afficherez "Cuisson terminée", et votre programme se terminera.

BONUS : Vous pourrez aussi jouer un son une fois la cuisson terminée


"""

#
