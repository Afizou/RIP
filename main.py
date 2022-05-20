import pandas

# recupere les donnee des fichiers csv et les convertir en dictionnaires
donnee1 = pandas.read_csv("messager1.csv")
donnee2 = pandas.read_csv("tableroutager2.csv")


def rip(data1, data2):
    reseau1 = donnee1.to_dict()
    reseau2 = donnee2.to_dict()

    # calculer le nombre de ligne de chacun des fichiers
    taille_reseau1 = len(donnee1)
    taille_reseau2 = len(donnee2)

    # creer deux listes vides
    liste1 = []
    liste2 = []
    k = -1

    # pour chaque liste  recuperer la colonne destination
    for i in range(0, taille_reseau1):
        liste1.append(reseau1["destination"][i])

    for j in range(0, taille_reseau2):
        liste2.append(reseau2["destination"][j])

    # comparer les deux listes pour connaitres les informations qui se trouvent dans la table r1(liste1) et pas dans la table r2(liste2)
    for value in liste1:
        k += 1

        # on verifie si notre reseau n'est pas dans la table de routage de r2 alors on l'ajoute dans r2
        if value not in liste2:

            l = len(reseau2['destination'])

            reseau2["destination"][l] = reseau1["destination"][k]
            reseau2["distance"][l] = reseau1["distance"][k] + 1
            reseau2["route"][l] = "R1"

        # sinon /s'il est deja dans la table de routage on a plusieurs situation
        else:
            z = 0

            # on va bocler sur tous les elements que r1 a envoye a r2 (tous elements de reseau1)
            while z < len(reseau2["destination"]):

                # si nous trouvons l'element correspondant a  notre valeur dans r2 on recuperer la distance de cet element dans les deux tables que nous comparerons
                if reseau2["destination"][z] == value:
                    distance2 = reseau2["distance"][z]
                    distance1 = reseau1["distance"][k]

                    # si la distance1 plus grande que la distance2  et que la route differente de R1 on fait rien
                    if distance1 >= distance2 and reseau2["route"][z] != "R1":
                        pass
                    # si la distance1 plus grande que la distance2 et que la route est r1 on ajoute la nouvelle valeur+1 envoyée par r1
                    elif distance1 >= distance2 and reseau2["route"][z] == "R1":
                        reseau2["distance"][z] = reseau1["distance"][k] + 1

                    # enfin si la distance envoyée par r1 est plus petite que celle de la table de routage de r2 on change la valeur de la route et de la distance
                    else:
                        reseau2["distance"][z] = distance1 + 1
                        reseau2["route"][z] = 'R1'
                z += 1

    print(pandas.DataFrame(reseau2))


rip(donnee1, donnee2)
