#
#---------<>--------
def fonction(a, limit):
    if a > limit:
        return
    print(f"la valeur est: {a}")
    fonction(a*a, limit)
        
fonction(2, 100)