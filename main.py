
from classe_livre import *
list_livres = []
livre_1 = Livre()
livre_1.Titre = input("Entrez le titre du livre : " )
livre_1.Auteur = input("Entrez l'auteur du livre : ")
while True :
    try:
        livre_1.Prix = float(input("Entrez le prix du livre : "))
    except :
        print("Entrez un nombre entier svp.. : ")

    else :
        if livre_1.Prix < 50 :
            break
        else :
            print("Entrer un nombre inferieur à 50")
print(livre_1.Titre , livre_1.Auteur, livre_1.Prix)

list_livres.append(livre_1)



