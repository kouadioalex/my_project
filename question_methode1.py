#-----------------------methode simple-----------------
def questionnaire(r0,r1, r2,r3, reponse):
    global score
    print(r0)
    print('a-', r1)
    print('b-',r2)
    print('c-',r3)

    choix = input("entrez la bonne reponse: ")
    print()
    if  choix ==reponse :
        print('bonne reponse !')
        score += 0
    else:
        print('mauvaise reponse')
    print()
score =0
questionnaire("quelle est la capitale du Mali ?",'Nyame','Bamako',' Nianssakara', 'b')
questionnaire("quelle est la capitale du Burkina ?",'Bobo dioulasso','Ouagadougou',' Mafére', 'b')
questionnaire("quelle est la capitale de le Côte d'ivoire ?",'Abidjan','yamousokro','bouake', 'a')
questionnaire("quelle est la capitale du Ghana ?",'Sata','Noé','Accra','c')
print(score)

