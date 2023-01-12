grille = {'A': [None, None, None], 
          'B': [None, None, None], 
          'C': [None, None, None]
          }


def afficher_grille (grille):
    """Dessiner la grille du jeu, ligne et colonne et indicateur de position pour situer le joueur pour placer son coup"""
    print ("    0","   1","   2")
    print ("_________________")
    for clé in grille:
        print(clé, end=" ")
        
        for e in grille[clé]:
            if e==None:
                print("|", " ", "|", end="")
            else :
                print("|", e, "|", end="")
        print ("\n")
        
def coup_valide(grille, colonne, ligne):
    if colonne not in ["0","1","2"] or ligne not in ["A", "B", "C"]:
        return False  
    if grille[ligne][int(colonne)]!=None:
        return False
    return True
            
            
def jouer_un_coup (grille, joueur):
    afficher_grille(grille)
    colonne=input("Joueur, dans quelle colonne souhaitez-vous jouer ?")
    ligne=input("Dans quelle ligne souhaitez-vous jouer ?")
    while not coup_valide(grille, colonne, ligne):
        print("Le coup n'est pas valide !")
        colonne=input("Joueur, dans quelle colonne souhaitez-vous jouer ?")
        ligne=input("Dans quelle ligne souhaitez-vous jouer ?")
    grille[ligne][int(colonne)]=joueur

def victoire(grille):
    if (grille["A"][0]==grille["A"][1]==grille["A"][2])=="X"or (grille["B"][0]==grille["B"][1]==grille["B"][2])=="X"or (grille["C"][0]==grille["C"][1]==grille["C"][2])=="X"or (grille["A"][0]==grille["B"][0]==grille["C"][0])=="X"or (grille["A"][1]==grille["B"][1]==grille["C"][1])=="X"or (grille["A"][2]==grille["B"][2]==grille["C"][2])=="X"or (grille["A"][0]==grille["B"][1]==grille["C"][2])=="X"or (grille["C"][0]==grille["B"][0]==grille["A"][0])=="X":
        return True
    elif (grille["A"][0]==grille["A"][1]==grille["A"][2])=="O"or (grille["B"][0]==grille["B"][1]==grille["B"][2])=="O"or (grille["C"][0]==grille["C"][1]==grille["C"][2])=="O"or (grille["A"][0]==grille["B"][0]==grille["C"][0])=="O"or (grille["A"][1]==grille["B"][1]==grille["C"][1])=="O"or (grille["A"][2]==grille["B"][2]==grille["C"][2])=="O"or (grille["A"][0]==grille["B"][1]==grille["C"][2])=="O"or (grille["C"][0]==grille["B"][0]==grille["A"][0])=="O":
        return True
    else :
        return False

def est_gagnee(grille)-> bool:
    for clé in grille:
        if grille[clé][0]==grille[clé][1]==grille[clé][2]and grille[clé][0]!=None:
            return True
    for i in range(3):
        if grille["A"][i]==grille["B"][i]==grille["C"][i] and grille["A"][i]!=None:
            return True
    if grille["A"][0]==grille["B"][1]==grille["C"][2] and grille["A"][0]!=None:
            return True
    if grille["A"][2]==grille["B"][2]==grille["C"][2] and grille["A"][2]!=None:
        return False
    
    
def morpion(grille):
    while not est_gagnee(grille):
        if not est_gagnee(grille):
            jouer_un_coup (grille, "X")
        if not est_gagnee(grille):
            jouer_un_coup (grille, "Y")
    print ("C'est finiii")
        
        
morpion(grille)