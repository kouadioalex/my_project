etudiant = [("bah",25, 1.65),
            ("jean",24, 1.67),
            ("kouame", 27, 1.70),
            ("alice",23, 1.40),
            ("felicité", 17, 1.18)]

def info(nom):
    for i in etudiant:
        if i==nom:
            return True
        #return None

        print(i)

info("")
