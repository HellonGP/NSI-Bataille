from random import shuffle
from termcolor import colored
import time


#Variables
Couleurs = ("♦","♥","♣", "♠")
Numéros = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
milieu = [] #Liste vide qui sert à stocker les cartes posées au milieu pendant le jeu
paquet = [n + c for c in Couleurs for n in Numéros] #Création du paquet en liste
dicts = {} #Création dictionnaire vide pour le remplir automatiquement avec les cartes + valeurs
valeurs =  [1,2,3,4,5,6,7,8]*4 #Valeurs que l'on va donner aux cartes pour qu'elles puissent être comparées
global v_rouge, v_bleu
v_rouge = 0
v_bleu = 0
for i in range(32): #Boucle 32 car 32 cartes
    dicts[paquet[i]] = valeurs[i] #En gros: on prend comme clé une carte de la liste "paquet" et puis on lui assigne la valeur à partir de la liste "valeurs". Exemple : '7♦': 1  (Ici la valeur "7♦" à la valeur 1 assignée, ce qui nous permet de la comparer avec les autres valeurs)

#Classe (c'est classe) 
class Jeu: #Création de la classe
    def __init__(self): #Constructeur
        self.paquet_complet = [n+c for c in Couleurs for n in Numéros] #Création attribut "paquet_complet", on prend tous les "n" pris dans la liste Numéros auquel on ajoute le premier symbole (ici c'est "♦"), ainsi de suite avec les autres symboles
    def couper(self): #Fonction pour mélanger le paquet et le distribuer en 2
        shuffle(self.paquet_complet) #Mélange avec la fonction shuffle du module random
        self.paquet_rouge = self.paquet_complet[:16] #On prends 16 cartes en partant du début du "paquet_complet"
        self.paquet_bleu = self.paquet_complet[16:] #On prends 16 cartes jusqu'à la fin du "paquet_complet"
        return "Le paquet a été mélangé et les deux paquets ont été distribués" + "\n---"
    def jouer_partie(self): #Fonction pour jouer la partie tout simplement
        global v_rouge, v_bleu
        jeu_en_cours = True #On dit que le jeu est en cours: c'est pour la boucle While
        while jeu_en_cours == True: 
            if self.paquet_rouge != [] and self.paquet_bleu != []: #On vérifie si le paquet de l'un des joueurs est vide et si c'est le cas on regarde qui c'est.
                X = self.paquet_rouge.pop(0) #On assigne à une variable la carte qui a été tirée du paquet rouge
                Y = self.paquet_bleu.pop(0) #On assigne à une variable la carte qui a été tirée du paquet bleu
                valeur_X = dicts.get(X) #On recherche dans le dictionnaire la valeur de la carte rouge
                valeur_Y = dicts.get(Y) #On recherche dans le dictionnaire la valeur de la carte bleu
                milieu.append(X) #On ajoute à la pile du milieu la carte rouge
                milieu.append(Y) #On ajoute à la pile du milieu la carte bleu
                print(colored("le joueur bleu joue ", "cyan",attrs=["bold"]) + milieu[-1] + colored("\nle joueur rouge joue ","red",attrs=["bold"])+ milieu[-2]+"\n---")
                if valeur_X > valeur_Y: #Carte rouge est supérieure à carte bleu
                    shuffle(milieu) #On mélange pour reproduire une vraie partie de bataille, c'est à dire qu'on met en dessous de notre paquet les cartes en désordre (et si on laisse en ordre, alors la bataille dure 200h parce que le paquet est alors ordonné et on a un déroulement looooong)
                    self.paquet_rouge.extend(milieu) #Ajout de la pile au milieu dans le paquet du rouge
                    print (colored("Le joueur rouge gagne ce combat et il remporte : ","red","on_white"), milieu,"\n---")
                    milieu.clear() #Reset de la pile du milieu
                    v_rouge += 1 #Pour avoir des stats
                    time.sleep(0.5)
                elif valeur_X < valeur_Y: #Carte bleu est supérieure à carte rouge
                    shuffle(milieu)
                    self.paquet_bleu.extend(milieu) #Ajout de la pile au milieu dans le paquet du bleu
                    print(colored("Le joueur bleu gagne ce combat et il remporte : ","blue","on_white"), milieu,   "\n---")
                    milieu.clear() #Reset de la pile du milieu
                    v_bleu += 1 #Pour avoir des stats
                    time.sleep(0.5)
                else: #Egalité
                    print(colored("Il y'a égalité, c'est la guerre !!!","magenta",attrs=["bold"])+"\n---")
                    if self.paquet_rouge == [] or self.paquet_bleu == []:
                        if self.paquet_rouge == []:
                            print("Le joueur rouge n'a plus de carte, le joueur bleu va donc tirer une carte :")
                            ultime_carte = self.paquet_bleu.pop(0)
                            valeur_ult = dicts.get(ultime_carte)
                            milieu.append(ultime_carte)
                            if valeur_ult > valeur_X:
                                self.paquet_bleu.extend(milieu)
                                print(colored("Le joueur bleu gagne ce combat et il remporte : ","blue","on_white"), milieu,   "\n---")
                                self.jouer_partie()
                            else:
                                self.paquet_rouge.extend(milieu)
                                print (colored("Le joueur rouge gagne ce combat et il remporte : ","red","on_white"), milieu,"\n---")
                                self.jouer_partie()
                        else:
                            print("Le joueur bleu n'a plus de carte, le joueur rouge va donc tirer une carte :")
                            ultime_carte = self.paquet_rouge.pop(0)
                            valeur_ult = dicts.get(ultime_carte)
                            milieu.append(ultime_carte)
                            if valeur_ult > valeur_X:
                                self.paquet_rouge.extend(milieu)
                                print(colored("Le joueur rouge gagne ce combat et il remporte : ","blue","on_white"), milieu,   "\n---")
                                self.jouer_partie()
                            else:
                                self.paquet_bleu.extend(milieu)
                                print (colored("Le joueur bleu gagne ce combat et il remporte : ","red","on_white"), milieu,"\n---")
                                self.jouer_partie()
                    else:
                        milieu.append(self.paquet_rouge.pop(0)) #On prends la carte face cachée dans le paquet rouge
                        milieu.append(self.paquet_bleu.pop(0)) #On prends la carte face cachée dans le paquet bleu
                        self.jouer_partie() #Appel récursif pour retester les 2 cartes qui ont été tirées après les cartes faces cachées
            else: #Si l'un des deux paquets est vide alors:
                if self.paquet_rouge ==[]: #Si c'est le paquet du joueur rouge qui est vide...
                    jeu_en_cours = False #Alors on dit que la boucle s'arrête...
                    return "Joueur bleu a gagné !!!"+" Il a gagné : ",v_bleu," combats alors que le joueur rouge a gagné : ",v_rouge," combats."
                elif self.paquet_bleu==[]: #Sinon c'est le paquet du joueur bleu qui est vide...
                    jeu_en_cours = False #On arrête la boucle et le jeu
                    return "Joueur rouge a gagné !!!"+" Il a gagné : ",v_rouge," combats alors que le joueur bleu a gagné : ",v_bleu," combats." #Et on dit que le joueur rouge à gagné plus quelques stats
                else:
                    return "y'a un problème là"
        


#Petit code pour créer instance et "lancer" la classe        
p = Jeu() #Création instance
print(p.couper()) #Mélange+coupe le paquet
print(p.jouer_partie()) #Lancement de la partie





'''COPYRIGHT BY FBI and Hellon'''
