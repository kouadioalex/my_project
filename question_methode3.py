#------------------------------<>--------------
def gestion_erreur(min, max):

    choix_int = input(f"entrez la bonne reponse entre ({min} et {max}) : ")
    try:
        choix_v = int(choix_int)
        if min <= choix_v <= max:
            return choix_v
        print(f'erreur, saissir un nombre compris entre {min} et {max} ')
    except:
        print(f"erreur, entrez uniquement que des nombres )")

    return gestion_erreur(min, max)


def questionnaire(question1):
    titre = question1[0]
    choix = question1[1]
    reponse = question1[2]
    global score
    print('', titre)
    for i in range(len(choix)):
        print(i+1,'-',choix[i])

    print()
    choix_v = gestion_erreur(1, len(choix))
    #if  choix_v.lower() ==reponse.lower() :
    if  choix_v ==reponse:
        print('bonne reponse !')
        score +=1
        #print('le score final est:', score)
    else:
        print('mauvaise reponse')

    print()
score = 0

def lancer_question(questionnaires):

    for question in questionnaires:
        questionnaire(question)


questionnaires=(
    ("quelle est la capitale de le Côte d'ivoire ?",('Abidjan','yamousokro','bouake','daloa', 'korogho'), 1),
    ("quelle est la capitale du Mali ?",('Nyame','Bamako','Nianssakara'),  2),
    ("quelle est la capitale du Burkina ?",('Bobo dioulasso','Ouagadougou','Mafére'), 2),
    ("quelle est la capitale du Ghana ?",('Sata','Noé','Accra'), 3)
                  )
lancer_question(questionnaires)
print('le score final est:', score)



