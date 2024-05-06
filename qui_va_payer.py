import random

print("Mettez moi les noms des personnes sous ce format :  Alice, Bob, Colin, ...")
noms_virgules = input("Donnez moi les noms de chaque personne, séparé par une virgule. \n")
noms = noms_virgules.split(", ")

nbr_personne = len(noms)-1
payeur = random.randint(0, nbr_personne)

print(f"{noms[payeur]} doit payer l'addition")

input("Appuyez sur [Enter] pour sortir.")
