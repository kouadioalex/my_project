pizza_nom = ("4-fromage", "calzone", "hawai")
pizza_prix = (3700, 4400, 3500)

zip(pizza_nom, pizza_prix)

liste =list( zip(pizza_nom, pizza_prix))

print("le nom et les prix des fromage: ")
for (nom, prix) in liste:

    print(f"{nom}- {prix} cfa")
