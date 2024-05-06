import random

nombre_secret = random.randint(1, 10)


end_game = False
while not end_game:
    choix = int(input("Quel nombre penses-tu que j'ai ? "))
    if choix < nombre_secret:
        print("Trop bas")
    elif choix > nombre_secret:
        print("Trop grand.")
    else:
        print("Tu as gagné!")
        ciao = input("Tu veux encore joué ? Si oui, tape 'encore' ou 'quitter' pour sortir ").lower()
        if ciao == "encore":
            nombre_secret = random.randint(1, 10)
            print("C'est reparti!")
        else:
            print("Aurevoir!")
            end_game = True
