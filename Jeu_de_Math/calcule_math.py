#
#

def math(prnb, denb):

#------------methode1-------------
    """a=4
    b= 13
    calcul = a+b
    print(f"la somme de a et b est {calcul}")"""

#----------------methode2-------------------
    """nb1 = input("entrez le 1er nombre  ")
    nb2 = input("entrez le 2er nombre  ")
    nbr = int(nb1)+ int(nb2)
    print(f" la somme de {nb1} et {nb2} est egal à  {nbr}")"""

#---------------------methode3-----------------
    nbs= 2

    for i in range(0 , nbs):
        nb1 = input(f"entrez le {prnb}er et {denb}ième nombre  ")
        nbr = int(nb1)+int(nb1)
    print(f" la somme de {nb1} et {nb1} est egal à  {nbr}")
math(1, 2)
