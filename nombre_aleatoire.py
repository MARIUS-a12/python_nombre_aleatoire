import random
nombre_secret = random.randint(1, 100)
print("Bienvenue!")
proposition = int(input("Entrez un nombre de votre choix: "))

compteur = 1
while proposition != nombre_secret:
    if proposition < 1 or proposition> 100:
        print("entrez un nombre entre 1 et 100")
    elif proposition > nombre_secret:
        print("Votre nombre est trop élevé")
        compteur +=1
    elif proposition < nombre_secret:
        print("Votre nombre est trop bas")
        compteur +=1
    proposition = int(input("Reessayez avec un autre nombre: "))
    
else:
    print("Félicitations")
print("Vous avez trouvé en ", compteur, "tentatives")
   